# main.py
from fastapi import FastAPI
from fastapi.responses import FileResponse
import pandas as pd
from os import path, stat
import json
from json.decoder import JSONDecodeError

filename = 'data.json'
from npi import npi_calculator

app = FastAPI()

@app.get("/")
async def root():
    return {"greeting":"hello"}

@app.post("/calcul")
async def calcul(data: str):
    # On retire les single et double quotes afin de ne pas concaténer au moment de recréer notre liste
    data = data.replace('"', '').replace("'", "").strip('][').split(',')
    # On gère le cas où il n'y a pas d'espace devant un élément de la liste.
    data = [i.strip(' ') for i in data]
    print('data :',data)
    calc = npi_calculator(data)

    df = []
    # On vérifie que le fichier existe
    if path.isfile(filename) is False:
        pass
    # Sinon
    else: 
        with open(filename) as f:
            # On essaie de charger le fichier json
            try:
                df = json.load(f)
            # Si le fichier est vide alors on lève l'exception
            except JSONDecodeError:
                pass

    with open(filename, "w+") as f: 
        try:
            # On ajoute notre requête à notre liste
            df.append({"id":len(df), "operation":str(data), "resultat":calc})
            f.write(json.dumps(df, indent=4))
        except:
            raise Exception("Erreur lors de l'enregistrement")
    
    return {"result":calc}

@app.get("/getCsv")
async def get_data():
    # On vérifie que le fichier existe et qu'il a un poid supérieur à 0 kilo-Octet
    if (path.isfile(filename) is True) and (stat(filename).st_size > 0):
        # On récupère les données du fichier pour les stocker dans un DataFrame
        df = pd.read_json(filename)
        df.to_csv("db.csv", index=False)
        # On prépare l'envoi du fichier .csv
        response = FileResponse('db.csv', media_type="text/csv")
        # On indique qu'il s'agit d'un fichier de type .csv dans l'en-tête de la réponse
        response.headers["Content-Disposition"] = "attachment; filename=downloaded_file.csv"
        return response
    # Sinon on renvoi une erreur
    else: 
        return {"result":"Aucune donnée disponible"}
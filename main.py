# main.py
from fastapi import FastAPI
import pandas as pd
from os import path
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
        raise Exception("File not found")
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
            f.write(json.dumps(df, indent=2))
        except:
            raise Exception("Erreur lors de l'enregistrement")
    
    return {"result":calc}

@app.get("/getCsv")
async def get_data():
    # On initialise un tableau vide
    df = []
    # On vérifie que le fichier existe
    if path.isfile(filename) is False:
        raise Exception("File not found")
    # Sinon
    else: 
        with open(filename) as f:
            # On essaie de charger le fichier json
            try:
                df = json.load(f)
                pdf = pd.read_json(df)
                pdf.to_csv('./files/db.csv', index=False)
            # Si le fichier est vide alors on lève l'exception
            except JSONDecodeError:
                pass
    return df
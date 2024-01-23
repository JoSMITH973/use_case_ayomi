# API NPI (Notation Polonais Inversé)

Cet API permet :
- Effectuer des calculs en NPI grâce à une liste envoyé sous forme d'une chaine de charactère sous la forme suivante : [1, 2, "+", 6, '5', "*", "+"]
- Récupérer tous les calculs effectués sous format .csv.

Pour créer un conteneur et le lancer :
- lancer la commande : docker image build . -t "nom_souhaité"
- docker container run -t nom_souhaité:latest -p 8000:8000

__________

Projet réalisé en Python (3.10.2)

librairies utilisées :
- fastapi (0.109.0)
- uvicorn (0.27.0)
- pandas (2.2.0)

__________

Auteur :
SMITH Joan
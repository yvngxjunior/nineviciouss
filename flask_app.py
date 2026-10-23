# ---------------------------------------------------------------
#  Mon premier site Web avec Flask
# ---------------------------------------------------------------
#  Ce fichier est le "cerveau" de votre site : c'est lui qui
#  reçoit les demandes des navigateurs et qui fabrique les réponses.
#
#  Vous allez le compléter petit à petit, exercice après exercice.
#  Les consignes sont dans le dossier "exercices/".
# ---------------------------------------------------------------

from flask import Flask

app = Flask(__name__)


# Une "route" associe une adresse (URL) à une fonction Python.
# Ici : quand quelqu'un visite la page d'accueil "/",
# Flask exécute la fonction accueil() et renvoie son résultat au navigateur.
@app.get("/")
def accueil():
    return "Avec mon twin on est lié comme des siamois, Elle recherche mon mini moi,Il est mort depuis des mois"


# ---------------------------------------------------------------
#  Ajoutez vos nouvelles routes ci-dessous 👇
# ---------------------------------------------------------------
@app.get("/presentation")
def presentation():
    return """
    <h1>Léa Martin</h1>
    <pJe veux mon<strong>nom dans le Figaro, je suis avec une  #### à Reuilly-Diderot</strong>.</p>
    <h2>Ce que j'aime</h2>
    <ul>
        <li>Guap</li>
        <li>Money</li>
        <li>Bands</li>
    </ul>
    """

@app.get("/loisirs")
def loisirs():
    return "When i needed guap, I aint get not helping hands"



# ---------------------------------------------------------------
#  Ne pas modifier : utile seulement pour lancer le site
#  sur votre propre ordinateur (python flask_app.py)
# ---------------------------------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

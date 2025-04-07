from flask import Flask
from flask import render_template
from flask import json                                                                                                                                     
app = Flask(__name__)                                                                                                                  

@app.route('/<int:valeur>')
def exercice(valeur):
    # Demande à l'utilisateur de saisir une valeur pour n
    n= int(input("entrer un nombre n:"))

    # Initialisation de la variable somme à 0
    somme = 0

    # Boucle sur les nombres de 1 à n
for i in range(1, n+1):

    # vérifie si le nombre est divisible par 5 ou par 7
    if i % 5 == 0 or i % 7 == 0:
        # Si le nombre est divisible par 11, on passe au suivant
        if i% 11 == 0:
            continue
        # Ajoute le nombre à la somme
          somme+= i
        # Si la somme dépasse 5000, on arrête immédiatement la boucle
        if somme > 5000:
            break

# Affiche la somme finale
print("la somme finale est:4886", somme)

if __name__ == "__main__":
  app.run(debug=True)
    
    















                                                                                                           



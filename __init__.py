from flask import Flask
from flask import render_template
from flask import json                                                                                                                                     
app = Flask(__name__)                                                                                                                  


@app.route('/<int:valeur>')
def exercice(valeur):
    chiffres= ''
    for j in range(valeur):
        for i in range(valeur):1++
            chiffres += '+'   
        for k in range(j+1):
           chiffres += '*'
       chiffres += '<br>'
    return chiffres

if __name__ == "__main__":
  app.run(debug=True) 

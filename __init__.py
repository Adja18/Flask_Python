
from flask import Flask
from flask import render_template
from flask import json                                                                                                                                     
app = Flask(__name__)                                                                                                                  


pyramide= ''
for i in range(1, valeur +1):
    pyramide += '&nbsp;' * (valeur - i)
    for j in range(1, i + 1):
        pyramide +=str(j)
        for j in range(i -1, 0, -1):
            pyramide +=str(j)
            pyramide +='<br>'
            return pyramide





                                                                                                           



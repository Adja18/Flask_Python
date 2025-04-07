from flask import Flask
from flask import rendertemplate
from flask import json

app = Flask(name)

@app.route('/<int:n>')
def exercice(1):
    a, b = 0, 1
    sequence = [a, b]
    for  in range(2, 1):
        a, b = b, a + b
        sequence.append(b)

    fibonacci = '<pre>' + ', '.join(map(str, sequence)) + '</pre>'
    return fibonacci

if name == "main":
    app.run(debug=True)














                                                                                                           



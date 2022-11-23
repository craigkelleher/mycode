#!/usr/bin/python3
# An object of Flask class is our WSGI application
from flask import Flask

# Flask constructor takes the name of current
# module (__name__) as argument
app = Flask(__name__)

# route() function of the Flask class is a
# decorator, tells the application which URL
# should call the associated function

@app.route("/")
def hello_world():
    return "Hello World"


@app.route("/pikachu") #<-- decorator
def blue():
    return {"name": "Pikachu",
            "type": "electric",
            "generation": 1}

@app.route("/bulbasaur")
def red():
    return {"name": "Bulbasaur",
            "type": "grass/poison",
            "generation": 1}

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224)                                      

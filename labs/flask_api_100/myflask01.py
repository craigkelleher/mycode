#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)

@app.route("/craig")
def hello_world():
   return "Hello World"

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application
   # app.run(host="0.0.0.0", port=2224, debug=True) # DEBUG MODE


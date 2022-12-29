import os
from flask import request, jsonify, Flask
from flask_ngrok import run_with_ngrok

app = Flask(__name__)

run_with_ngrok(app) 

@app.route('/')
def helloWorld():
	name = os.environ.get("NAME","World")
	return "Hello {}! First App".format(name)

if __name__ == "__main__":
	 app.run()

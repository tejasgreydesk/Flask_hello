import os
from flask import request, jsonify, Flask

app = Flask(__name__)

@app.route('/')
def helloWorld():
	name = os.environ.get("NAME","World")
	return "Hello {}! First App".format(name)

if __name__ == "__main__":
	app.run(debug=True,host="0.0.0.0",port=int(os.environ.get("PORT",8080)))

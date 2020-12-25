from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello, Welcome World!'

@app.route('/say-name')
def hello_world():
	return 'Hello, Welcome ' + request.args.get('name')
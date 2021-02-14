from flask import Blueprint

api = Blueprint("API", __name__)

@api.route("/helloworld", methods=['POST'])
def helloworld():
	return "Hello, World!"
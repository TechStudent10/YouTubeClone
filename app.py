from flask import Flask, render_template
from api import api

app = Flask(__name__, template_folder="website\\templates", static_folder="website\\static")
app.register_blueprint(api, url_prefix="/api")

@app.route("/")
def index():
	return render_template("index.html")

if __name__ == '__main__':
	app.run(debug=True)
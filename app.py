from databases import *
from flask import Flask, render_template, url_for, request
app = Flask(__name__)

@app.route("/")
def challenge():
	return render_template("ch_page.html")

@app.route("/ch-list")
def challenge_list():
	return render_template("ch_lists.html")

if __name__ == '__main__':
	app.run(debug=True, port = 2000)
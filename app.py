from databases import *
from flask import Flask, render_template, url_for, request
app = Flask(__name__)

@app.route("/")
def challenge():
	return render_template("ch_page.html")

@app.route("/ch-list")
def challenge_list():
	return render_template("ch_lists.html")

@app.route("/ch-sub", methods=['GET','POST'])
def challenger_info():
	if request.method == 'GET':
		return render_template("ch_sub.html")
	else:
		name = request.form['fname']
		famname = request.form['lname']
		ch_num = request.form['ch-num']
		# vid = request.form['video']
		add_challenger(name, famname, ch_num)
		return render_template("ch_sub.html", last_ch = get_last())

print(query_all())

if __name__ == '__main__':
	app.run(debug=True, port = 2000)
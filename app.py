from databases import *
from flask import redirect, Flask, render_template, url_for, request
app = Flask(__name__)

@app.route("/")
def challenge():
	return render_template("ch_page.html")

@app.route("/ch-list")
def challenge_list():
	return render_template("ch_lists.html")

@app.route("/ch-sub-completed")
def approved_ch():
	return render_template("ch_sub.html", last_ch = get_last())

@app.route("/ch-sub", methods=['GET','POST'])
def challenger_info():
	if request.method == 'GET':
		return redirect("/")
	else:
		name = request.form['fname']
		famname = request.form['lname']
		ch_num = request.form['ch-num']
		# vid = request.form['video']
		add_challenger(name, famname, ch_num)
		return redirect("/ch-sub-completed")


delete_all()

print(query_all())

if __name__ == '__main__':
	app.run(debug=True, port = 2000)
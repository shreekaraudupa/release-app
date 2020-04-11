from flask import Flask, render_template, request

app = Flask(__name__)

user_cred = {}


@app.route("/")
def home():
    return render_template("login-details.html")


@app.route("/main", methods=["POST"])
def mainPage():
    sid = request.form['sid']
    sso = request.form['sso']
    user_cred['sid'] = sid
    user_cred['sso'] = sso
    return render_template("main-page.html", sid=sid)


@app.route("/branch_cut")
def branch_cut():
    #print(user_cred)
    return render_template("branch-cut.html")


if __name__ == "__main__":
    app.run(debug=True, port=8000)

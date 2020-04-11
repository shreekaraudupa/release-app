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
    return render_template("main-page.html", sid=user_cred['sid'])


@app.route("/branch_cut")
def branch_cut():
    # user_cred dictionary will have the sid and sso
    return render_template("branch-cut.html", sid=user_cred.get('sid'))

@app.route("/release_notes")
def release_notes():
    # user_cred dictionary will have the sid and sso
    return render_template("release-notes.html", sid=user_cred.get('sid'))

@app.route("/post_release")
def post_release():
    # user_cred dictionary will have the sid and sso
    return render_template("post-release.html", sid=user_cred.get('sid'))

if __name__ =="__main__":
    app.run(debug=True, port=8000)

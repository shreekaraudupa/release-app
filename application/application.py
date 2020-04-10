from flask import Flask , render_template

app = Flask(__name__)


@app.route("/")
def mainPage():
    return render_template("main-page.html")

@app.route("/branch_cut")
def branch_cut():
    return render_template("branch-cut.html")

if __name__ == "__main__":
    app.run(debug=True,port=8000)

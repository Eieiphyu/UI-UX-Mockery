from flask import Flask,render_template

app = Flask(__name__)
@app.route("/eg")
def eg():
    return render_template("eg_gmail.html")

@app.route("/")
def home():
    return render_template("index1.html")


@app.route("/egvidmate")
def egvidmate():
    return render_template("examplevidmate.html")


if __name__=="__main__":
    app.run(debug=True)

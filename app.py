from flask import Flask, render_template, flash, request

app = Flask(__name__)
app.secret_key = "C2Hk9K4hL4G7z3J6tN2Q8s5J8M3a9R"

@app.route("/hello")
def index():
    flash("Adını öğrenebilirmiyim?")
    return render_template("index.html")

@app.route("/greet", methods=["POST","GET"])
def greet():
    flash("Selam  " + str(request.form["name_input"]) + ", Nedir derdin?")
    return render_template("index.html")

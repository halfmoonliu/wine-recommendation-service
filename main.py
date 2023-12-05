from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        feeling = request.form["feeling"]
        return redirect(url_for("feeling", feel = feeling))
    else:
        return render_template("home.html")

@app.route("/<feel>")
def feeling(feel):
    return f"<h1>{feel}</h1>"

if __name__ == "__main__":
    app.run(debug=True)
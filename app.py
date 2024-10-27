import os
from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap5


app = Flask(__name__)
app.config["SECRET_KEY"] = os.urandom(24)
Bootstrap5(app)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

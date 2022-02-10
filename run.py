#! /usr/bin/env python
from flask import Flask, render_template
import glob

app = Flask(__name__)

app.config["TEAMPLATES_AUTO_RELOAD"] = True


@app.route("/")
def home():
    images = list(glob.glob("static/imgs/*.png"))
    images = list(map(lambda x: x[7:], images))
    return render_template("index.html", images=images)


if __name__ == "__main__":
    app.run()

#! /usr/bin/env python
from flask import Flask, render_template
import glob

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/")
def home():
    images = {}
    # types = list(glob.glob("static/imgs/*"))
    types = ["arms", "bg"]
    for t in types:
        tmp = list(glob.glob(f"static/imgs/{t}/*.png"))
        tmp = list(map(lambda x: x[7:], tmp))
        images[t] = tmp
    return render_template("index.html", images=images)

@app.route("/collection")
def collection():
    images = list(glob.glob("static/collection/*.png"))
    images = list(map(lambda x: x[7:], images))
    return render_template("collection.html", images=images)



if __name__ == "__main__":
    app.run()

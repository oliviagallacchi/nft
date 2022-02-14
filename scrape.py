#! /usr/bin/env python

from bs4 import BeautifulSoup
import requests
from PIL import Image
from random import choice
from io import BytesIO
from datetime import datetime
from hashlib import md5


def pick_url(img_list, url):
    img = choice(img_list)
    return f"{url}{img['src']}"


def get_bg_image(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "html.parser")
    bgs = soup.select(".bg img")
    r = requests.get(pick_url(bgs, url))
    return Image.open(BytesIO(r.content))


def assemble_image():
    # Get the background image. All the parts will be added onto this image.
    bg = get_bg_image("http://localhost:5000")

    # Store all the parts for assembling later
    collection = []

    # A list with all the servers we want to get parts from, and which parts we
    # want.
    li = [
        {
            "url": "http://localhost:5000",
            "parts": [
                ".arms",
                ".shoes",
                ".faces",
                ".hats",
            ]
        }
    ]

    # Iterate over the servers to collect all the parts. Append them to the
    # collection
    for server in li:
        res = requests.get(server["url"])
        soup = BeautifulSoup(res.content, "html.parser")
        for t in server["parts"]:
            tmp = soup.select(f"{t} img")
            collection.append(pick_url(tmp, server["url"]))

    # Iterate over the collection to assemble the image
    for url in collection:
        r = requests.get(url)
        tmp = Image.open(BytesIO(r.content))
        bg.paste(tmp, (0,0), tmp)

    # Create a filename that does not yet exist and save the image.
    filename = md5(str(datetime.timestamp(datetime.now())).encode()).hexdigest()
    bg.save(f"static/collection/{filename}.png", "PNG")

if __name__ == "__main__":
    assemble_image()

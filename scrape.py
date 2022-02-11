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


url = "http://localhost:5000"

res = requests.get(url)

soup = BeautifulSoup(res.content, "html.parser")

bgs = soup.select(".bg img")
r = requests.get(pick_url(bgs, url))
bg = Image.open(BytesIO(r.content))

collection = []

arms = soup.select(".arms img")
collection.append(pick_url(arms, url))

for url in collection:
    r = requests.get(url)
    tmp = Image.open(BytesIO(r.content))
    bg.paste(tmp, (0,0), tmp)

filename = md5(str(datetime.timestamp(datetime.now())).encode()).hexdigest()
bg.save(f"static/collection/{filename}.png", "PNG")

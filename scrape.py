#! /usr/bin/env python

from bs4 import BeautifulSoup
import requests
from PIL import Image
from random import choice
from io import BytesIO



url = "http://localhost:5000"

res = requests.get(url)

soup = BeautifulSoup(res.content, "html.parser")

imgs = soup.find_all("img")

for img in imgs:
    r = requests.get(f"{url}{img['src']}")
    im = Image.open(BytesIO(r.content))
    im.save("/tmp/out.png", "PNG")

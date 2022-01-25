#!/usr/bin/env python
from PIL import Image
from random import choice


def main():
    arms = [Image.open("imgs/arms_01.png"), Image.open("imgs/arms_02.png")]
    bg = Image.open("imgs/bg.png")


    arm = choice(arms)
    bg.paste(arm, (0,0), arm)
    bg.save("out.png", "PNG")


if __name__ == "__main__":
    main()

import os

blank = [int(i.split(".")[0].strip()) for i in open("/home/gauravs/github/skema/skema/img2mml/logs/blank_images.lst").readlines()]

nl = open("new_latex.lst", "w")
l = open("latex.lst").readlines()

for idx,i in enumerate(l):
    if idx not in blank:
        nl.write(i)

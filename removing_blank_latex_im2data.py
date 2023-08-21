import os

base_path = "/home/skema/img2mml/gauravs_data_for_paper/data/"
blank = [int(i.split(".")[0].strip()) for i in open(f"{base_path}/opennmt/our_blank_images.txt").readlines()]

nl = open("new_latex.lst", "w")
l = open("latex.lst").readlines()

for idx,i in enumerate(l):
    if idx not in blank:
        nl.write(i)

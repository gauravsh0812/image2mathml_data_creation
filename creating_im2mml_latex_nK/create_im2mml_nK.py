# CONVERT LaTeX EQUATION TO MathML CODE USING MathJax
import requests
import subprocess, os
import json
from simplify_basic import simp_basic
from simplify_advance import simp_adv
from datetime import datetime


# Printing starting time
print(" ")
start_time = datetime.now()
print("Starting at:  ", start_time)


def CleaningMML(res):
    # Removing "\ and /" at the begining and at the en
    res = res[res.find("<"):]
    res = res[::-1][res[::-1].find(">"):]
    res = res[::-1]

    # Removing "\\n"
    res = res.replace(">\\n", ">")
    return(res)

def MjxMML(eqn):

    #global lock

    # Define the webservice address
    webservice = "http://localhost:8081"

    # Translate and save each LaTeX string using the NodeJS service for MathJax
    res = requests.post(
            f"{webservice}/tex2mml",
            headers={"Content-type": "application/json"},
            json={"tex_src": json.dumps(eqn)},
             )

    # Cleaning and Dumping the MathML strings to JSON file
    MML = CleaningMML(res.text)
    return MML


def main():

    formulas = open("img2mml_datasets/raw_datasets/im2latex-103K/formulas.norm.lst").readlines()
    train = open("img2mml_datasets/raw_datasets/im2latex-103K/train.lst").readlines()
    test = open("img2mml_datasets/raw_datasets/im2latex-103K/test.lst").readlines()
    val = open("img2mml_datasets/raw_datasets/im2latex-103K/validate.lst").readlines()

    formulas_mml = open("img2mml_datasets/opennmt_datasets/im2mml-100K/mml.lst", "w")

    count, rejected = 0,0
    for fidx, f in enumerate([train, test, val]):
        arr = ["train", "test", "validate"]
        f_mml = open(f"img2mml_datasets/opennmt_datasets/im2mml-100K/{arr[fidx]}.lst", "w")
        print(f"working on {arr[fidx]}")

        for i, v in enumerate(f):
            if i%10000 == 0: print(i)

            idx, img, _ = v.split()

            latex = formulas[int(idx)]

            mml = MjxMML(latex)

            if len(mml) > 3:
                mml = simp_basic(mml)
                mml = simp_adv(mml)

                formulas_mml.write(mml + "\n")
                f_mml.write(f"{count} {img} basic" + "\n")
                count += 1
            else:
                rejected += 1

    print("total rejected equations: ", rejected)
    print("total rendered equations: ", count)

if __name__ == "__main__":
    main()

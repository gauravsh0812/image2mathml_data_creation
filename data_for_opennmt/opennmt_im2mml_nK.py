# CONVERT LaTeX EQUATION TO MathML CODE USING MathJax
import requests
import subprocess, os
import time, re
import json
from simplify import simplification
from datetime import datetime
import multiprocessing
from multiprocessing import Pool, Lock, TimeoutError, Event


# Printing starting time
print(" ")
start_time = datetime.now()
print("Starting at:  ", start_time)

pause_event = Event()  # suspend and resume processing
equation_counter = multiprocessing.Value("i", 0)
time.sleep(3)

def CleaningMML(res):
    # Removing "\ and /" at the begining and at the end
    res = res[res.find("<"):]
    res = res[::-1][res[::-1].find(">"):]
    res = res[::-1]

    # Removing "\\n"
    res = res.replace(">\\n", ">")
    return(res)

def correct_phi(string):
    pattern = r"(<mi>&#x03C6;<!-- φ --></mi> <mi>&#x03C6;<!-- φ --></mi> <mtext>&#xA0;</mtext> <mi mathvariant=\"normal\">&#x0393;<!-- Γ --></mi> <mo stretchy=\"false\">[</mo> <mi>f</mi> <mo stretchy=\"false\">(</mo> <mi>t</mi> <mo stretchy=\"false\">)</mo> <mi>cos</mi> <mo>&#x2061;<!-- ⁡ --></mo> <mi>&#x03C6;<!-- φ --></mi> )(.+?)( <mo stretchy=\"false\">]</mo>)"
    replacement_dict = {
        "\\": "place_holder1",
        "[": "place_holder2",
        "]": "place_holder3",
        ">(<": "place_holder4",
        ">)<": "place_holder5",
    }
    for key, val in replacement_dict.items():
        pattern = pattern.replace(key, val)
        string = string.replace(key, val)

    matches = re.findall(pattern, string)
    for match in matches:
        placeholder = match[1]
        string = string.replace(
            "".join(match), f"{placeholder} <mi>&#x0278;<!-- ɸ --></mi>"
        )

    for key, val in replacement_dict.items():
        string = string.replace(val, key)
    return string


def restart_mathjax_server():
    response = requests.get("http://localhost:8081/restart")


def MjxMML(eqn):

    global pause_event

    # Define the webservice address
    webservice = "http://localhost:8081"
    # Load the LaTeX string data
    # Translate and save each LaTeX string using the NodeJS service for MathJax
    res = requests.post(
        f"{webservice}/tex2mml",
        headers={"Content-type": "application/json"},
        json={"tex_src": json.dumps(eqn)},
    )
    if not "FAILED" in res.content.decode("utf-8"):
        # Cleaning and Dumping the MathML strings to JSON file
        MML = CleaningMML(res.text)
        # Replacing the wrong generation from MathJax
        mml = re.sub("\s+", " ", mml)
        mml = mml.replace(
            r"<msub> <mi>&#x2113;<!-- ℓ --></mi> <mn>1</mn> </msub> <mo>,</mo> <msub> <mi>&#x2113;<!-- ℓ --></mi> <mn>2</mn> </msub>",
            "",
        )
        mml = mml.replace(
            r"<mi>&#x03C6;<!-- φ --></mi> <mi>&#x03C6;<!-- φ --></mi> <mtext>&#xA0;</mtext> <mi mathvariant=\"normal\">&#x0393;<!-- Γ --></mi> <mo stretchy=\"false\">[</mo> <mi>f</mi> <mo stretchy=\"false\">(</mo> <mi>t</mi> <mo stretchy=\"false\">)</mo> <mi>cos</mi> <mo>&#x2061;<!-- ⁡ --></mo> <mi>&#x03C6;<!-- φ --></mi> <mo stretchy=\"false\">]</mo>",
            r"<mi>&#x0278;<!-- ɸ --></mi>",
        )
        mml = correct_phi(mml)

        # To avoid the buffer issue from MathJax, restart the service once processing 1000 equations
        if equation_counter.value % 1000 == 0:
            pause_event.clear()
            restart_mathjax_server()
            time.sleep(3)
            pause_event.set()
            equation_counter.value = 0
        else:
            pause_event.set()

        lock.release()
        pause_event.wait()

        return MML
    else:
        return None

def latex2mml():

    formulas = open("data/im2latex-103K/formulas.norm.lst").readlines()
    train = open("data/im2latex-103K/train.lst").readlines()
    test = open("data/im2latex-103K/test.lst").readlines()
    val = open("data/im2latex-103K/validate.lst").readlines()

    org_mml = open("data/opennmt/im2mml-100K/original_mml.lst", "w")
    simp_mml = open("data/opennmt/im2mml-100K/mml.lst", "w")

    count, rejected = 0,0
    for fidx, f in enumerate([train, test, val]):
        arr = ["train", "test", "validate"]
        f_mml = open(f"data/opennmt/im2mml-100K/{arr[fidx]}.lst", "w")
        f_mml_src = open(f"data/opennmt/im2mml-100K/src-{arr[fidx]}.lst", "w")
        f_mml_tgt = open(f"data/opennmt/im2mml-100K/tgt-{arr[fidx]}.lst", "w")

        print(f"working on {arr[fidx]}")

        for i, v in enumerate(f):
            if i%10000 == 0: print(i)

            idx, img, _ = v.split()

            latex = formulas[int(idx)]

            mml = MjxMML(latex)

            if mml != None:
                org_mml.write(mml + "\n")

                mml = simplification(mml)

                simp_mml.write(mml + "\n")
                f_mml.write(f"{count} {img} basic" + "\n")
                f_mml_src.write(f"{img}\n")
                f_mml_tgt.write(f"{mml}\n")
                count += 1

            else:
                rejected += 1

        f_mml.close()

    org_mml.close()
    simp_mml.close()
    print("total rejected equations: ", rejected)
    print("total rendered equations: ", count)

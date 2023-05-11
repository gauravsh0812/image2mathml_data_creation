# CONVERT LaTeX EQUATION TO MathML CODE USING MathJax
import requests
import subprocess, os
import time, re
import json
# from simplify import simplification
from datetime import datetime
import multiprocessing as mp
from threading import Timer
from multiprocessing import Pool, Lock, TimeoutError, Event


# Printing starting time
print(" ")
start_time = datetime.now()
print("Starting at:  ", start_time)

pause_event = Event()  # suspend and resume processing
equation_counter = mp.Value("i", 0)
time.sleep(3)

# Function to kill process if TimeoutError occurs
kill = lambda process: process.kill()


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

    # global pause_event

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
        mml = CleaningMML(res.text)
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
        equation_counter.value += 1
        # To avoid the buffer issue from MathJax, restart the service once processing 1000 equations
        if equation_counter.value % 1000 == 0:
            pause_event.clear()
            restart_mathjax_server()
            time.sleep(3)
            pause_event.set()
            equation_counter.value = 0
        else:
            pause_event.set()

        pause_event.wait()

        return mml
    else:
        return None

def latex2mml():

    formulas = open("/home/skema/img2mml/gauravs_data_for_paper/data/im2latex-103K/formulas.norm.lst").readlines()
    train = open("/home/skema/img2mml/gauravs_data_for_paper/data/im2latex-103K/train.lst").readlines()
    test = open("/home/skema/img2mml/gauravs_data_for_paper/data/im2latex-103K/test.lst").readlines()
    val = open("/home/skema/img2mml/gauravs_data_for_paper/data/im2latex-103K/validate.lst").readlines()

    if not os.path.exists("/home/skema/img2mml/gauravs_data_for_paper/data/opennmt"):
        os.mkdir("/home/skema/img2mml/gauravs_data_for_paper/data/opennmt")
    if not os.path.exists("/home/skema/img2mml/gauravs_data_for_paper/data/opennmt/im2mml-100K"):
        os.mkdir("/home/skema/img2mml/gauravs_data_for_paper/data/opennmt/im2mml-100K")

    org_mml = open("/home/skema/img2mml/gauravs_data_for_paper/data/opennmt/im2mml-100K/original_mml.lst", "w")
    simp_mml = open("/home/skema/img2mml/gauravs_data_for_paper/data/opennmt/im2mml-100K/mml.lst", "w")

    count, rejected = 0,0
    for fidx, f in enumerate([train, test, val]):
        arr = ["train", "test", "validate"]
        f_mml = open(f"/home/skema/img2mml/gauravs_data_for_paper/data/opennmt/im2mml-100K/{arr[fidx]}.lst", "w")
        f_mml_src = open(f"/home/skema/img2mml/gauravs_data_for_paper/data/opennmt/im2mml-100K/src-{arr[fidx]}.lst", "w")
        f_mml_tgt = open(f"/home/skema/img2mml/gauravs_data_for_paper/data/opennmt/im2mml-100K/tgt-{arr[fidx]}.lst", "w")

        print(f"working on {arr[fidx]}")

        for i, v in enumerate(f):
            if i%100 == 0: print(i)

            idx, img, _ = v.split()

            latex = formulas[int(idx)]

            mml = MjxMML(latex)
            if mml != None:
                open("mml_org.txt", "w").write(mml)
                cmd = ["python", f"{os.getcwd()}/simplify.py"]
                output = subprocess.Popen(
                    cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE
                )
                my_timer = Timer(5, kill, [output])

                try:
                    my_timer.start()
                    stdout, stderr = output.communicate()
                    org_mml.write(mml + "\n")
                    smml = open("mml_mod.txt").readlines()[0].strip()
                    simp_mml.write(smml + "\n")
                    f_mml.write(f"{count} {img} basic" + "\n")
                    f_mml_src.write(f"{img}\n")
                    f_mml_tgt.write(f"{smml}\n")
                    count += 1

                except:
                    rejected += 1

                finally:
                    my_timer.cancel()


        f_mml.close()

    org_mml.close()
    simp_mml.close()
    print("total rejected equations: ", rejected)
    print("total rendered equations: ", count)

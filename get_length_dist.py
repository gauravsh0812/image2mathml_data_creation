import json, os, sys

data_type = sys.argv[-1]

def get_distribution_opennmt():
    im2latex_103K = open("/home/skema/img2mml/gauravs_data_for_paper/data/im2latex-103K/formulas.norm.lst").readlines()
    im2latex_100K = open("/home/skema/img2mml/gauravs_data_for_paper/data/opennmt/im2latex-100K/latex.lst").readlines()
    im2mml_100K = open("/home/skema/img2mml/gauravs_data_for_paper/data/opennmt/im2mml-100K/mml.lst").readlines()

    p = "/home/skema/img2mml/gauravs_data_for_paper/data/opennmt/im2data_distributions"
    if not os.path.exists(p):
        os.mkdir(p)

    im2latex_103K_dict = dict()
    im2latex_100K_dict = dict()
    im2mml_100K_dict = dict()

    for i,v in enumerate([im2latex_103K, im2latex_100K, im2mml_100K]):
        if i == 0: d = im2latex_103K_dict
        elif i == 1: d = im2latex_100K_dict
        else: d = im2mml_100K_dict

        # initialize dict
        for r in range(0,350, 50):
            begin = r
            end = r+50
            d[f"{begin}-{end}"] = 0
        d["350+"] = 0

        keys = d.keys()

        for l in v:

            length = len(l.split())
            flag350 = False

            # finding which bin it belongs to
            for k in keys:
                if k != "350+":
                    begin, end = k.split("-")
                    if (length > int(begin)) and (length <= int(end)):
                        d[k] += 1
                        flag350 = True

                else:
                    if not flag350:
                        d["350+"] += 1

        # save the distribution
        if i==0: json.dump(d, open("/home/skema/img2mml/gauravs_data_for_paper/data/opennmt/im2data_distributions/im2latex-103K-length-dist.json", "w"))
        elif i==1: json.dump(d, open("/home/skema/img2mml/gauravs_data_for_paper/data/opennmt/im2data_distributions/im2latex-100K-length-dist.json", "w"))
        else: json.dump(d, open("/home/skema/img2mml/gauravs_data_for_paper/data/opennmt/im2data_distributions/im2mml-100K-length-dist.json", "w"))


def get_distribution_odata():
    olatex_100K = open("/home/skema/img2mml/gauravs_data_for_paper/data/opennmt/olatex-100K/latex.lst").readlines()
    omml_100K = open("/home/skema/img2mml/gauravs_data_for_paper/data/opennmt/omml-100K/mml.lst").readlines()

    p = "/home/skema/img2mml/gauravs_data_for_paper/data/opennmt/im2data_distributions"
    if not os.path.exists(p):
        os.mkdir(p)

    olatex_100K_dict = dict()
    omml_100K_dict = dict()

    for i,v in enumerate([olatex_100K, omml_100K]):
        if i == 0: d = olatex_100K_dict
        else: d = omml_100K_dict

        # initialize dict
        for r in range(0,350, 50):
            begin = r
            end = r+50
            d[f"{begin}-{end}"] = 0
        d["350+"] = 0

        keys = d.keys()

        for l in v:

            length = len(l.split())
            flag350 = False

            # finding which bin it belongs to
            for k in keys:
                if k != "350+":
                    begin, end = k.split("-")
                    if (length > int(begin)) and (length <= int(end)):
                        d[k] += 1
                        flag350 = True

                else:
                    if not flag350:
                        d["350+"] += 1

        # save the distribution
        if i==0: json.dump(d, open("/home/skema/img2mml/gauravs_data_for_paper/data/opennmt/im2data_distributions/olatex-100K-length-dist.json", "w"))
        else: json.dump(d, open("/home/skema/img2mml/gauravs_data_for_paper/data/opennmt/im2data_distributions/omml-100K-length-dist.json", "w"))


if data_type == "opennmt":
    get_distribution_opennmt()
elif data_type == "odata":
    get_distribution_odata()

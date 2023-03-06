import json

im2latex_103K = open("/home/gauravs/data/img2mml_datasets/raw_datasets/im2latex-103K/formulas.norm.lst").readlines()
im2latex_100K = open("/home/gauravs/data/img2mml_datasets/opennmt_datasets/im2latex-100K/latex.lst").readlines()
im2mml_100K = open("/home/gauravs/data/img2mml_datasets/opennmt_datasets/im2mml-100K/mml.lst").readlines()

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

        # finding which bin it belongs to
        for k in keys:
            if k != "350+":
                begin, end = k.split("-")
                if (length > int(begin)) and (length <= int(end)):
                    d[k] += 1
                    break 
            else:
                d["350+"] += 1
    
    # save the distribution
    if i==0: json.dump(d, open("/home/gauravs/data/img2mml_datasets/opennmt_datasets/distributions/im2latex-103K-length-dist.json", "w"))
    elif i==1: json.dump(d, open("/home/gauravs/data/img2mml_datasets/opennmt_datasets/distributions/im2latex-100K-length-dist.json", "w"))
    else: json.dump(d, open("/home/gauravs/data/img2mml_datasets/opennmt_datasets/distributions/im2mml-100K-length-dist.json", "w"))

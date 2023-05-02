import os

def im2mml_2_im2latex():
    latex_formulas_original = open("data/im2latex-103K/formulas.norm.lst").readlines()
    latex_formulas_nK = open(f"data/opennmt/im2latex-100K/latex.lst", "w")

    if not os.path.exists("data/opennmt/im2latex-100K"):
        os.mkdir("data/opennmt/im2latex-100K")

    # creating the dictionary for the index:image_name for original im2latex
    idx_img = dict()
    for t in ["train", "test", "validate"]:
        t_im2latex_org = open(f"data/im2latex-103K/{t}.lst").readlines()
        for i in t_im2latex_org:
            idx, img, _ = i.split()
            idx_img[img] = idx

    count = 0
    for t in ["train", "test", "validate"]:
        print(t)
        t_im2mml = open(f"data/opennmt/im2mml-100K/{t}.lst").readlines()
        t_im2latex_org = open(f"data/im2latex-103K/{t}.lst").readlines()

        # combined file
        t_im2latex = open(f"data/opennmt/im2latex-100K/{t}.lst", "w")

        # src  and tgt file
        t_im2latex_src = open(f"data/opennmt/im2latex-100K/src-{t}.lst", "w")
        t_im2latex_tgt = open(f"data/opennmt/im2latex-100K/tgt-{t}.lst", "w")

        for i,v in enumerate(t_im2mml):
            if i%1000 == 0: print(i)
            _, img, _ = v.split()
            latex_index = int(idx_img[img])
            latex_eqn = latex_formulas_original[latex_index]
            latex_formulas_nK.write(latex_eqn)
            t_im2latex.write(f"{count} {img} basic \n")
            t_im2latex_src.write(f"{img}.png \n")
            t_im2latex_tgt.write(f"{latex_eqn}")
            count+=1

    t_im2latex.close()

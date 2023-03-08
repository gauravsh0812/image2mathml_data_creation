
def im2mml_2_im2latex():
    latex_formulas_original = open("img2mml_datasets/raw_datasets/im2latex-103K/formulas.norm.lst").readlines()
    latex_formulas_nK = open(f"img2mml_datasets/opennmt_datasets/im2latex-100K/latex.lst", "w")

    # creating the dictionary for the index:image_name for original im2latex
    idx_img = dict()
    for t in ["train", "test", "validate"]:
        t_im2latex_org = open(f"img2mml_datasets/raw_datasets/im2latex-103K/{t}.lst").readlines()
        for i in t_im2latex_org:
            idx, img, _ = i.split()
            idx_img[img] = idx

    count = 0
    for t in ["train", "test", "validate"]:
        print(t)
        t_im2mml = open(f"img2mml_datasets/opennmt_datasets/im2mml-100K/{t}.lst").readlines()
        t_im2latex_org = open(f"img2mml_datasets/raw_datasets/im2latex-103K/{t}.lst").readlines()
        t_im2latex = open(f"img2mml_datasets/opennmt_datasets/im2latex-100K/{t}.lst", "w")

        for i,v in enumerate(t_im2mml):
            if i%10000 == 0: print(i)
            _, img, _ = v.split()
            latex_index = int(idx_img[img])
            latex_eqn = latex_formulas_original[latex_index]
            latex_formulas_nK.write(latex_eqn)
            t_im2latex.write(f"{count} {img} basic \n")
            count+=1

    t_im2latex.close()

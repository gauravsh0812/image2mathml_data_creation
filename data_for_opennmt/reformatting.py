import os
import shutil

def reformat():
    # ------------------------------------
    # reformatting for opennmt olatex
    # ------------------------------------
    src = "/home/skema/img2mml/gauravs_data_for_paper/data/odata/our_sampled_data"
    dst = "/home/skema/img2mml/gauravs_data_for_paper/data/opennmt/olatex-100K"
    shutil.copyfile(src+"/no_blank_original_latex.lst", dst+"/original_latex.lst")
    shutil.copyfile(src+"/latex.lst", dst+"/latex.lst")

    os.chdir(dst)
    test = open("test.lst", "w")
    train = open("train.lst", "w")
    val = open("validate.lst", "w")
    src_test, tgt_test = open("src-test.lst", "w"), open("tgt-test.lst", "w")
    src_train, tgt_train = open("src-train.lst", "w"), open("tgt-train.lst", "w")
    src_val, tgt_val = open("src-validate.lst", "w"), open("tgt-validate.lst", "w")

    latex = open('latex.lst').readlines()

    n = len(latex)
    n1 = int(0.8*n)
    n2 = int(0.9*n)

    for i in range(0,n1):
        train.write(f"{i} {i} basic\n")
        src_train.write(str(i)+".png\n")
        tgt_train.write(latex[i])

    for i in range(n1, n2):
        test.write(f"{i} {i} basic\n")
        src_test.write(str(i)+".png\n")
        tgt_test.write(latex[i])

    for i in range(n2, n):
        val.write(f"{i} {i} basic\n")
        src_val.write(str(i)+".png\n")
        tgt_val.write(latex[i])

    print("reformatting for opennmt olatex done!...")

    # ------------------------------------
    # reformatting for opennmt omml
    # ------------------------------------
    src = "/home/skema/img2mml/gauravs_data_for_paper/data/odata/our_sampled_data"
    dst = "/home/skema/img2mml/gauravs_data_for_paper/data/opennmt/omml-100K"
    shutil.copyfile(src+"/original_mml.lst", dst+"/original_mml.lst")
    shutil.copyfile(src+"/mml.lst", dst+"/mml.lst")

    os.chdir(dst)
    test = open("test.lst", "w")
    train = open("train.lst", "w")
    val = open("validate.lst", "w")
    src_test, tgt_test = open("src-test.lst", "w"), open("tgt-test.lst", "w")
    src_train, tgt_train = open("src-train.lst", "w"), open("tgt-train.lst", "w")
    src_val, tgt_val = open("src-validate.lst", "w"), open("tgt-validate.lst", "w")

    mml = open('mml.lst').readlines()

    assert len(latex) == len(mml)

    n = len(mml)
    n1 = int(0.8*n)
    n2 = int(0.9*n)

    for i in range(0,n1):
        train.write(f"{i} {i} basic\n")
        src_train.write(str(i)+".png\n")
        tgt_train.write(mml[i])

    for i in range(n1, n2):
        test.write(f"{i} {i} basic\n")
        src_test.write(str(i)+".png\n")
        tgt_test.write(mml[i])

    for i in range(n2, n):
        val.write(f"{i} {i} basic\n")
        src_val.write(str(i)+".png\n")
        tgt_val.write(mml[i])

    print("reformatting for opennmt omml done!...")

    # ------------------------------------
    # reformatting for odata im2data
    # ------------------------------------
    src = "/home/skema/img2mml/gauravs_data_for_paper/data/opennmt/"
    dst = "/home/skema/img2mml/gauravs_data_for_paper/data/odata/im2data"
    dst_mml, dst_latex = open(dst+"/mml.lst", "w"), open(dst+"/latex.lst", "w")

    if not os.path.exists(dst+"/images"):
        os.mkdir(dst+"/images")

    count = 0
    for tt in ["train, test, validate"]:
        for s,t in zip(open(src+f"/im2mml-100K/src-{tt}.lst").readlines(),
                        open(src+f"/im2mml-100K/tgt-{tt}.lst").readlines()):

            dst_mml.write(t)
            shutil.copyfile(src+"/images_processed/"+s, dst+"/images/"+count+".png")
            count+=1

    print("reformatting for odata im2data done!...")

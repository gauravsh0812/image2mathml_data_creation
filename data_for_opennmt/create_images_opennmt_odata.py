import os
import shutil

def no_blank_data():
    images = "/home/skema/img2mml/gauravs_data_for_paper/data/odata/our_sampled_data/images"
    new_images = "/home/skema/img2mml/gauravs_data_for_paper/data/opennmt/oimages"
    blank = open("/home/skema/img2mml/gauravs_data_for_paper/data/opennmt/our_blank_images.txt").readlines()
    # 
    # count = 0
    # for i in range(len(os.listdir(images))):
    #     if str(i)+".png" not in blank:
    #         if i % 1000 ==0: print(i)
    #         src = os.path.join(images, str(i)+".png")
    #         dst = os.path.join(new_images, str(count)+".png")
    #         shutil.copyfile(src, dst)

    # -------------------------------------------------------------------------------
    # redefining original-latex file by eliminating latex correspoding to blank file.
    # -------------------------------------------------------------------------------

    org_latex = open("/home/skema/img2mml/gauravs_data_for_paper/data/odata/our_sampled_data/original_latex.lst").readlines()
    new_latex = open("/home/skema/img2mml/gauravs_data_for_paper/data/odata/our_sampled_data/no_blank_original_latex.lst", "w")

    for i in range(len(org_latex)):
        if str(i)+".png" not in blank:
            new_latex.write(org_latex[i])

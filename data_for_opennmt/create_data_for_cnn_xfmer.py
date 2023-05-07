from shutil import copyfile as CP
import os


# create im2mml-100K/im2latex-100K
# we only need to copy images from images_processed folder to
# new image folder with name representing index of mml/latex.lst
def create_data():
    i_path = "/home/skema/img2mml/gauravs_data_for_paper/data/im2mml-100K/images_for_cnn_xfmer"
    if not os.path.exists(i_path):
        os.mkdir(i_path)

    arr_files = ["train", "test", "validate"]
    for af in arr_files:
        print(af)
        f = open(f"/home/skema/img2mml/gauravs_data_for_paper/data/im2mml-100K/{af}.lst").readlines()
        for i in f:
            idx, img, _ = i.split()
            if int(idx)%10000==0: print(idx)
            src = f"/home/skema/img2mml/gauravs_data_for_paper/data/im2mml-100K/images_processed/{img}.png"
            dst = f"/home/skema/img2mml/gauravs_data_for_paper/data/images_for_cnn_xfmer/{idx}.png"
            CP(src, dst)

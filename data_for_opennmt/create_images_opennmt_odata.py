import os
import shutil.copyfile as CP

images = "/home/skema/img2mml/gauravs_data_for_paper/data/odata/our_sampled_data/images"
new_images = "/home/skema/img2mml/gauravs_data_for_paper/data/opennmt/oimages"
blank = open("/home/skema/img2mml/gauravs_data_for_paper/data/opennmt/our_blank_images.txt").readlines()

count = 0
for i in range(len(os.listdir(images))):
    if i+".png" not in blank:
        src = os.path.join(images, i+".png")
        dst = os.path.join(new_images, count+".png")
        CP(src, dst)

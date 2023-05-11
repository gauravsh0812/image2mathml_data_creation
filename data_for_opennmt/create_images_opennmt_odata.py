import os
import shutil.copyfile as CP

images = "/Users/gaurav/Desktop/research/DONT_DELETE_training_data/new/our_sampled_data/images"
new_images = "/Users/gaurav/Desktop/research/DONT_DELETE_training_data/new/opennmt/oimages"
blank = open("/Users/gaurav/Desktop/research/DONT_DELETE_training_data/new/opennmt/odata_blank_images.txt").readlines()

count = 0
for i in range(len(os.listdir(images))):
    if i+".png" not in blank:
        src = os.path.join(images, i+".png")
        dst = os.path.join(new_images, count+".png")
        CP(src, dst)

import json
from simplify_basic import simp_basic as sb
from simplify_advance import simp_adv as sd
from shutil import copyfile 

im2mml_dist = json.load(open("/home/gauravs/data/img2mml_datasets/opennmt_datasets/distributions/im2mml-100K-length-dist.json"))

raw_mml = open("/home/gauravs/data/img2mml_datasets/raw_datasets/our_data_500K/mml-500k.txt").readlines()
raw_latex = open("/home/gauravs/data/img2mml_datasets/raw_datasets/our_data_500K/latex-500k.txt").readlines()
raw_images = "/home/gauravs/data/img2mml_datasets/raw_datasets/our_data_500K/images-500k"

#new_mml = open("/home/gauravs/data/img2mml_datasets/raw_datasets/our_data_100K/mml-100K.txt", "w")
#new_latex = open("/home/gauravs/data/img2mml_datasets/raw_datasets/our_data_100K/latex-100K.txt", "w")
#new_images = "/home/gauravs/data/img2mml_datasets/raw_datasets/our_data_100K/images-100K"

# create dict to track the mmls, latexs, and imgs
index_dict = dict()
for id in im2mml_dist.keys():
    index_dict[id] = list()

overall_count = 0
for i,v in im2mml_dist.items():
    
    print(i, v)
    count = 0
    begin, end = i.split("-")
    n=0
    if int(begin) > 250:
        while count <= v and n < 500000:
                     
                mml = sd(sb(raw_mml[n]))
                l = len(mml.split())
                
                if l > int(begin) and l <= int(end):
                    if count%1000==0:print("count, n : ", count, n)
                    # appending the index
                    index_dict[i].append(n)

                    #  wrting mml and latex
                    #new_mml.write(raw_mml[n])
                    #new_latex.write(raw_latex[n])
    
                    # copying image
                    #src = raw_images + f"/{n}.png"
                    #dst = new_images + f"/{overall_count}.png"
                    #copyfile(src, dst)

                    count+=1
                    overall_count+=1
            #except:
            #    pass
        
                n+=1
print(n)

#new_mml.close()
#new_latex.close()

# saving index_dict
#json.dump(index_dict, open("/home/gauravs/data/img2mml_datasets/raw_datasets/our_data_100K/index_length_dist.json", "w"))


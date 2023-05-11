import os

latex = open("/Users/gaurav/Desktop/research/DONT_DELETE_training_data/new/opennmt/im2latex-100K/latex.lst").readlines()
os.chdir("/Users/gaurav/Desktop/research/DONT_DELETE_training_data/new/opennmt/olatex-100K")

strain, ttrain = open("src-train.lst", "w"), open("tgt-train.lst", "w")
stest, ttest = open("src-test.lst", "w"), open("tgt-test.lst", "w")
sval, tval = open("src-validate.lst", "w"), open("tgt-validate.lst", "w")
train, test, val = open("train.lst","w"), open("test.lst","w"), open("validate.lst","w")

N = len(mml)
ntrain = int(0.8 * N)
nstep = int(0.1 * N)

for i in range(0, ntrain):
    train.write(f"{i} {i} basic\n")
    strain.write(f"{i}.png\n")
    ttrain.write(latex[i]+"\n")

for i in range(ntrain, ntrain + nstep):
    test.write(f"{i} {i} basic\n")
    stest.write(f"{i}.png\n")
    ttest.write(latex[i]+"\n")

for i in range(ntrain + nstep, N):
    val.write(f"{i} {i} basic\n")
    sval.write(f"{i}.png\n")
    tval.write(latex[i]+"\n")

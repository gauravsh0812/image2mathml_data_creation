import os

def create_length_bleu_distribution_dataset(folder):

    lenlist = [0, 50, 100, 150, 200, 250, 300, 350]

    base = f"/home/skema/img2mml/gauravs_data_for_paper/data/opennmt/{folder}"
    if not os.path.exists(os.path.join(base, "length_bleu_distribution")):
        os.mkdir(os.path.join(base, "length_bleu_distribution"))

    tgt = open(f"{base}/tgt-test.lst").readlines()
    src = open(f"{base}/src-test.lst").readlines()

    for ll in lenlist:
        if ll!=350:
            category = f"{ll}-{ll+50}"
            print(f"{folder}-{category}")
            cat_tgt = open(f"{base}/length_bleu_distribution/tgt-test-{category}.lst", "w")
            cat_src = open(f"{base}/length_bleu_distribution/src-test-{category}.lst", "w")

            for (t,s) in zip(tgt, src):
                length = len(t.split())
                if length >= ll and length < ll+50:
                    cat_tgt.write(t)
                    cat_src.write(s)
        else:
            category = f"{ll}-more"
            print(category)
            cat_tgt = open(f"{base}/length_bleu_distribution/tgt-test-{category}.lst", "w")
            cat_src = open(f"{base}/length_bleu_distribution/src-test-{category}.lst", "w")

            for (t,s) in zip(tgt, src):
                length = len(t.split())
                if length >= ll:
                    cat_tgt.write(t)
                    cat_src.write(s)

if __name__=="__main__":
    for f in ["im2latex-100K", "im2mml-100K", "olatex-100K", "omml-100K"]:
        create_length_bleu_distribution_dataset(f)

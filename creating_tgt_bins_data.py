import os

def create_length_bleu_distribution_dataset(folder):

    lenlist = [0, 50, 100, 150, 200, 250, 300, 350]

    base = f"/home/skema/img2mml/gauravs_data_for_paper/data/opennmt/{folder}"

    if not os.path.exists(os.path.join(base, "length_based_distribution")):
        os.mkdir(os.path.join(base, "length_based_distribution"))
    if not os.path.exists(os.path.join(base, "content_based_distribution")):
        os.mkdir(os.path.join(base, "content_based_distribution"))

    tgt = open(f"{base}/tgt-test.lst").readlines()
    src = open(f"{base}/src-test.lst").readlines()

    # length_based_distribution
    for ll in lenlist:
        if ll!=350:
            category = f"{ll}-{ll+50}"
            print(f"{folder}-{category}")

            cat_tgt = open(f"{base}/length_based_distribution/tgt-test-{category}.lst", "w")
            cat_src = open(f"{base}/length_based_distribution/src-test-{category}.lst", "w")

            for (t,s) in zip(tgt, src):
                length = len(t.split())
                if length >= ll and length < ll+50:
                    # length_wise_separation
                    cat_tgt.write(t)
                    cat_src.write(s)

        else:
            category = f"{ll}-more"
            print(category)
            cat_tgt = open(f"{base}/length_based_distribution/tgt-test-{category}.lst", "w")
            cat_src = open(f"{base}/length_based_distribution/src-test-{category}.lst", "w")

            for (t,s) in zip(tgt, src):
                length = len(t.split())
                if length >= ll:
                    cat_tgt.write(t)
                    cat_src.write(s)


def create_content_bleu_distribution_dataset(latex_folder, mml_folder):

    lbase = f"/home/skema/img2mml/gauravs_data_for_paper/data/opennmt/{latex_folder}"
    mbase = f"/home/skema/img2mml/gauravs_data_for_paper/data/opennmt/{mml_folder}"
    tgt = open(f"{mbase}/tgt-test.lst").readlines()
    src = open(f"{lbase}/src-test.lst").readlines()

    lenlist = [0, 50, 100, 150, 200, 250, 300, 350]
    for ll in lenlist:
        if ll!=350:
            category = f"{ll}-{ll+50}"
        else:
            category = f"{ll}-more"

        con_tgt = open(f"{mbase}/length_based_distribution/tgt-test-{category}.lst", "w")
        con_src = open(f"{mbase}/length_based_distribution/src-test-{category}.lst", "w")
        cat_src = open(f"{lbase}/length_based_distribution/src-test-{category}.lst").readlines()

        for cs in cat_src:
            cat_idx = src.index(cs)
            con_tgt.write(tgt[cat_idx])
            con_src.write(cs)



if __name__=="__main__":
    # for f in ["im2latex-100K", "im2mml-100K", "olatex-100K", "omml-100K"]:
    #     create_length_bleu_distribution_dataset(f)

    create_content_bleu_distribution_dataset("olatex-100K", "omml-100K")
    create_content_bleu_distribution_dataset("im2latex-100K", "im2mml-100K")

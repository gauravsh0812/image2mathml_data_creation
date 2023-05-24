import os, sys

def get_scores(SRC, TGT, folder, pred, max_len, image_type):

    cmd = f"python translate.py \
        -data_type img \
        -model demos/{folder}/demo-model_step_100000.pt \
        -src_dir /home/gauravs/data/opennmt/{image_type} \
        -max_length {max_len} \
        -beam_size 5 \
        -gpu 0 \
        -image_channel_size 1 \
        -src {SRC} \
        -output {pred}"

    os.system(cmd)

    cmd = f"perl multi-bleu.perl {TGT} < {pred}"
    os.system(cmd)
    print("----------  -------------  --------------\n")
    cmd = f"python edit_distance.py --tgt {TGT} --pred {pred}"
    os.system(cmd)

    print("================="*3)

if __name__ == "__main__":
    # python length_content_comparison_opennmt.py im2mml-100K preds/im2mml-100K/ 300 images_processed
    # python length_content_comparison_opennmt.py im2latex-100K preds/im2latex-100K/ 200 images_processed
    # python length_content_comparison_opennmt.py omml-100K preds/omml-100K/ 300 oimages
    # python length_content_comparison_opennmt.py olatex-100K preds/olatex-100K/ 300 oimages

    folder = sys.argv[-4]
    pred_path = sys.argv[-3]
    max_len = sys.argv[-2]
    image_type = sys.argv[-1]

    lenlist = [0, 50, 100, 150, 200, 250, 300, 350]
    for ll in lenlist:
        if ll!=350:
            category = f"{ll}-{ll+50}"
            SRC = f"/home/gauravs/data/opennmt/{folder}/length_based_distribution/src-test-{category}.lst"
            TGT = f"/home/gauravs/data/opennmt/{folder}/tgt-test-{category}.lst"
            pred = pred_path + "-"+category+".lst"
        else:
            SRC = f"/home/gauravs/data/opennmt/{folder}/length_based_distribution/src-test-350-more.lst"
            TGT = f"/home/gauravs/data/opennmt/{folder}/tgt-test-350-more.lst"
            pred = pred_path + "-350-more.lst"

        get_scores(SRC, TGT, folder, pred, max_len, image_type)

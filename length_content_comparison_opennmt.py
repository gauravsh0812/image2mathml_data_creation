import os, sys

def get_scores(folder, pred_path, max_len):

    cmd = f"python translate.py \
        -data_type img \
        -model demo_{folder}/demo-model_step_100000.pt \
        -src_dir data/data_new/{FILE}-100K/images_processed \
        -max_length {max_len} \
        -beam_size 5 \
        -gpu 0 \
        -image_channel_size 1 \
        -src {SRC} \
        -output {pred_path}"

    os.system(cmd)



if __name__ == "__main__":
    folder = sys.argv[-3]
    pred_path = sys.argv[-2]
    max_len = sys.argv[-1]

    SRC = f"/home/gauravs/data/opennmt/{folder}/src-test.lst"
    TGT = f"/home/gauravs/data/opennmt/{folder}/tgt-test.lst"

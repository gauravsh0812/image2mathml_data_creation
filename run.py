import sys
from data_for_opennmt.opennmt_im2mml_nK import latex2mml
from data_for_opennmt.opennmt_im2latex_nK import im2mml_2_im2latex

if __name__=="__main__":

    cond = sys.argv[-1]

    # render im2mml from im2latex-103K for opennmt
    if cond == "opennmt_im2mml":
        latex2mml()
    if cond == "opennmt_im2latex":
        im2mml_2_im2latex()

    # grab the corresponding latex from im2latex-103K
    # m2l()

    # create data for cnn_xfmer
    # create_data()

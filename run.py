import sys
from data_for_opennmt.opennmt_im2mml_nK import latex2mml
from data_for_opennmt.opennmt_im2latex_nK import im2mml_2_im2latex
# from getting_distribution_of_datasets.get_length_dist import get_dist

if __name__=="__main__":

    cond = sys.argv[-1]

    # render im2mml from im2latex-103K for opennmt
    if cond == "opennmt_im2mml":
        latex2mml()
    if cond == "opennmt_im2latex":
        im2mml_2_im2latex()
    # if cond == "get_distribution":
    #     get_distribution()

    # grab the corresponding latex from im2latex-103K
    # m2l()

    # create data for cnn_xfmer
    # create_data()

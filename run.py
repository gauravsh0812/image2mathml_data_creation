import sys
from data_for_opennmt.opennmt_im2mml_nK import latex2mml
from data_for_opennmt.opennmt_im2latex_nK import im2mml_2_im2latex
from data_for_opennmt.create_images_opennmt_odata import no_blank_data

if __name__=="__main__":

    cond = sys.argv[-1]

    # render im2mml from im2latex-103K for opennmt
    # if cond == "opennmt_im2mml":
    #     latex2mml()
    # if cond == "opennmt_im2latex":
    #     im2mml_2_im2latex()

    if cond == "remove_blank_data":
        no_blank_data()

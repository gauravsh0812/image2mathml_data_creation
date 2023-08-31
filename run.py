import sys
from data_for_opennmt.opennmt_im2mml_nK import latex2mml
from data_for_opennmt.opennmt_im2latex_nK import im2mml_2_im2latex
from data_for_opennmt.create_images_opennmt_odata import no_blank_data
from data_for_opennmt.reformatting import reformat
from data_for_opennmt.cleaning_odata_im2data import remove_eqn_corr_blank_img
from get_length_dist import get_distribution_opennmt, get_distribution_odata

if __name__=="__main__":

    cond = sys.argv[-1]

    base_path = "/home/gauravs/data"

    # render im2mml from im2latex-103K for opennmt
    if cond == "opennmt_im2mml":
        latex2mml(base_path)
    if cond == "opennmt_im2latex":
        im2mml_2_im2latex(base_path)

    if cond == "remove_blank_data":
        no_blank_data(base_path)

    if cond == "reformatting":
        reformat(base_path)
    
    if cond == "distribution_opennmt":
        get_distribution_opennmt(base_path)
    
    if cond == "distribution_odata":
        get_distribution_odata(base_path)
    
    if cond == "clean_odata_im2data":
        remove_eqn_corr_blank_img(base_path)
    

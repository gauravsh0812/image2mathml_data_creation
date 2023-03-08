from creating_im2mml_latex_nK.create_im2mml_nK import latex2mml as l2m
from creating_im2mml_latex_nK.create_im2mml_nK import im2mml_2_im2latex as m2l


if __name__=="__main__":
    # render im2mml from im2latex-103K
    l2m()

    # grab the corresponding latex from im2latex-103K
    # m2l()

import os

def remove_eqn_corr_blank_img(base_path):
    blank = open(f'{base_path}/odata/im2data/im2data_blank_images.txt').readlines()
    blank = [int(b.split(".")[0]) for b in blank ]

    mml = open(f'{base_path}/odata/im2data/mml.lst').readlines()
    latex = open(f'{base_path}/odata/im2data/latex.lst').readlines()

    _mml = open(f'{base_path}/odata/im2data/mml_new.lst', 'w')
    _latex = open(f'{base_path}/odata/im2data/latex_new.lst', 'w')

    assert len(mml) == len(latex)

    for i in range(len(mml)):
        if i in blank:
            pass
        else:
            _mml.write(mml[i])
            _latex.write(latex[i])

    
# image2mathml_data_creation

### create data for opennmt:

1) create dataset: im2mml_nK from the im2latex-103K. Run `python run.py "opennmt_im2mml"`
2) create dataset: im2latex_nK. Run `python run.py "opennmt_im2latex"`
3) get the distribution of the im2mml_nK
4) sample the dataset from arxiv created dataset
5) create dataset: omml_nK for opennmt
6) create dataset: olatex_nK for opennmt

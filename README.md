# image2mathml_data_creation

### create data for opennmt:

All the data will be under /home/skema/img2mml/gauravs_data_for_paper/data

1) create dataset: im2mml_nK from the im2latex-103K. Run `python run.py opennmt_im2mml`
2) create dataset: im2latex_nK. Run `python run.py opennmt_im2latex`
3) get the distribution of the im2mml_nK
4) sample the dataset from "arxiv created" dataset. Save it as "our_arxiv_sample_dataset".
5) Preprocess the sampled dataset:
    use OpenNMT (`https://github.com/harvardnlp/im2markup`) to preprocess the `original_latex.lst` sampled in above step.
    preprocess the `original_mml.lst` using `preprocessing/preprocess_mml.py` script.
    and preprocess images using  `preprocessing/preprocess_images.py` script.
    (NOTE: We don't need to preprocess images for OpenNMT. It is for Our model.)
    The final sampled dataset has both omml_nK and olatex_nK for our model.

next steps can be done on local system. copying data to local system.
6) create dataset: omml_nK for opennmt
7) create dataset: olatex_nK for opennmt

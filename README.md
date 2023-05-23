# image2mathml_data_creation

### create data for opennmt:

All the data will be under /home/skema/img2mml/gauravs_data_for_paper/data

1) create dataset: im2mml_nK from the im2latex-103K. Run `python run.py opennmt_im2mml`
2) create dataset: im2latex_nK. Run `python run.py opennmt_im2latex`
3) get the distribution of the im2mml_nK. Run `python get_length_dist.py`
4) sample the dataset from "arxiv created" dataset. Save it as "our_sample_dataset".
5) Preprocess the sampled dataset:
    use OpenNMT (`https://github.com/harvardnlp/im2markup`) to preprocess the `original_latex.lst` sampled in above step.
    preprocess the `original_mml.lst` using `preprocessing/preprocess_mml.py` script.
    and preprocess images using  `preprocessing/preprocess_images.py` script.
    (NOTE: We don't need to preprocess images for OpenNMT. It is for Our model.)
    The final sampled dataset has both omml_nK and olatex_nK for our model.

before proceeding, let's copy all the relevant image folders to respective
directories to create final structure as mention below.

for opennmt create a new image folder that will not contain any blank image from our dataset.
Make sure you have the "blank_images log" under "image2mathml_data_creation" folder.
6) move the "sampled_data" to "odata" as our_sampled_data. Then `python run.py remove_blank_data`
6a) preprocess the "no_blank_original_latex.lst" using opennmt-lua and rename it to latex.lst.
use `python scripts/preprocessing/preprocess_formulas.py --mode normalize --input-file /home/skema/img2mml/gauravs_data_for_paper/data/odata/our_sampled_data/no_blank_original_latex.lst --output-file /home/skema/img2mml/gauravs_data_for_paper/data/odata/our_sampled_data/latex.ls`

7) run `python run.py reformatting` to create dataset: omml_nK/olatex_nK for opennmt and im2data for odata.
7a) copy opennmt/images_processed to odata/im2data manually

Final structure of the datasets would be :
datasets
    im2latex-103K
    opennmt
        images_processed (cp from im2latex-103K)
        oimages (create using create_images_opennmt_odata, removing blank images)
        odata_blank_images.txt
        im2data_distributions
        im2mml-100K
            original_mml.lst
            mml.lst
            train/test/validate.lst          
            src-train/test/validate.lst
            tgt-train/test/validate.lst

        im2latex-100K
            original_latex.lst
            latex.lst
            train/test/validate.lst          
            src-train/test/validate.lst
            tgt-train/test/validate.lst

        olatex-100K
            original_latex.lst
            latex.lst
            train/test/validate.lst          
            src-train/test/validate.lst
            tgt-train/test/validate.lst

        omml-100K
            original_mml.lst
            mml.lst          
            train/test/validate.lst          
            src-train/test/validate.lst
            tgt-train/test/validate.lst

    odata
        our_sampled_data
            images
            image_tensors
            original_mml/latex.lst (use opennmt preprocessing code to preprocess LaTeX)
            no_blank_original_latex.lst
            mml/latex.lst
            paths.lst

        im2data
            images_processed
            image_tensors (will be created when preprocess the data)
            original_mml/latex.lst
            mml/latex.lst

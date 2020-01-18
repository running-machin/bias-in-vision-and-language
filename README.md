## Installation
`
pip install spacy==2.1.0
python -m spacy download en
pip install neuralcoref --no-binary neuralcoref

# for ViLBERT, we removed the python-prctl
# from requirements.txt

`

## Download Pre-trained Models
We use the ViLBERT 6-layer model trained on Conceptual Captions, with model checkpoint and config file found [here](https://drive.google.com/drive/folders/1Re0L75uazH3Qrep_aRgtaVelDEz4HV9c).


## Usage
For running ViLBERT:
`
conda create -n vilbert python=3.6
conda activate vilbert
cd vilbert_beta
pip install -r requirements.txt
`

For extracting visual features:
`conda install caffe`


For running VisualBERT:
`
conda create -n visual-bias python=3.7
conda activate visual-bias
cd vilbert_beta

conda install numpy pyyaml setuptools cmake cffi tqdm pyyaml scipy ipython mkl mkl-include cython typing h5py pandas nltk spacy numpydoc scikit-learn jpeg tensorflow
pip install tensorflow-hub

#Please check your cuda version using `nvcc --version` and make sure the cuda version matches the cudatoolkit version.
conda install pytorch torchvision cudatoolkit=10.1 -c pytorch

# Below is the way to install allennlp recommended in R2C. But in my experience, directly installing allennlp seems also okay.
pip install -r allennlp-requirements.txt
pip install --no-deps allennlp==0.8.0
python -m spacy download en_core_web_sm
pip install attrdict
pip install pycocotools
pip install commentjson
`

Download [pretrained VisualBERT](https://drive.google.com/file/d/1QvivVfRsRF518OQSQNaN7aFk6eQ43vP_/view).

To compute image features, we use the same model backbone/size as VisualBERT. Detectron model id is 137851257 ([see Model Zoo](https://github.com/facebookresearch/detectron2/blob/master/MODEL_ZOO.md)).\

// from https://www.bls.gov/cps/cpsaat11.htm and https://github.com/uclanlp/corefBias

Write all image features to single file for convenience
`./scripts/image-features/format_image_features.py --config scripts/image-features/google_images_config.yaml`
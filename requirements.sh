#!/usr/bin/env bash

conda install --yes lxml
conda install --yes nltk=3.8.1
conda install --yes pep8
conda install --yes pylint
#conda install --yes pycodestyle
conda install --yes pytest
conda install --yes PyYAML
conda install --yes regex
conda install --yes requests
conda install --yes pathlib
conda install -c conda-forge spacy
python -m spacy download en
python -m spacy download en_core_web_lg
bash scripts/download_ntlk_corpus.sh


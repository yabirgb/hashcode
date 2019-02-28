#!/bin/bash

testa="a_example"
testb="b_lovely_landscapes"
testc="c_memorable_moments"
testd="d_pet_pictures"
teste="e_shiny_selfies"

python3 main.py $testa
python3 main.py $testb
python3 main.py $testc
python3 main.py $testd
python3 main.py $teste

zip -r ohno *.py

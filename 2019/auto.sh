#!/bin/bash

testa="a_example"
testb="b_lovely_landscapes"
testc="c_memorable_moments"
testd="d_pet_pictures"
teste="e_shiny_selfies"

time python3 main.py $testa 50 50 0.4 0.2 0.3
time python3 main.py $testb 50 50 0.4 0.2 0.3
time python3 main.py $testc 50 50 0.4 0.2 0.3
time python3 main.py $testd 50 50 0.4 0.2 0.3
time python3 main.py $teste 50 50 0.4 0.2 0.3

zip -r ohno *.py

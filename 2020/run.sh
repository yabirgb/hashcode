#!/bin/bash

testa="inputs/a_example"
testb="inputs/b_read_on.txt"
testc="inputs/c_incunabula.txt"
testd="inputs/d_tough_choices.txt"
teste="inputs/e_so_many_books.txt"
testf="inputs/f_libraries_of_the_world.txt"

python3 main.py $testa
python3 main.py $testb
python3 main.py $testc
python3 main.py $testd
python3 main.py $teste
python3 main.py $testf
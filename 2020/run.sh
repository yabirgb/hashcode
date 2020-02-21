#!/bin/bash

testa="inputs/a_example.txt"
testb="inputs/b_read_on.txt"
testc="inputs/c_incunabula.txt"
testd="inputs/d_tough_choices.txt"
teste="inputs/e_so_many_books.txt"
testf="inputs/f_libraries_of_the_world.txt"

time python3 main.py $testa
time python3 main.py $testb
time python3 main.py $testc
time python3 main.py $testd
time python3 main.py $teste
time python3 main.py $testf

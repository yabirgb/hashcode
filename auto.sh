#!/bin/bash

testa="a_example"
testb="b_should_be_easy"
testc="c_no_hurry"
testd="d_metropolis"
teste="e_high_bonus"

python3 main.py $testa
python3 main.py $testb
python3 main.py $testc
python3 main.py $testd
python3 main.py $teste

zip output/code main.py ride.py plan.py car.py

from __future__ import print_function	
import os
from random import randint
from time import sleep

my_location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
input_path = os.path.join(my_location, 'nova-juno-tests-out')

while True:
    with open(input_path) as f:
        for l in f:
            print(l, end="")
            sleep(randint(100, 600) / 1000.0)   

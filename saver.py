from __future__ import print_function	
from os import path, getcwd
from random import uniform, gauss
from time import sleep

my_location = path.realpath(path.join(getcwd(), path.dirname(__file__)))
input_path = path.join(my_location, 'data/nova-juno-tests-out')

while True:
    with open(input_path) as f:
        for l in f:
            print(l, end="")
            #timeout = uniform(0.1, 0.6)
            timeout = abs(gauss(0.0, 0.3))
            sleep(timeout)


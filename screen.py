from __future__ import print_function	
from random import randint
from time import sleep

while True:
    with open('nova-juno-tests-out') as f:
        for l in f:
            print(l, end="")
            sleep(randint(100, 600) / 1000.0)   

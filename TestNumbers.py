# from sys import stdin
# from random import choice
# from string import ascii_lowercase
# import time
import sys
import random
import time

def list_solution(values, collection):
    for value in values:
        assert value in collection

def set_solution(values, collection):
    for value in values:
        assert value in collection

size = 50000000
mylist = [x for x in range(size)]

values = [random.randint(0, size) for _ in range(100)]

start_time = time.time()
list_solution(values, mylist)
print("Test Numbers: time elapsed for list solution: {:.2f}s".format(time.time() - start_time))

myset = set(mylist)
start_time = time.time()
set_solution(values, myset)
print("Test Numbers: time elapsed for set solution: {:.2f}s".format(time.time() - start_time))

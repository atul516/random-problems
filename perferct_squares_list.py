# import numpy as np
import math
from sympy.utilities.iterables import multiset_permutations
import argparse
from collections.abc import MutableMapping 
import json 
from scipy.stats._resampling import permutation_test

possibilities = {}
    
def is_square(i):
    return i == math.isqrt(i) ** 2

def count_squares(n):
    return (math.isqrt(n))

def get_perfect_squares_array(n):
    return [i**2 for i in range(1, math.isqrt(n) + 1)]

def check_if_all_squares(perm):
    c = 0
    l = len(perm)
    for i in range(l - 1):
        if (is_square(perm[i] + perm[i+1])):
            c += 1
    return c

def print_squares(seq):
    l = len(seq)
    for i in range(l-1):
        print(seq[i] + seq[i+1])

def build_grand_chain(previous_list):
    last_elem = previous_list[-1]
    next_possible_nodes = possibilities[last_elem]
    for i, (j,v) in enumerate(next_possible_nodes.items()):
        if (is_square(j+last_elem) and j not in previous_list):
            previous_list.append(j)
            return {j : build_grand_chain(previous_list)}

def compute(seq):
    # print('**************Running Compute_v4 on sequence 32:*********************** \n ', seq)
    permutation_list= []
    for i in range(len(seq)):
        permutation_list.extend(
            [list((seq[i], a)) for a in seq if is_square(seq[i] + a) and seq[i] != a]
            )

    deduplicated_set = set(map(frozenset, permutation_list))
    deduplicated_list = [list(i) for i in deduplicated_set]
    
    for i in range(len(seq)):
        count = {}
        for j in deduplicated_list:
            if(seq[i] in j):
                count[[k for k in j if k!=seq[i]][0]] = {}
        possibilities[seq[i]] = count

    for i, (k,v) in enumerate(possibilities.items()):
        print(k, v)
    
    g_chain = {}
    
    for i, (j,v) in enumerate(possibilities.items()):
        previous_list = [j]
        g_chain[j] = build_grand_chain(previous_list)
    
    json_dump = json.dumps(g_chain,indent=2)
    print(json_dump)
    
if __name__ == '__main__':
    argvparser = argparse.ArgumentParser()
    argvparser.add_argument('number', help='Number of elements', type=int)
    args = argvparser.parse_args()
    n = args.number
    seq = list(range(1,n+1))
    compute(seq)
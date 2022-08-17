# import numpy as np
import math
from sympy.utilities.iterables import multiset_permutations
import argparse
from collections.abc import MutableMapping 
import json 
from scipy.stats._resampling import permutation_test

grand_chain = {}
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
        count = []
        for j in deduplicated_list:
            if(seq[i] in j):
                count.append([k for k in j if k!=seq[i]][0])
        possibilities[seq[i]] = count

    # for i, (k,v) in enumerate(possibilities.items()):
    #     print(i, k, v)

    for i, (k,v) in enumerate(possibilities.items()):
        grand_chain[k] = {}
        li = list ([k])
        build_grand_chain(li)
    json_dump = json.dumps(grand_chain,indent=2)
    print(json_dump)

def build_grand_chain(li):
    if(len(li) > 0):
        for l in possibilities[li[-1]]:
            if(l not in li and is_square(l+li[-1])):
                exprr = 'grand_chain['
                for x in li:
                    exprr += str(x) + ']' + '['
                exprr += str(l) + ']'
                exec('{} = {}'.format(exprr, '{}'))
                li.append(l)
                build_grand_chain(li)

if __name__ == '__main__':
    argvparser = argparse.ArgumentParser()
    argvparser.add_argument('number', help='Number of elements', type=int)
    args = argvparser.parse_args()
    n = args.number
    seq = list(range(1,n+1))
    compute(seq)
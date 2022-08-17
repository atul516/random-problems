# import numpy as np
import math
import argparse
import json 
from sympy.ntheory.primetest import is_square

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

def flatten(input_dict, separator='_', prefix=''):
    output_dict = {}
    for key, value in input_dict.items():
        if isinstance(value, dict) and value:
            deeper = flatten(value, separator, prefix+key+separator)
            output_dict.update({key2: val2 for key2, val2 in deeper.items()})
        elif isinstance(value, list) and value:
            for index, sublist in enumerate(value, start=1):
                if isinstance(sublist, dict) and sublist:
                    deeper = flatten(sublist, separator, prefix+key+separator+str(index)+separator)
                    output_dict.update({key2: val2 for key2, val2 in deeper.items()})
                else:
                    output_dict[prefix+key+separator+str(index)] = value
        else:
            output_dict[prefix+key] = value
    return output_dict

def build_grand_chain(next_possible_nodes, previous_list):
    return_obj = {}
    next_possible_nodes = list(set(next_possible_nodes) - set(previous_list))
    if(len(next_possible_nodes) and len(previous_list)):
        for j in next_possible_nodes:
            previous_list_1 = list(previous_list)
            if (is_square(j+previous_list_1[-1])):
                previous_list_1.append(j)
                return_obj[str(j)] = build_grand_chain(possibilities[j],previous_list_1)
            else:
                return_obj[str(j)] = {}

            if(len(previous_list_1) == 30 and check_if_all_squares(previous_list_1) == 29):
                print(previous_list_1)
                print('Success')
                return
        return return_obj
    else:
        return {}

def compute(seq):
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
    #     print(k, v)
    
    g_chain = {}
    
    for j in possibilities.keys():
        previous_list = [j]
        g_chain[str(j)] = build_grand_chain(possibilities[j],previous_list)
    
    json_dump = json.dumps(flatten(g_chain),indent=2)
    # print(json_dump)
    
if __name__ == '__main__':
    argvparser = argparse.ArgumentParser()
    argvparser.add_argument('number', help='Number of elements', type=int)
    args = argvparser.parse_args()
    n = args.number
    seq = list(range(1,n+1))
    compute(seq)
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
        
#don't use compute_v1
# def compute_v1(n):
#     seq = np.linspace(1, n, n, dtype=int)
    
    #Don't use a list of all permutations as we hit a barrier while calculating it
    for perm in list((multiset_permutations(seq))):
        if check_if_all_squares(perm):
            print(perm)

#this is still not working, let's try the reverse approach in compute_v3
# def compute_v2(n):
#     t = np.math.factorial(n)
#     print('Total sample space (n!): {}'.format(t))
#     seq = np.linspace(1, n, n, dtype=int)
#     i = 0
#     success = False
#     max_count_seq = None
#     max_count = 0
#     ite = 5000000 if t>5000000 else t
#     while i<=ite and success == False:
#         i += 1
#         np.random.shuffle(seq)
#         c = check_if_all_squares(seq)
#         if c == n-1:
#             success = True
#             print('Success with sequence: {}'.format(seq))
#         if i%1000000 == 0:
#             print('Iteration: {}'.format(i))
#             if success == False:
#                 print('So far, the sequence with max value of perfect squares is: {}'.format(max_count_seq))
#                 print('So far, maximum value of perfect squares: {} and is not same as optimum value of {}'.format(max_count, n-1))
#         if c > max_count:
#             max_count = c
#             max_count_seq = list(seq)
#
#     print('Maximum value of perfect squares lies in sequence: {}'.format(max_count_seq))
#     print('Maximum value of perfect squares: {} and is not same as optimum value of {}'.format(max_count, n-1))

def compute_v3(n):
    seq = list(range(1,n+1))
    final_list = []
    l = len(seq)
    final_list.append(seq[-1])
    seq.pop(-1)
    offset = 0
    while len(final_list) <= l:
        we_progress = True
        print(final_list)
        while we_progress:
            l1 = len(final_list)
            for i, val in enumerate(seq):
                if (offset == 0 
                    and is_square(final_list[-1] + seq[i])
                    ):
                    final_list.append(seq[i])
                    seq.pop(i)
                    break
                elif(offset > 0 
                     and is_square(final_list[len(final_list)-(offset + 1)] + seq[i])
                     and is_square(final_list[len(final_list)-offset] + seq[i])
                     ):
                    final_list.insert(len(final_list)-offset, seq[i])
                    seq.pop(i)
                    break
          
            if(len(final_list) <= l1):
                we_progress = False
                offset += 1


    print(check_if_all_squares(final_list))

def compute_v4(seq):
    # print('**************Running Compute_v4 on sequence 32:*********************** \n ', seq)
    permutation_list= []
    for i in range(len(seq)):
        permutation_list.extend(
            [list((seq[i], a)) for a in seq[i:] if is_square(seq[i] + a) and seq[i] != a]
            )
    # print('\n', permutation_list, '\n')
    
    print(permutation_list)
    
    for i in range(len(seq)):
        count = []
        for j in permutation_list:
            if(seq[i] in j):
                count.append([k for k in j if k!=seq[i]][0])
        possibilities[seq[i]] = count

    #print possibilities
    # for i, (k,v) in enumerate(possibilities.items()):
    #     print(i, k, v)

    for i, (k,v) in enumerate(possibilities.items()):
        grand_chain[k] = {}
        li = list ([k])
        build_grand_chain(li)
    # json_dump = json.dumps(grand_chain,indent=2)
    # print(json_dump)

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


    # small_seq1 = []
    #combine small seq
    # while len(small_seq):
    #     for v in small_seq:
    #         if i!=v:
    #             if i[0] == v[0]:
    #                 small_seq1.append([i[2],i[1], v[0],v[1],v[2]])
                # or i[0] == v[2]
                # or i[2] == v[0]
                # or i[2] == v[2]):
        
    # deduplicated_set = set(map(frozenset, permutation_list))
    # deduplicated_list = [list(i) for i in deduplicated_set]
    # final_list = []
    # ite = 1
    # while len(final_list) == 0 or len(final_list[0]) <= n:
    #     # print(permutation_list)
    #     # print('\nOuter iteration----------------------: ', ite)
    #     # print(len(permutation_list[0]))
    #     for j in range(len(permutation_list)):
    #         final_list.extend(
    #             [permutation_list[j] + a for a in permutation_list[j+1:] if (is_square(permutation_list[j][-1] + a[0]) or is_square(permutation_list[j][0] + a[-1])) and not(set(permutation_list[j]) & set(a))]
    #             )
    #     if(len(final_list) == 0):
    #         break
    #     permutation_list = list(final_list)
    #     final_list = []
    #     ite += 1
    # return permutation_list

if __name__ == '__main__':
    argvparser = argparse.ArgumentParser()
    argvparser.add_argument('number', help='Number of elements', type=int)
    args = argvparser.parse_args()
    #seq = [18,7,20,29,16,9,27,22,14,2,23,26,10,15,21,28,8,17,19,30,6,3,13,12,4,5,11,25,24,1]
    n = args.number
    seq = list(range(1,n+1))
    compute_v4(seq)
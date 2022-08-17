import math
import argparse
import sys

possibilities = {}
n = 0
    
def is_square(i):
    return i == math.isqrt(i) ** 2

def check_if_all_squares(perm):
    c = 0
    l = len(perm)
    for i in range(l - 1):
        if (is_square(perm[i] + perm[i+1])):
            c += 1
    return c

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
    
    g_chain = {}
    
    for j in possibilities.keys():
        previous_list = [j]
        g_chain[str(j)] = build_grand_chain(possibilities[j],previous_list)


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
            #check if its already found
            if(len(previous_list_1) == n and check_if_all_squares(previous_list_1) == n-1):
                print(previous_list_1)
                #check if all individual elements are unique
                print(list(set(previous_list_1) - set(list(range(1,n+1)))))
                #stop execution
                sys.exit("Success")
        return return_obj
    else:
        return {}

    
if __name__ == '__main__':
    argvparser = argparse.ArgumentParser()
    argvparser.add_argument('number', help='Number of elements', type=int)
    args = argvparser.parse_args()
    n = args.number
    seq = list(range(1,n+1))
    compute(seq)
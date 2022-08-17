import math
import argparse
import sys

possibilities = []
truncated_possibilities={}
n = 0
COUNT = 0
def increment():
    global COUNT
    COUNT = COUNT+1
    
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
        possibilities.append(count)
    
    print(possibilities)
    for j in range(len(possibilities)):
        previous_list = [j+1]
        find_all_solutions(possibilities[j],previous_list)
    global COUNT
    global n
    print('n = {} has {} solutions'.format(n, math.floor(COUNT/2)))


def find_all_solutions(next_possible_nodes, previous_list):
    global n
    next_possible_nodes = list(set(next_possible_nodes) - set(previous_list))
    if(len(next_possible_nodes) and len(previous_list)):
        for j in next_possible_nodes:
            previous_list_1 = list(previous_list)
            if (is_square(j+previous_list_1[-1])):
                previous_list_1.append(j)
                find_all_solutions(possibilities[j-1],previous_list_1)
            #check if its already found
            if(len(previous_list_1) == n
               and check_if_all_squares(previous_list_1) == n-1
               and len(list(set(previous_list_1) - set(list(range(1,n+1))))) == 0
               ):
                increment()
                #check if all individual elements are unique
                #stop execution
                # sys.exit("Success")

    
if __name__ == '__main__':
    argvparser = argparse.ArgumentParser()
    argvparser.add_argument('number', help='Number of elements', type=int)
    args = argvparser.parse_args()
    n = args.number
    seq = list(range(1,n+1))
    compute(seq)
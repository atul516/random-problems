import math
import argparse
import sys
import time

possibilities = []
n = 0
COUNT = 0
start = time.perf_counter()
sol_found = False
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
    
    for j in range(len(possibilities)):
        if(sol_found):
            break
        previous_list = [j+1]
        next_possible_nodes = [x for x in possibilities[j] if x not in previous_list]
        find_first_solution(next_possible_nodes ,previous_list)
    global COUNT
    global n
    print('n = {} has {} solutions'.format(n, math.floor(COUNT/2)))


def find_all_solutions(next_possible_nodes, previous_list):
    global n
    if(len(next_possible_nodes) and len(previous_list)):
        for j in next_possible_nodes:
            previous_list_1 = list(previous_list)
            previous_list_1.append(j)
            next =  [x for x in possibilities[j-1] if x not in previous_list]
            find_all_solutions(next,previous_list_1)
            #check if its already found
            if(len(previous_list_1) == n
               and check_if_all_squares(previous_list_1) == n-1
               and len(list(set(previous_list_1) - set(list(range(1,n+1))))) == 0
               ):
                increment()
                #check if all individual elements are unique
                #stop execution
                # sys.exit("Success")

def find_first_solution(next_possible_nodes, previous_list):
    global n
    global start
    global sol_found
    if(len(next_possible_nodes) and len(previous_list)):
        for j in next_possible_nodes:
            previous_list_1 = list(previous_list)
            previous_list_1.append(j)
            # check if its already found
            if (len(previous_list_1) == n
                    and check_if_all_squares(previous_list_1) == n - 1
                    and len(list(set(previous_list_1) - set(list(range(1, n + 1))))) == 0
            ):
                sol_found = True
                print(f"Solution found:\n {previous_list_1}")
                end = time.perf_counter()
                print(f"Time taken: {end - start} seconds")
                # stop execution
                sys.exit()
            else:
                next =  [x for x in possibilities[j-1] if x not in previous_list]
                find_first_solution(next,previous_list_1)
    
if __name__ == '__main__':
    argvparser = argparse.ArgumentParser()
    argvparser.add_argument('number', help='Number of elements', type=int)
    args = argvparser.parse_args()
    n = args.number
    seq = list(range(1,n+1))
    compute(seq)
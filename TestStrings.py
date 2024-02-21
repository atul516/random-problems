import time
start_time = time.time()

def solution(values, collection):
    counter = 0
    for value in values:
        if value in collection:
            print(counter)
            counter += 1

#load one million strings
with open('strings.txt', 'r') as file:
    mylist = file.read().splitlines()

# we will search for 1000 strings among a million strings to elapse a comparable time
with open('to_find.txt', 'r') as file:
    to_find = file.read().splitlines()
print("Pre. work: {:.2f}s".format(time.time() - start_time))

start_time = time.time()
myset = set(mylist)
print("Set creation: {:.2f}s".format(time.time() - start_time))

start_time = time.time()
solution(to_find, myset)
print("Test Strings: time elapsed for set solution: {:.2f}s".format(time.time() - start_time))

start_time = time.time()
solution(to_find, mylist)
print("Test Strings: time elapsed for list solution: {:.2f}s".format(time.time() - start_time))


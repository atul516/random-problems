import random
from random import choice
from string import ascii_lowercase

mylist = list()
for _ in range(10**6):
    s = ''.join([choice(ascii_lowercase) for _ in range(10)])
    if (_ == 10**6//2):
        mylist.append("atul")
        pass
    mylist.append(s)

with open('strings.txt', 'w') as file:
    file.write('\n'.join(mylist))


with open('to_find.txt', 'w') as file:
    random_find_strs = list()
    for _ in range(2000):
        ind = random.randint(0,10**6)
        random_find_strs.append(mylist[ind])
    file.writelines('\n'.join(random_find_strs))
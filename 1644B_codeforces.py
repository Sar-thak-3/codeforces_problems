# Anti-Fibonacci Permutation
from itertools import permutations

test_cases = int(input())
final_list = []
lenlist = []
for le in range(test_cases):
    length = int(input())
    lenlist.append(length)

total = 0
for case in lenlist:
    total += case
    permut_list = list(permutations(range(1,case+1)))
    # print(permut_list)
    for itm in permut_list:
        newitm = itm[2:]
        # print(itm)
        for index,n in enumerate(newitm):
            if (itm[index]+itm[index+1])==itm[index+2]:
                break
            elif (itm[index]+itm[index+1])!=itm[index+2] and index==(len(itm)-3):
                final_list.append(itm)
        if len(final_list)==total:
            break  
for itm in final_list:
    for sub in itm: print(sub,end=" ")
    print()             
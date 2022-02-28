# Phoenix and gold --> Codeforces
import random
test_cases = int(input())
number_and_avoidable = input()
number_and_avoidable = number_and_avoidable.split(" ")
weights = input()
weights = weights.split(" ")
sum = 0
correct = []
def fibbonacci(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fibbonacci(n-1)    
for n in range(0,fibbonacci(int(number_and_avoidable[0]))):
    if correct != []:
        break   
    for one_one in weights:
        sum = sum + int(one_one)
        if sum==int(number_and_avoidable[1]):
            random.shuffle(weights)
            sum = 0
            break
        elif weights.index(one_one) == len(weights)-1:
            correct = weights
            break
if correct == []:
    print("NO")
else:    
    print("YES")
    print(" ".join(correct))            
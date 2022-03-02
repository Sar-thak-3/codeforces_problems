# Fashion in Berland --> Codeforces
buttons = int(input())
f = input()
f = f.split(" ")
fastened = list(map(lambda x:int(x),f))
if (buttons>1 and fastened.count(0)<2) or (buttons==1 and fastened[0]==1):
    print("YES")
else:
    print("NO")    
number = int(input())
a = input()
a = a.split(" ")
arrange = list(map(lambda x:int(x),a))
dictonary = {}    

second_hole = 0
for i in range(1,number+1):
    for i1 in range(1,number+1):
        dictonary[i1] = 0
    dictonary[i] = 1
    for itm in arrange:
        val = dictonary.get(itm)
        dictonary[itm] = val + 1
        if dictonary[itm]>1:
            second_hole = itm
            break  
    print(second_hole,end=" ")
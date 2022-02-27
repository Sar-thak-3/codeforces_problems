info = input()
info = info.split(" ")
information = list(map(lambda x: int(x),info))
def max_nuts(sections,max_nuts,divisors):
    if sections-1<=divisors:
        information[2] -= sections-1
        return (sections)*max_nuts
    else:
        information[2] = 0
        return (divisors+1)*max_nuts

box = 0
while True:
    maxi_nuts = max_nuts(information[0],information[3],information[2])
    box = box+1
    rem_nuts = information[1]-maxi_nuts
    information[1] -= maxi_nuts
    if rem_nuts<=0:
        break   
print(box)
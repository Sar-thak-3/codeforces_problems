f = input()
f = f.split(" ")
info = list(map(lambda x:int(x),f))
p = input()
p = p.split(" ")
poured = list(map(lambda x:int(x),p))
min_req = 0
for p in poured:
    min_req += max(poured)-p
if min_req>info[1]:
    print(-1)
else:
    info[1] = info[1]-min_req
    remaining = info[1]/info[0]
    for p in poured:
        print(f"{max(poured)-p+remaining : 0.6f}")
# Doors and Keys
test_case = int(input())
result = []
for n in range(test_case):
    way = input()
    if way.index("r")<way.index("R") and way.index("g")<way.index("G") and way.index("b")<way.index("B"):
        result.append("YES")
    else:
        result.append("NO")
for itm in result:
    print(itm)        
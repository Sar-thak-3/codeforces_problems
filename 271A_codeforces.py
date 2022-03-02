year = int(input())
while True:
    sum = 0
    year = year + 1
    set_year = set(str(year))
    if len(set_year)==4:
        print(year)
        break
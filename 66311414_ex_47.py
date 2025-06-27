number = int(input())

ls = [input() for _ in range(number)]
ls = sorted(ls)
for i in ls :
    print(i)
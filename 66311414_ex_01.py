number = int(input())
lst = []
for i in range(number) :
    x = int(input())
    if x % 2 == 0:
        lst.append(x)

print(*lst , sep = '\n')
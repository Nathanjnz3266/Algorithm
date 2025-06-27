number = int(input())
ls = [int(input()) for _ in range(number)]
ls.sort()
c = number // 2
if number % 2 == 1 :
    m = (ls[c])
print(m)
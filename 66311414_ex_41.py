number = int(input())
ls = [int(input()) for _ in range(number)]
ls.sort()
c = number // 2
if number % 2 == 0 :
    m = (ls[c] + ls[c-1]) / 2
print(f"{m:.2f}")
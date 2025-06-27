n = int(input())
rr = 0

for i in range(n) :
    r = int(input())
    if r % 3 == 0:
        rr += r

print(rr)
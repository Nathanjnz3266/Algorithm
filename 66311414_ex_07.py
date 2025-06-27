r = int(input())
sum = 0

for i in range(r) :
    n = int(input())
    sum += n

avg = sum / r

print(f"{avg:.2f}")
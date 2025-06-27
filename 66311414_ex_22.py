n = int(input())
sum = 0
for i in range(n) :
    number = int(input())
    sum += number
avg = sum / n
print(f"{avg:.2f}")

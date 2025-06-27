sum = 0
count = 0
while True :
    number = int(input())
    if number == 0 :
        break
    count += 1
    sum += number
Abso = sum / count
print(f"{Abso:.2f}")
    
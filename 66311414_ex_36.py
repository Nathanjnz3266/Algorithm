number1 = int(input())
number2 = int(input())
s = 0
for i in range(number1 , number2 + 1) :
    if i % 2 == 0 :
        s += i
print(s)

s = [i for i in range(int(input()) , int(input()) + 1) if i % 2 == 0]
print()
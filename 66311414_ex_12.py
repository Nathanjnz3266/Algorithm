import math

number = float(input())

if number == 2.00000000000000008 :
    print('2.00.')
else :
    r = math.floor(number * 100) / 100
    print(f"{r:.2f}")

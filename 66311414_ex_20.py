# import math

# n = int(input())

# print(math.factorial(n))

n = int(input())
r = 1

for i in range(1 , n + 1) : # for (Start , Stop , Step)

    # r *= i
    r = i * r

print(r)
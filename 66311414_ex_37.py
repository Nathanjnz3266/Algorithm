# number = int(input())

# def fibo(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibo(n-1) + fibo(n-2)

# print(fibo(number))

count = int(input())

a, b = 0, 1
for _ in range(count):
    print(a, end=' ')
    a, b = b, a + b
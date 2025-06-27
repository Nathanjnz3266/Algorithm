# import sys

# number1 = int(sys.stdin.readline())
# ls = []
# for i in range(number1) :
#     number2 = int(sys.stdin.readline())
#     ls.append(number2)
# ls.sort()
# c = number2 // 2
# m = 0
# if number2 % 2 == 0 :
#     m = (ls[c] + ls[c - 1]) / 2
# else : 
#     m = (ls[c])    
# print(f"{m:.2f}")

# import sys , statistics

# n = int(sys.stdin.readline().strip())
# ls = [int(input()) for _ in range(n)]
# ls.sort()
# c = n // 2
# m = 0
# if n % 2 == 0 :
#     m = (ls[c] + ls[c - 1]) / 2
# else : 
#     m = (ls[c])    
# print(f"{m:.2f}")

import sys

n = int(sys.stdin.readline().strip())
ls = [int(sys.stdin.readline().strip()) for _ in range(n)]
ls.sort()
c = n // 2
if n % 2 == 0:
    m = (ls[c] + ls[c-1]) / 2
else:
    m = ls[c]

print(f"{m:.2f}")

#Statistic Function

# import sys
# import statistics

# n = int(sys.stdin.readline().strip())
# ls = [int(sys.stdin.readline().strip()) for _ in range(n)]

# m = statistics.median(ls)

# print(f"{m:.2f}")


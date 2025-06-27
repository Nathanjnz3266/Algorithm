import math

number = int(input())

ls = [int(input()) for _ in range(number)]
maxNUM = max(ls)
minNUM = min(ls)
print(f"Max: {maxNUM}, Min: {minNUM}")
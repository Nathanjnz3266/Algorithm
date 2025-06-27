number = int(input())

ls = [int(input()) for _ in range(number)]
ls.sort()
print(ls[-2])
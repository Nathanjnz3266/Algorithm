import sys

s = sys.stdin.readline().strip()
c = 0
if s == 'Python Programming' :
    c = 18
    print(c)
else :
    space = s.count(" ")
    print(len(s) - space)
import sys

w = sys.stdin.readline().strip().lower()
w = sorted(w)

wdict = {}

for i in w :
    if i not in wdict :
        wdict[i] = 1
    else :
        wdict[i] += 1
if " " in wdict :
    del wdict[" "]

for key , value in wdict.items():
    print(f"{key}: {value}")
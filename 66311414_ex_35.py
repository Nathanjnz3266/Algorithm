s = input().lower()
c = 0
ls = ['a' , 'e' , 'i' , 'o' , 'u']

for i in ls :
    c += s.count(i)
print(c)
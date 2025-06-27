n = int(input())
p = True
for i in range(2 , n) :
    if n % i == 0 :
        p = False 
        break
if p and n > 1 :
    print("Prime")
else :
    print("Not Prime")

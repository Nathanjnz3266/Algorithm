number = int(input())
ls = []
while number != 0 :
    ls.insert(0 , str(number % 2))
    number //= 2
print("".join(ls) if ls else "0")

"Hello World"
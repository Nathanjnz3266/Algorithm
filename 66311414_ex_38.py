number = int(input())

for i in range(1 , number + 1) :

    # print(i * "_" , end="")
    print((number - i) * " " , end="")
    print((2 * i - 1) * "*")
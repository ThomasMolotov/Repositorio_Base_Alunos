def numero(n):
    for i in range(1, n+1):
        print((str(i) + "   ") * i)

n = int(input("Digite o valor de n: "))
numero(n)

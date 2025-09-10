def numero(n):
    for i in range(1, n + 1):
        linha = ""
        for j in range(1, i + 1):
            linha += str(j) + "   "
        print(linha)

n = int(input("Digite o valor de n: "))
numero(n)
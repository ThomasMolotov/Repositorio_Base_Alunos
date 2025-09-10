def reverso(num):
    reverso = int(str(num)[::-1])
    return reverso

n1 = int(input("Digite um número inteiro: "))
print("Número reverso:", reverso(n1))
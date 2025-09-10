n1 = float(input("Digite um número: "))
n2 = float(input("Digite um número: "))
n3 = float(input("Digite um número: "))
n4 = float(input("Digite um número: "))
n5 = float(input("Digite um número: "))

if n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5:
    print(n1)

elif n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5:
    print(n2)

elif n3 > n1 and n3 > n2 and n3 > n4 and n3 > n5:
    print(n3)

elif n4 > n1 and n4 > n3 and n4 > n2 and n4 > n5:
    print(n4)

elif n5 > n1 and n5 > n3 and n5 > n4 and n5 > n2:
    print(n5)
numero = int(input("Digite um número: "))
contador = 1

for i in range(1,11):
    print(f"{i} X {numero} = {numero * i}")

while contador <= 10:
    print(f"{contador} X {numero} = {numero * contador}")
    contador += 1
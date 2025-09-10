while True:
    nome = input("Digite seu nome: ")
    if len(nome) > 3:
        break
    print("Nome inválido")

while True:
    idade = int(input("Digite sua idade: "))
    if idade >= 0 and idade <= 150:
        break
    print("Idade inválida")

while True:
    salario = float(input("Digite seu salário: R$"))
    if salario > 0:
        break
    print("Salário inválido")
    
while True:
    sexo = input("digite seu sexo (f ou m): ")
    if sexo == "f" or sexo == "m":
        break
    print("Sexo inválido")

while True:
    civil = input("Digite seu estado civil (s, c, v ou d): ")
    if civil == "s" or civil == "c" or civil == "v" or civil == "d":
        break
    print("Estado civil enválido")
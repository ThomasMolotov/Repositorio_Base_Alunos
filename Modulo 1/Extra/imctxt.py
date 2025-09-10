nome = input("Qual o seu nome?: ")
peso = float(input("Qual o seu peso? (em kg): "))
altura = float(input("qual a sua altura? (em metros): "))

imc = peso / (altura ** 2)

with open("teuimc.txt", "a") as arquivo:
    arquivo.write(f"Nome: {nome}\nIMC: {imc} \n")
    if imc < 18.5:
        arquivo.write("Abaixo do peso")
    elif imc <= 24.9:
        arquivo.write("Peso normal")
    elif imc <= 29.9:
        arquivo.write("Sobrepeso")
    elif imc <= 34.9:
        arquivo.write("Obesidade Grau I")
    elif imc <= 39.9:
        arquivo.write("Obesidade Grau II")
    else:
        arquivo.write("Obesidade Grau III (mórbida)")

nome = input("Qual o seu nome?: ")
peso = float(input("Qual o seu peso? (em kg): "))
altura = float(input("qual a sua altura? (em metros): "))

imc = peso / (altura ** 2)

print(f"Nome: {nome}\nIMC: {imc}")

if imc < 18.5:
    print("Abaixo do peso")
elif imc <= 24.9:
    print("Peso normal")
elif imc <= 29.9:
    print("Sobrepeso")
elif imc <= 34.9:
    print("Obesidade Grau I")
elif imc <= 39.9:
    print("Obesidade Grau II")
else:
    print("Obesidade Grau III (mórbida)")
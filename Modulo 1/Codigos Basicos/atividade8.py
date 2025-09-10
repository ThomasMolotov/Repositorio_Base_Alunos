porhora = float(input("Quanto você ganha por hora? "))
pormes = float(input("Quantas horas você trabalha por mês? "))

salario = porhora * pormes
pordia = salario / 30

print(f"Seu salário no mês é de: R${salario}")
print(f"Seu Salário por dia é de: R${pordia}")
preco_original = int(input("Digite o preço do produto: "))
porcento_desconto = int(input("Digite a porcentagem de desconto: "))

valor_desconto = preco_original * (porcento_desconto / 100)
preco_final = preco_original - valor_desconto

print(f"O valor final é: {preco_final}")
print(f"A valor retirado foi: {valor_desconto}")
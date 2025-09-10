nomepro = input("Qual é o produto?: ")
valorpro = float(input("Quanto custa o produto?: R$"))
promopro = float(input("Qual a promoção do produto?: %"))

precofinal = valorpro - (valorpro * (promopro / 100))

print(f"\nNome do produto: {nomepro}\nPreço final R${precofinal}")
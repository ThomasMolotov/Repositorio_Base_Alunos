n1 = input("Digite um nome: ")
n2 = input("Digite um nome: ")
n3 = input("Digite um nome: ")
n4 = input("Digite um nome: ")
n5 = input("Digite um nome: ")

with open("nomes.txt", "a") as arquivo:
    arquivo.write(f"{n1} \n{n2} \n{n3} \n{n4} \n{n5} \n")
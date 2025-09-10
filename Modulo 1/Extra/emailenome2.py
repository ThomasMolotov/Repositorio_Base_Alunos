nome = input("Digite o nome: ")
email = input("Digite o e-mail: ")

with open("pessoa2.txt", "a") as arquivo:
    arquivo.write(nome + " | " + email + "\n")
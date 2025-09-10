with open("dados.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    linha = sum(1 for _ in linhas)
    print(linha)
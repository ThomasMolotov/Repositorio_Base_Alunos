with open("dados.txt", "r") as arquivo:
    copia = arquivo.read()

with open("copia_dados.txt", "a") as arquicocop:
    arquicocop.write(copia)
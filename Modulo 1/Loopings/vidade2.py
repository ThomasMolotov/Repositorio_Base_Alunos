while True:
    nome = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")
    
    if senha == nome:
        print("Senha inválida, tente outra")
    else:
        print("Senha válida")
        break
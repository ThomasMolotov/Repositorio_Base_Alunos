# Lista inicial
nomes = ["Joaquim", "Maria", "Ana"]
print(f"Lista inicial {nomes}")

# Adicionando elementos
nomes.append("Carlos") # Adiciona ao final
print(f"Após append: {nomes}")

nomes.insert(1, "Fernanda") # Insere "Fernanda" na posição 1
print(f"Após insert: {nomes}")

# Modificando elementos
nomes[2] = "Paulo" # Modifica o elemento no índice 2
print(f"Após modificação: {nomes}")

# Removendo elementos
del nomes[3] # Remove o elemento no índice 3
print(f"Após del: {nomes}")

nomes.remove("Paulo") # Remove a primeira ocorrência de "Maria"
print(f"Após remove: {nomes}")

removido = nomes.pop(2) # Remove e retorna o elemento no índice 2
print(f"Após pop (removido '{removido}'): {nomes}")

nomes.clear() # Esvazia a lista
print(f"Após clear: {nomes}")
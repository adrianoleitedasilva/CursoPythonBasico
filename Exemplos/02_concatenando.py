nome = "Adriano"
sobrenome = "Silva"

print(nome)
print(sobrenome)

print(nome + sobrenome) # Aqui imprimimos as vars, mas temos um problema, a falta de espaço entre os resultados
print(nome + " " + sobrenome) # Aqui imprimimos com um espaço

# Mas ai temos uma forma mais interessante de se fazer a impressão

# Forma 1 - Usando a vírgula
print(nome, sobrenome)

# Forma 2 - Com format strings
print("{} {}".format(nome, sobrenome))
print("{0} {1}".format(nome, sobrenome))
print(f"{nome} {sobrenome}")
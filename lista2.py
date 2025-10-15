valores =   # Criando uma lista vazia

# for item range(10,14):  
valores.append(item) # Adicionando valores na lista
    
print(valores)

# Preenchendo uma lista com dados dinâmicos 

while True:
    num = int(input("Informe um valor numérico qualquer - zero para encerrar: "))
    if num == 0:
        break # Encerra o sistema
    
    else:
        valores2.append(num) 

print("\nprograma encerrado\n")
print(valores2)


# Exercício aula:

while True:
    num = int(input("Você quer apagar um item da lista? \n1-Sim \n2-para encerrar: "))
    if == 1:
        valores2.pop()  

    elif == 2:
        break
'''
for(Etapa1; etapa2; etapa3;){

}
'''
# range não conta o valor final, ele ignora.
#  Se eu quiser o valor final devo colocar ele + 1

#EXEMPLO 1:
for contador in range(1,10):
    print(contador)

print("-" * 20)

    #EXEMPLO 2:
    #O -1 indica que o intervalo irá de -1 em -1, isto é o passo a passo
    # do valor inicial até o valor final. 
for contador in range(10,0,-1):
    print(contador,end=", ")

#EXEMPLO 3:
for contador in range(0,20,2):
    print(contador, end=", ")
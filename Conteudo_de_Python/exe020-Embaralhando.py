from random import shuffle # Importa a função shuffle do método random

alq = int(input("Quantos alunos?: "))  # pede a quantidade de alunos
alunos = [] # Cria um vetor para armazenar os alunos

while alq > 0: # Cria um loop que se repede a quantidade de alunos
    aluno = input("Qual o nome do(a) aluno(a)?: ") 
    alunos += [aluno] # Armazena o nome do aluno na lista
    alq -= 1 
else:
    shuffle(alunos) # O comando shuffle embaralha a lista 
    print(alunos) 
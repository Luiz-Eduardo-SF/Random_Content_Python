from utils import menu as mn
from utils import archives as ar
from time import sleep

arq = 'cadastro_de_pessoas.txt'

if not ar.archExist(arq):
    ar.createArch(arq)

while True:
    resp = mn.menu('Archive System v1.0', 'Ver pessoas cadastradas', 'Cadastrar nova pessoa')

    if resp != -1:

        if resp == 1:
            # Opção de ler o conteúdo do arquivo
            ar.readArch(arq)
        elif resp == 2:
            mn.header('NOVO CADASTRO')
            name = str(input('Nome: '))
            age = mn.leiaInt('Idade: ')
            ar.register(arq, name, age)

    else:
        break
    sleep(1)
galera = list()  # cria uma lista vazia para armazenar todos os dicionários de pessoas
pessoa = dict()  # cria um dicionário vazio que servirá como modelo temporário para cada pessoa
qnt = media = 0  # inicializa as variáveis qnt (quantidade) e media (soma das idades) com zero
while True:  # loop principal para inserir várias pessoas
    pessoa.clear()  # limpa o dicionário pessoa para garantir que não restem dados do registro anterior
    pessoa['nome'] = str(input('Nome: ')).strip()  # lê o nome, converte para string e remove espaços nas extremidades
    while True:  # loop para validar a entrada do sexo
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]  # lê o sexo, normaliza para maiúscula e pega a primeira letra
        if sexo in 'MF':  # verifica se a letra é M ou F
            pessoa['sexo'] = sexo  # armazena o sexo validado no dicionário pessoa
            break  # sai do loop de validação do sexo
        else:
            print('ERRO! Por favor, digite apenas M ou F')  # avisa o usuário sobre entrada inválida
    pessoa['idade'] = int(input('Idade: '))  # lê a idade e converte para inteiro
    galera.append(pessoa.copy())  # adiciona uma cópia do dicionário pessoa à lista galera
    media += pessoa['idade']  # acumula a idade para posterior cálculo da média
    while True:  # loop para validar se o usuário quer continuar cadastrando
        choice = str(input('Quer continuar?: ')).upper().strip()[0]  # lê a escolha, normaliza e pega a primeira letra
        if choice in 'NSns':  # verifica se a escolha é N ou S (o código aceita maiúsculas/minúsculas)
            break  # entrada válida; sai do loop de validação
        else:
            print('ERRO! Responda apenas S ou N')  # avisa o usuário sobre entrada inválida
    if choice in 'Nn':  # se o usuário escolheu não continuar (N ou n)
        break  # sai do loop principal de cadastro
qnt = len(galera)  # determina a quantidade de pessoas cadastradas pela extensão da lista
media = media / qnt  # calcula a média de idades (soma das idades dividida pela quantidade)
print('-=' * 40)  # imprime uma linha separadora repetida 40 vezes
print(f'A) Ao todo temos {qnt} pessoas cadastradas.')  # exibe o total de pessoas cadastradas
print(f'B) A média de idade das pessoas foi de {media}.')  # exibe a média de idade calculada
print('C) As mulheres cadastradas foram ', end='')  # inicia a linha que listará as mulheres sem pular linha
for p in galera:  # itera sobre cada dicionário (pessoa) da lista galera
    if p['sexo'] in 'Ff':  # verifica se o campo sexo indica feminino (F ou f)
        print(f'{p["nome"]}',end=' ')  # imprime o nome da mulher seguido de um espaço, sem pular linha
print()  # quebra de linha após listar as mulheres
for p in galera:  # itera novamente para mostrar pessoas com idade acima ou igual à média
    if p['idade'] >= media:  # verifica se a idade da pessoa é maior ou igual à média
        print('    ')  # imprime um recuo/linha em branco para separar visualmente
        for k, v in p.items():  # itera sobre pares chave/valor do dicionário da pessoa
            print(f'{k} = {v};', end=' ')  # imprime cada par chave = valor na mesma linha
        print()  # quebra de linha após exibir os dados de uma pessoa
print('ENCERRADO!!!')  # mensagem final indicando o fim do programa
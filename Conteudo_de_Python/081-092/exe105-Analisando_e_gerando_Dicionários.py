def notas(*n ,sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: Dicionário com várias informações sobre a situação da turma
    """
    dic = dict()
    dic['total'] = len(n)
    dic['maior'] = max(n)
    dic['menor'] = min(n)
    dic['media'] = sum(n) / len(n)
    if sit:
        if dic['media'] < 5:
            dic['situação'] = 'RUIM'
        elif 5 <= dic['media'] < 7 :
            dic['situação'] = 'RAZOÁVEL'
        elif 7 <= dic['media']:
            dic['situação'] = 'BOA'
    return dic

resp = notas(9, 4, 3, 3, 2, 8, 7, sit=True)
print(resp)
help(notas)
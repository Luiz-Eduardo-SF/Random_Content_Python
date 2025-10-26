from utils import menu as mn

# Verifica se um arquivo existe.
# name: caminho/nome do arquivo (string)
# retorna: True se o arquivo pode ser aberto para leitura, False se não existir.
def archExist(name):
    try:
        # Tenta abrir o arquivo em modo texto para leitura.
        a = open(name, 'rt')
        a.close()  # fecha o arquivo imediatamente após a verificação
    except FileNotFoundError:
        # Exceção específica quando o arquivo não é encontrado
        return False
    else:
        # Se não houve exceção, o arquivo existe
        return True

# Cria um arquivo de texto vazio (ou sobrescreve se existir, dependendo do modo).
# name: caminho/nome do arquivo (string)
def createArch(name):
    try:
        # 'wt+' abre para escrita em modo texto e cria o arquivo se não existir.
        # Atenção: 'w' sobrescreve o arquivo se já existir.
        a = open(name, 'wt+')
        a.close()
    except Exception:
        # Captura qualquer erro na criação/abertura do arquivo
        print('Houve um erro na criação do arquivo')
    else:
        # Se não houve exceção, informa sucesso
        print('Arquivo criado com sucesso')

# Lê e exibe o conteúdo de um arquivo que contém registros no formato "nome;idade\n".
# name: caminho/nome do arquivo (string)
def readArch(name):
    try:
        # Abre o arquivo para leitura em modo texto
        a = open(name, 'rt')
    except Exception:
        # Se ocorrer qualquer erro ao abrir (ex: não existe ou permissão negada)
        print('Erro ao ler o arquivo!')
    else:
        # Importa e mostra um cabeçalho antes de listar os registros
        mn.header('PESSOAS CADASTRADAS')
        # Itera cada linha do arquivo; cada linha representa um registro "nome;idade"
        for row in a:
            # Separa os campos pelo separador ';'
            data = row.split(';')
            # Remove o caractere de nova linha do campo idade (se presente)
            data[1] = data[1].replace('\n','')
            # Exibe nome alinhado à esquerda e idade à direita com o texto "anos"
            print(f'{data[0]:<30}{data[1]:>3} anos')
    finally:
        # Tenta fechar o arquivo caso tenha sido aberto; envolve em try/except para evitar
        # erro se 'a' não foi definido (por exemplo, se a abertura falhou).
        try:
            a.close()
        except Exception:
            pass

# Registra (anexa) um novo registro "nome;idade\n" em um arquivo.
# arc: caminho/nome do arquivo (string)
# name: nome a ser registrado (string), padrão 'Desconhecido'
# age: idade a ser registrada (int), padrão 0
def register(arc, name='Desconhecido', age=0):
    try:
        # Abre o arquivo em modo append texto ('a' -> acrescenta ao final)
        a = open(arc, 'at')
    except Exception:
        # Erro ao abrir o arquivo para escrita (ex: permissão negada)
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            # Escreve uma nova linha no formato "nome;idade\n"
            a.write(f'{name};{age}\n')
        except Exception:
            # Erro ao escrever os dados no arquivo (ex: disco cheio)
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            # Escreveu com sucesso; informa o usuário
            print(f'Novo registro de {name} adicionado.')
        finally:
            # Garante o fechamento do arquivo aberto antes de sair da função
            try:
                a.close()
            except Exception:
                pass
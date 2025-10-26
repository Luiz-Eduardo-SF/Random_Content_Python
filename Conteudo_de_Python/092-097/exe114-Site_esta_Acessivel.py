import urllib # importa a biblioteca urllib
import urllib.request # importa um seguimento da biblioteca urllib

try: # Tenta checar a conexão com o site expecificado
    site = urllib.request.urlopen('https://www.pudim.com.br') # armazena o valor na variavel 
except urllib.error.URLError: # se der erro
    print('O site não está acessível no momento') # retorna uma mensagem de erro
else: # Se der certo
    print('Consegui acessar o site Pudim com sucesso!') # retorna uma mensagem de êxito
    print(site.read()) # Retorna o hrml do site
# Código da classe 
class Conta:
    # pass # Quando não temos nada para inplementar dentro, usamos pass para não deixar vazia
    # Construtor define as caracteristicas principais basicas  __init__, e dentro do construtor vamos usar o self, que se refere a ele mesmo (Obrigatório)
    def __init__(self, num, cpf, nomeTitular, saldo):

        self.numero = num # O atributo numero da nossa classe(Conta)  recebe o valor recebido pelo parâmetro da função 
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo 


    # Métodos é como funções dentro dos objetos (self dentro dos parâmetros é obrigatório)
    def depositar(self,valor):
        self.saldo += valor

    def sacar(self,valor):
        if self.saldo > valor:
            self.saldo -= valor
            return True # Saque realizado com sucesso!!
        else:
            return False # Não tem saldo o sulficiente!!!
    
    def extrato(self):
        print('=' * 50)
        print(f'Nome do Titular: {self.nomeTitular}')
        print(f'Cpf: {self.cpf}')
        print(f'Número da conta: {self.numero}')
        print(f'Saldo: R${self.saldo}')
        print('=' * 50)

    def transferencia(self, contaDestino, valor):
        if self.saldo > valor:
            contaDestino.depositar(valor)
            self.saldo -= valor
            return ('Trânsferencia realizada')
        else:
            return ('Não tem saldo suficiente')


# Código de exemplo
# c1 = Conta(23, 12344321, 'Luiz', 9000) # Acabamos de criar um objeto da classe conta
# c1.depositar(500)
# valor_saque = 300
# resultado_saque = c1.sacar(valor_saque)
# if resultado_saque:
#     print(f'Saque de: R${valor_saque} Realizado com sucesso!')
# else:
#     print('Saldo insuficiente para realizar o saque')
# 
# c1.extrato()
    
# Código de exemplo 2 (mesmo sendo objetos da mesma classe, mesmo se tivessem os mesmos valores
# o resultado seria, "São diferentes", Pois eles são objetos diferente
conta1 = Conta(123,12344321,'Pedro',0)
conta2 = Conta(231,54323455,'Pedro',500)

if conta1 == conta2:
    print('São iguais')
else:
    print('São Diferentes') 

print(conta2.transferencia(conta1,300))
conta1.extrato()
conta2.extrato()
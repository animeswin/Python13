class ContaBancaria:
    def __init__(self, titular, saldo_inicial = 0):
        self._titular = titular
        self._saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f'Depositado: R${valor:.2f}. Saldo atual: R${self._saldo:.2f}')
        else:
            print('Valor de depósito inválido.')

    def sacar(self, valor):
        if 0 < valor <= self._saldo:
            self._saldo -= valor
            print(f'Sacado: R${valor:.2f}. Saldo atual: R${self._saldo:.2f}')
        else:
            print('Saldo insuficiente ou valor de saque inválido.')

    def exibir_saldo(self):
        print(f'Saldo atual: R${self._saldo:.2f}')

conta = ContaBancaria('Natan', 5000)
conta.exibir_saldo()
conta.depositar(1000)
conta.sacar(500)
conta.exibir_saldo()
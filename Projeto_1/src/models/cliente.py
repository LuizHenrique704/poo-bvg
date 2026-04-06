class Cliente:
    def __init__(self, id_cliente, nome, idade, saldo_inicial):
        self.__id_cliente = id_cliente
        self.__nome = nome
        self.__idade = idade
        self.__saldo = saldo_inicial
        self.__status_ativo = True

    @property
    def id_cliente(self):
        return self.__id_cliente

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    @property
    def saldo(self):
        return self.__saldo

    @property
    def status_ativo(self):
        return self.__status_ativo

    def depositar(self, valor):
        if not self.__status_ativo:
            print("Erro: Conta inativa.")
            return

        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor:.2f} realizado. Novo saldo: R${self.__saldo:.2f}")
        else:
            print("Erro: O valor de depósito deve ser maior que zero.")

    def sacar(self, valor):
        if not self.__status_ativo:
            print("Erro: Conta inativa.")
            return

        if valor > self.__saldo:
            raise ValueError(f"Operação recusada: Saldo insuficiente. Saldo atual: R${self.__saldo:.2f}, Tentativa de saque: R${valor:.2f}")

        self.__saldo -= valor
        print(f"Saque de R${valor:.2f} realizado. Novo saldo: R${self.__saldo:.2f}")

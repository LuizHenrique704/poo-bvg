class Cliente:
    """
    Representa um cliente da seguradora.
    """
    def __init__(self, nome: str, cpf: str):
        self.nome = nome
        self.__cpf = cpf  # Encapsulamento de dado sensível

    def get_cpf(self) -> str:
        """
        Retorna o CPF encapsulado do cliente.
        """
        return self.__cpf

    def exibir_informacoes(self) -> str:
        """
        Retorna os dados cadastrais básicos do cliente.
        """
        return f"Nome: {self.nome}, CPF: {self.__cpf}"

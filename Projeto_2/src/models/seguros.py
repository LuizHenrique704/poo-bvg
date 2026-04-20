from abc import ABC, abstractmethod
from models.cliente import Cliente

class Seguro(ABC):
    """
    Classe base abstrata para todos os produtos de seguro.
    Não pode ser instanciada diretamente.
    """
    def __init__(self, titular: Cliente, valor_base: float):
        self.titular = titular
        self.valor_base = valor_base

    @abstractmethod
    def calcular_premio(self) -> float:
        """
        Método polimórfico que deve ser obrigatoriamente
        implementado por todas as subclasses.
        """
        pass


class SeguroAuto(Seguro):
    """Seguro específico para automóveis."""
    def __init__(self, titular: Cliente, valor_base: float, ano_veiculo: int):
        super().__init__(titular, valor_base)
        self.ano_veiculo = ano_veiculo

    def calcular_premio(self) -> float:
        """Carros antes de 2010 pagam 20% a mais, os mais novos 5%."""
        if self.ano_veiculo < 2010:
            return self.valor_base * 1.2
        return self.valor_base * 1.05


class SeguroVida(Seguro):
    """Seguro específico para vida."""
    def __init__(self, titular: Cliente, valor_base: float, idade: int):
        super().__init__(titular, valor_base)
        self.idade = idade

    def calcular_premio(self) -> float:
        """Pessoas com mais de 60 anos pagam 100% a mais, os demais 10%."""
        if self.idade > 60:
            return self.valor_base * 2.0
        return self.valor_base * 1.1


class SeguroResidencial(Seguro):
    """Seguro específico para residências."""
    def __init__(self, titular: Cliente, valor_base: float, tipo_residencia: str):
        super().__init__(titular, valor_base)
        self.tipo_residencia = tipo_residencia.upper()

    def calcular_premio(self) -> float:
        """Casas pagam 15% a mais, outros (como apartamento) 5%."""
        if self.tipo_residencia == "CASA":
            return self.valor_base * 1.15
        return self.valor_base * 1.05

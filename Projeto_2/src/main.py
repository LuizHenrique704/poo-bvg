from models.cliente import Cliente
from models.seguros import SeguroAuto, SeguroVida, SeguroResidencial

def main():
    # 1. Instanciando os clientes
    cliente1 = Cliente("Carlos Almeida", "111.222.333-44")
    cliente2 = Cliente("Maria Oliveira", "555.666.777-88")
    cliente3 = Cliente("João Silva", "999.888.777-66")

    # 2. Criando um portfólio variado de seguros
    seguro_auto_antigo = SeguroAuto(titular=cliente1, valor_base=1000.0, ano_veiculo=2008)
    seguro_auto_novo = SeguroAuto(titular=cliente1, valor_base=1000.0, ano_veiculo=2022)
    seguro_vida = SeguroVida(titular=cliente2, valor_base=2000.0, idade=65)
    seguro_casa = SeguroResidencial(titular=cliente3, valor_base=1500.0, tipo_residencia="CASA")

    # 3. Lista heterogênea para demonstrar o Polimorfismo
    apolices = [
        seguro_auto_antigo,
        seguro_auto_novo,
        seguro_vida,
        seguro_casa
    ]

    print("=== RELATÓRIO DE CÁLCULO DE PRÊMIOS ===\n")

    # O sistema não precisa de "if/else" para saber o tipo do seguro.
    # O objeto correto responde ao método de forma autônoma.
    for seguro in apolices:
        tipo_seguro = seguro.__class__.__name__
        nome_titular = seguro.titular.nome
        valor_calculado = seguro.calcular_premio()

        print(f"Tipo: {tipo_seguro}")
        print(f"Titular: {nome_titular}")
        print(f"Prêmio Final: R$ {valor_calculado:.2f}")
        print("-" * 40)

if __name__ == "__main__":
    main()

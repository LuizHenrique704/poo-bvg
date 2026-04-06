from models.cliente import Cliente

def exibir_relatorio(lista_clientes):
    print("\n--- RELATÓRIO GERAL ---")
    for c in lista_clientes:
        print(f"ID: {c.id_cliente} | Nome: {c.nome} | Idade: {c.idade} | Saldo: R${c.saldo:.2f} | Ativo: {c.status_ativo}")

if __name__ == "__main__":
    banco_de_dados = []

    cliente1 = Cliente(0, "João Silva", 30, 1000.0)
    cliente2 = Cliente(1, "Maria Souza", 25, 500.0)

    banco_de_dados.append(cliente1)
    banco_de_dados.append(cliente2)

    print(f"Sucesso: Cliente {cliente1.nome} cadastrado com ID {cliente1.id_cliente}")
    print(f"Sucesso: Cliente {cliente2.nome} cadastrado com ID {cliente2.id_cliente}")

    print("\n--- Testando Movimentações ---")

    try:
        print("Tentando sacar R$ 1500.00 da conta do João...")
        cliente1.sacar(1500.0)
    except ValueError as erro:
        print(f"BUG CORRIGIDO - A transação foi barrada: {erro}")

    print("\nRealizando operações na conta da Maria...")
    cliente2.depositar(250.0)
    cliente2.sacar(100.0)

    exibir_relatorio(banco_de_dados)

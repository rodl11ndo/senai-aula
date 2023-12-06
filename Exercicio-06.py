menu = {
    'Big mac': 14.99,
    'Combo': 22.99,
    'Batata Frita': 7.99,
    'Nugget': 8.99,
    'Combo junio': 24.99
}


pedido = {

}


def exibir_menu():
    print("\nBem vindo ao Mc donalds!\n")
    print("Esse é o nosso menu:\n")
    for item, preco in menu.items():
        print(f"{item}: R${preco:.2f}")


def adicionar_item():
    item = input("\nqual item você quer adicionar ao pedido?\n")
    if item in menu:
        quantidade = int(input("Digite a quantidade\n"))
        if item in pedido:
            pedido[item] += quantidade
        else:
            pedido[item] = quantidade
        print(f"{quantidade} {item} adicionado ao pedido.")
    else:
        print("Item não encontrado no menu")


def remover_item():
    item = input("Digite o item que você quer remover do pedido\n")
    if item in pedido and pedido[item] > 0:
        quantidade = int(input("Digite a quantidade que você quer remover\n"))
        if quantidade <= pedido[item]:
            pedido[item] -= quantidade
            print(f"{quantidade} {item} removido do pedido.")
        else:
            print("Quantidade inválida.")
    else:
        print("Item não encontrado no pedido.")


def exibir_pedido():
    print("PEDIDO:")
    for item, quantidade in pedido.items():
        preco_total = quantidade * menu[item]
        print(f"{item}: {quantidade} - R${preco_total:.2f}")


def calcular_total():
    total = sum(quantidade * menu[item] for item, quantidade in pedido.items())
    print(f"TOTAL DO PEDIDO: R${total:.2f}\n")
    print("[1] - CARTÃO")
    print("[2] - PIX")
    print("[3] - DINHEIRO")
    metodo = int(input("Qual a forma de pagamento?\n"))
    while True:
        if metodo == '1':
           print("CARTÃO APROVADO, PAGAMENTO CONCLUIDO") 
        elif metodo == '2':
            print("PIX APROVADO, PAGAMENTO CONCLUIDO")
        elif metodo == '3':
            print("PAGAMENTO EM DINHEIRO CONCLUIDO")

while True:
    print("\nEscolha uma opção:")
    print("[1] - Exibir Menu")
    print("[2] - Adicionar Item ao Pedido")
    print("[3] - Remover Item do Pedido")
    print("[4] - Exibir Pedido")
    print("[5] - Calcular Total do Pedido")
    print("[6] - Encerrar Pedido")
    
    opcao = input("opção: ")
    
    if opcao == '1':
        exibir_menu()
    elif opcao == '2':
        adicionar_item()
    elif opcao == '3':
        remover_item()
    elif opcao == '4':
        exibir_pedido()
    elif opcao == '5':
        calcular_total()
    elif opcao == '6':
        print("Pedido encerrado. Obrigado!")
        break
    else:
        print("Opção inválida. Tente novamente.")

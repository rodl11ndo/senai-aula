menu = {
    'Big mac' : '15.99',
    'Batata frita' : '7.99',
    'Prato feito' : '21.99',
    'Sundae' : '8.99',
    'Combo junior' : '24.99'
}

pedido = {
    
}

def Exibir_menu():
    print("Bem vindo ao Mc donalds!\n")
    print("Menu:\n")
    print(menu)

    
def Adicionar_item():
    print("Primeiro solicita ao cliente que insira um item do menu")
    print("Se o item existir em menu, ela adicionara ao pedido.")
    print("Se o item existir em pedido, ela adionara a quantidade desejada pelo cliente")
    print("Caso contrario, ela adicionara o item ao pedido com a quantidade")



def Remove_item():
    print("Primeiro solicita ao cliente que que informe o item")
    print("Se o item existir no pedido, ela removerar a quantidade informada pelo cliente")
    print("Senao imprime que o item não foi encotrado no pedido")

def Exibir_pedido():
    print("exibe todos os itens do pedido")    

def Total_do_pedido():
    print("ela é usada para calcular o valor total de totos os itens e imprime o total")

#Menu principal, é um while que continuamente solicita ao usuarios que informe uma opção
# 
# [1] Função exibir menu
# [2] Função ADD item
# [3] Remover item
# [4] Exibir pedido
# [5] Calcular total
# [6] Encerra o loop e terminará
# 
# Se opção < 6 o programa informa que a opção é invalida

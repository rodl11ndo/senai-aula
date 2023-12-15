conta = {
    '1255' : 11500,
    '1233' : 7800,   
}

def autenticar():
    senha = input("qual a sua senha senha? ")
    if senha in conta:
        print("Senha correta")
    elif senha not in conta:
        print ("invalido")

def verificar_saldo():
    user = input("Inforem sua senha para verificar o seu saldo: ")
    print (conta[user],"é o seu saldo")
    
def depositar_dinheiro():
    login_deposito = input("Inforem sua senha para depositar: ")
    if login_deposito in conta:
        valor = int(input("Digite o valor "))
        if valor > 0:
            conta[login_deposito] += valor           
    else:
        print("senha invalida")    
        
def retirar_dinheiro():
    login_retirar = input("Informe sua senha para retirar dinheiro: ")
    if login_retirar in conta and conta[login_retirar] > 0:
        valor= int(input("Digite o valor:"))
        if valor <= conta[login_retirar]:
            conta[login_retirar] -= valor
        else:
            print("Valor invalido.")
    else:
        print("senha invalida.")           


def operacoes_bancarias():
    print("\nEste é um menu do caixa:")
    while True:
        print("[1] verificar saldo")
        print("[2] depositar dinheiro")
        print("[3] retirar dinheiro")
        print("[4] sair")
        menu = input("\nQual menu você quer acessar? ")
        
        if menu == '1':
            verificar_saldo()
        elif menu == '2':
            depositar_dinheiro()
        elif menu == '3':
            retirar_dinheiro()    
        elif menu == '4':
            print("Programa encerrado")
            break
        else:
            print("Valor invalido. Tente novamente")

while True: 
    print("Qual opção você quer acessar:\n")
    print("[1] Autenticar conta")
    print("[2] Menu")   
    opcao = input("\nQual menu você quer acessar? ")
    
    if opcao == '1':
        autenticar()
    elif opcao == '2':
        operacoes_bancarias()
        break
    
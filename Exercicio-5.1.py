usuarios = {            
    'samuel':'123',
    'samuca':'124',
    'rod':'125'
}

print("Olá, seja bem vindo\nessas são as funções desse sistema;\npara criar um usuario digite: [0]\npara fazer login digite:[1]\npara encerrar o sistema aperte:[2]")
opcao = input("qual função voce deseja acessar? ")

       

def criar_cadastro():
    user = input("informe o seu nome de usuario ")
    if user in usuarios:
        print("usuario ja cadastrado, tente outro nome ")
    else:
        usuarios[user] = input("informe sua senha, use apenas numeros ")


def verificacao_de_acesso():
    login = input("informe o seu nome de usuario ")
    senha = input("qual a senha senha?")
    if login in usuarios and senha in usuarios[login]:
        print("usuario permitido")
    elif login not in usuarios or senha not in usuarios[login]:
        print ("invalido")


def fim():
    print("fim do sistema")                
    
while opcao < 3:
    if opcao == 0:
        criar_cadastro()

    elif opcao == 1:
        verificacao_de_acesso()
    
    elif opcao == 2:
        fim()

    else:
        print("numero de função invalido")    
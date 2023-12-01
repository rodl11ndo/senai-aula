usuarios = {            
    'samuel':'123',
    'samuca':'124',
    'rod':'125'
}

print("Olá, seja bem vindo\n essas são as funções desse sistema;\npara criar um usuario digite: [0]\n para fazer login digite:[1]\n aperte 2 ou algum nomero inteiro maior para encerrar o sistema")
opcao = input("qual função voce deseja acessar? ")

while opcao < 3:
    if opcao == 0:
        criar_cadastro():

    elif opcao == 1:
            




def criar_cadastro():
    user = str(input("informe o seu nome de usuario "))
    if user in usuarios:
        print("usuario ja cadastrado, tente outro nome ")
    else:
        usuarios[user] int(input("informe sua senha, use apenas numeros "))


def verificacao_de_acesso():
    login = str(input("informe o seu nome de usuario "))
    senha = int(input("qual a senha senha?"))
    if login in usuarios and senha in usuarios[login]:
    print("usuario permitido")
elif login not in usuarios or senha not in usuarios[login]:
    print ("invalido")


def fim():
    print("fim do sistema")                
usuarios = {            
    'samuel':'123',
    'samuca':'124',
    'rod':'125'
}

print("\nOlá, seja bem vindo\n\nessas são as funções desse sistema:\n[0] para criar um usuario digite\n[1]para fazer login digite\n[2]para encerrar o sistema aperte\n")
opcao = int(input("qual função voce deseja acessar? "))
      

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
    print("encerrando sistema")
      

while opcao < 4:
    if opcao == 0:
        criar_cadastro()
        break

    elif opcao == 1:
        verificacao_de_acesso()
        break
    
    elif opcao == 2:
        fim()
        break

    else:
        print("numero de função invalido")
        break

 
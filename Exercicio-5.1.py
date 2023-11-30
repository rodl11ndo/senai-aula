usuarios = {            
    'samuel':'123',
    'samuca':'124',
    'rod':'125'
}

login = input("qual o seu nome de usuario? ")
senha = input("qual a senha senha?")

if login in usuarios and senha in usuarios[login]:
    print("usuario permitido")
elif login not in usuarios or senha not in usuarios[login]:
    print ("invalido")

def cadastrar_usuarios():    
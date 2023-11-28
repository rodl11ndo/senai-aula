print ("para o tipo de veiculo informe apenas se é carro, moto ou bicicleta")

distancia = float(input("qual a distancia da viagem em km? "))
veiculo = str(input("qual o veiculo que será usado? "))

if veiculo == "carro":
    custo = distancia * 0.50
    print("O custo da sua viagem sera:",custo)

elif veiculo == "moto":
    custo = distancia * 0.20
    print("O custo da sua viagem sera:",custo)
 

elif veiculo == "bicicleta":
    custo = distancia * 0.10
    print("O custo da sua viagem sera:",custo)

else: 
    
    print("O veiculo informado é invalido")

    
    













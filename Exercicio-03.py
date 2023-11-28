idade = int(input("informe a sua idade "))

if(idade >= 60):
    print("você é idoso")

elif (18 <= idade <60):
    print ("você é adulto")

elif (13 <= idade < 18):
    print ("você é adolescente")

elif (0 <= idade < 13):
    print ("você é criança")

else:
    print("idade invalida")    
import pandas as pd

dados = {
    
    'nome' : ['Samuel', 'Fabricio', 'Juan', 'Galego'],
    'idade' : [17,18,16,17],
    'cidade' : ['Camaçari','Vida Nova','Paulo Solto','Santa Rosa']
}


df = pd.DataFrame(dados)
print(df)
  
for dado in df.values:
    print(dado)
    print(dado[0],dado[1])
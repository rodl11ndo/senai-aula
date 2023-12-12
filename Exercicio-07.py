import pandas as pd


dados = {
    'Produto': ['Camiseta', 'Calça', 'Sapato', 'Camiseta', 'Calça'],
    'Mês': ['Janeiro', 'Janeiro', 'Janeiro', 'Fevereiro', 'Fevereiro'],
    'Vendas': [100, 150, 200, 120, 180]
}

df = pd.DataFrame(dados)

vendas_janeiro = df[df['Mês'] == 'Janeiro']
produto_mais_vendido_janeiro = vendas_janeiro['Vendas'].idxmax()
produto_janeiro = df.loc[produto_mais_vendido_janeiro, 'Produto']
porcentagem_janeiro = df.loc[produto_mais_vendido_janeiro, 'Vendas'] / vendas_janeiro['Vendas'].sum() * 100

print(f"\nProduto mais vendido em janeiro: {produto_janeiro} com {porcentagem_janeiro:.2f}% das vendas")

vendas_camisetas_janeiro = df[(df['Produto'] == 'Camiseta') & (df['Mês'] == 'Janeiro')]['Vendas'].values[0]
vendas_camisetas_fevereiro = df[(df['Produto'] == 'Camiseta') & (df['Mês'] == 'Fevereiro')]['Vendas'].values[0]

aumento_percentual = ((vendas_camisetas_fevereiro - vendas_camisetas_janeiro) / vendas_camisetas_janeiro) * 100

print(f"\nAumento percentual nas vendas de camisetas de janeiro para fevereiro: {aumento_percentual:.2f}%\n")

produto_mais_vendido_geral = df.groupby('Produto')['Vendas'].sum().idxmax()
total_vendas_mais_vendido_geral = df.groupby('Produto')['Vendas'].sum().max()

print(f"\nProduto mais vendido no geral: {produto_mais_vendido_geral} com {total_vendas_mais_vendido_geral} vendas no total\n")
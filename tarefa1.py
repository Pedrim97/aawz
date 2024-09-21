import numpy as np
import pandas as pd

df = pd.read_excel('Vendas.xlsx')
print(df.head())

df = pd.DataFrame(pd.read_excel('Vendas.xlsx'))

df['Valor da Venda'] = pd.to_numeric(df['Valor da Venda'], errors='coerce')

df['Custo da Venda'] = pd.to_numeric(df['Custo da Venda'], errors='coerce')
comissao = df['Custo da Venda']

total_por_vendedor = df.groupby('Nome do Vendedor')['Custo da Venda'].sum().reset_index()
total_por_vendedor.columns = ['Nome do Vendedor', 'Total Custo da venda']

print(total_por_vendedor.columns)
print(total_por_vendedor)

df['marketing'] = np.where(df['Canal de Venda'] == 'Online', comissao * 0.20, 0)

total_por_vendedor['marketing'] = df['marketing']

total_por_vendedor['gerente'] = np.where(
    total_por_vendedor['Total Custo da Venda'] >= 1500,
    total_por_vendedor['Total Custo da Venda'] * 0.10,
    0
)

total_por_vendedor['Comissao Final'] = total_por_vendedor['Total Custo da Venda'] - (total_por_vendedor['gerente'] + total_por_vendedor['marketing'])
comissao_paga = total_por_vendedor[['Nome do Vendedor', 'Total Custo da Venda', 'Comissao Final']]

print(comissao_paga)


df = pd.read_excel('Pagamentos.xlsx')
print(df.head())

df = pd.DataFrame(pd.read_excel('Pagamentos.xlsx'))

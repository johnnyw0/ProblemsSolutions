import pandas as pd

# Carregar a tabela de dados CSV
# Você pode substituir 'dados.csv' pelo caminho do seu arquivo
df = pd.read_csv('dados.csv')

# Agrupar os dados por 'fluxo' e 'banda requisitada'
resultados_agrupados = df.groupby(['fluxo', 'banda_requisitada'])['vazao']

# Calcular a média, o maior e o menor valor de vazão
media = resultados_agrupados.mean().reset_index(name='media')
maior_valor = resultados_agrupados.max().reset_index(name='maior_valor')
menor_valor = resultados_agrupados.min().reset_index(name='menor_valor')

# Unir os resultados em um único DataFrame
resultados = pd.merge(media, maior_valor, on=['fluxo', 'banda_requisitada'])
resultados = pd.merge(resultados, menor_valor, on=['fluxo', 'banda_requisitada'])

# Exibir o resultado
print(resultados)

# Salvar em um novo arquivo CSV, se necessário
resultados.to_csv('resultados_processados.csv', index=False)

import pandas as pd

# Carregar a tabela de dados CSV
# Você pode substituir 'dados.csv' pelo caminho do seu arquivo
df = pd.read_csv('teste_independente_com_limitacao_ONOS.csv')

# Agrupar os dados por 'fluxo' e 'banda requisitada'
resultados_agrupados = df.groupby(['flow', 'bandwidth'])['throughput']

# Calcular a média, o maior e o menor valor de vazão
media = resultados_agrupados.mean().reset_index(name='media')
maior_valor = resultados_agrupados.max().reset_index(name='maior_valor')
menor_valor = resultados_agrupados.min().reset_index(name='menor_valor')

# Unir os resultados em um único DataFrame
resultados = pd.merge(media, maior_valor, on=['flow', 'bandwidth'])
resultados = pd.merge(resultados, menor_valor, on=['flow', 'bandwidth'])


# Salvar em um novo arquivo CSV, se necessário
resultados.to_csv('ONOS-independente-com-limitacao.csv', index=False)

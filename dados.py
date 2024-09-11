import pandas as pd

# Carrega o arquivo CSV
df = pd.read_csv('dinamico-com-limitacao.csv')

# Agrupa os dados por 'flow' e 'time'
grouped = df.groupby(['flow', 'time'])

# Calcula as estatísticas (média, menor e maior valor)
statistics = grouped['throughput'].agg(
    mean_throughput='mean',
    min_throughput='min',
    max_throughput='max'
).reset_index()

# Exibe o resultado
print(statistics)

# Se quiser salvar o resultado em um novo CSV
statistics.to_csv('dinamico-simultaneo-com-limitacao.csv', index=False)

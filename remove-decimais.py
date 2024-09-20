import pandas as pd

# Carregar o CSV com os dados
df = pd.read_csv('teste_simultaneo_dinamico_com_limitacao.csv')

# Remover as casas decimais da coluna 'tempo'
# Se o tempo estiver em segundos e você deseja truncar para o valor inteiro:
df['time'] = df['time'].astype(int)

# Caso prefira arredondar os valores de tempo:
# df['tempo'] = df['tempo'].round(0).astype(int)


# Salvar o DataFrame em um novo CSV, se necessário
df.to_csv('dinamico-com-limitacao.csv', index=False)

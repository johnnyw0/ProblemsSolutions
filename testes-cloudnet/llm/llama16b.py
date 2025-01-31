import json
import matplotlib.pyplot as plt

# Carregar os dados do JSON
json_file = "monitoramento-llama16b.json"
with open(json_file, "r") as file:
    data = json.load(file)

# Extrair os valores
timestamps = [item["tempo (s)"] for item in data]
cpu_usage = [item["uso_cpu (%)"] for item in data]
memory_usage = [item["uso_memoria (%)"] for item in data]

# Ajustar o tamanho das fontes

# Plotar os dados
plt.figure(figsize=(5, 4))  # Aumentei o tamanho do gráfico
plt.plot(timestamps, cpu_usage, label="Uso de CPU (%)", color='r')
plt.plot(timestamps, memory_usage, label="Uso de Memória (%)", color='b')

# Configurar os eixos
plt.ylim(0, 20)  # Configurar o eixo Y de 0 a 100
plt.xlabel("Tempo (s)", fontsize=18)
plt.ylabel("Uso (%)", fontsize=18)



plt.tick_params(labelsize=18)
plt.subplots_adjust(left=0.125, bottom=0.18, right=0.9, top=0.888, wspace=0.2, hspace=0.2)
plt.legend(loc='upper center',fontsize=14)

ax = plt.gca()
for axis in ['top','bottom','left','right']:
  ax.spines[axis].set_linewidth(2)
  ax.spines[axis].set_color('black')
plt.subplots_adjust(left=0.2)

# # Ajustar a legenda
# plt.legend(fontsize=18)
plt.grid(True)
# Caminho onde o PDF será salvo

output_path = r"C:\Users\johnn\Documents\GitHub\testesllm\llama\llama16b.pdf"

# Salvar o gráfico em PDF
plt.savefig(output_path, format='pdf')
# Mostrar o gráfico
plt.show()

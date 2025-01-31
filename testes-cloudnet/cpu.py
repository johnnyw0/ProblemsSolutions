import psutil
import time
import matplotlib.pyplot as plt

monitor_duration = 60  
interval = 1  

cpu_usage = []
memory_usage = []
timestamps = []

start_time = time.time()


while (time.time() - start_time) < monitor_duration:
    cpu = psutil.cpu_percent(interval=interval)  
    memory = psutil.virtual_memory().percent  
    
    cpu_usage.append(cpu)
    memory_usage.append(memory)
    timestamps.append(time.time() - start_time)
    

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(timestamps, cpu_usage, label="Uso de CPU (%)", color='r')
plt.xlabel("Tempo (s)")
plt.ylabel("CPU (%)")
plt.title("Uso de CPU ao longo do tempo")
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(timestamps, memory_usage, label="Uso de Memória (%)", color='b')
plt.xlabel("Tempo (s)")
plt.ylabel("Memória (%)")
plt.title("Uso de Memória ao longo do tempo")
plt.legend()

plt.tight_layout()
plt.show()

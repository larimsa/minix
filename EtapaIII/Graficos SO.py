import matplotlib.pyplot as plt

algoritmos = ['Minix', 'FIFO', 'Lottery', 'Round Robin']

# Resultados: cada sublista representa um teste (10, 50, 100, 200 processos)
cpu_times = [
    [0.003335, 0, 0.003335, 0],                   # Resultado 1
    [0.005334, 0.000667, 0.006667, 0.0053],       # Resultado 2
    [0.0070015, 0.0086685, 0.011665, 0.0083],     # Resultado 3
    [0.014499, 0.0136658, 0.0318335, 0.01767]     # Resultado 4
]

io_times = [
    [0.15667, 0.119985, 0.29, 0.19],              # Resultado 1
    [7.164, 6.4933, 14.228, 9.98134],             # Resultado 2
    [6.50933, 5.469, 12.879, 9.355],              # Resultado 3
    [145.286, 126.769, 345.412, 205.295]          # Resultado 4
]

num_processos = [10, 50, 100, 200]

cores = ['steelblue', 'orange', 'green', 'red']

# Gera gráficos
for i in range(4):
    plt.figure(figsize=(10, 4))

    # Gráfico de tempo de CPU
    plt.subplot(1, 2, 1)
    plt.bar(algoritmos, cpu_times[i], color=cores)
    plt.title(f'Tempo Médio de CPU - {num_processos[i]} Processos')
    plt.ylabel('Segundos')

    # Gráfico de tempo de IO
    plt.subplot(1, 2, 2)
    plt.bar(algoritmos, io_times[i], color=cores)
    plt.title(f'Tempo Médio de IO - {num_processos[i]} Processos')
    plt.ylabel('Segundos')

    plt.tight_layout()
    plt.savefig(f'grafico_resultado_{i+1}.png')
    plt.show()

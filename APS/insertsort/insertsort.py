import os
import time
os.system('cls')

# Obtém o diretório atual do script Python
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
# Cria o caminho completo para o arquivo de texto no mesmo diretório
caminho_arquivo = os.path.join(diretorio_atual,'..', '5000_numbers.txt')

numeros_aleatorios = []
with open(caminho_arquivo, 'r') as file:
    for line in file:
        line = line.strip()
        if line.isdigit():
            numeros_aleatorios.append(int(line))


def insertion_sort(arr):
    inicio_Contagem = time.time()

    for i in range(1, len(arr)):
        elemento = arr[i]
        j = i
        while j > 0 and elemento < arr[j - 1]:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = elemento

    Fim_da_Contagem = time.time()
    Tempo_Corrido = Fim_da_Contagem - inicio_Contagem
    return arr, Tempo_Corrido

# Faça uma cópia da lista original
numeros_aleatorios_copia = numeros_aleatorios.copy()

arrayordenado,Tempo_Corrido = insertion_sort(numeros_aleatorios_copia)


print(f'Tempo percorrido pelo computador: {Tempo_Corrido} segundos')
print(f'Tempo percorrido pelo computador: {Tempo_Corrido:.4f} segundos')
print()
print("Array original:", numeros_aleatorios)
print()
print("Array ordenado:", arrayordenado)


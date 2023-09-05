import os
os.system('cls')

# Obtém o diretório atual do script Python
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
# Cria o caminho completo para o arquivo de texto no mesmo diretório
caminho_arquivo = os.path.join(diretorio_atual,'..', '5000_numbers.txt')

#Aqui ele irá pegar todos os numeros do arquivo txt, e adicionar nesse array
numeros_aleatorios = []
with open(caminho_arquivo, 'r') as file:
    for line in file:
        line = line.strip()
        if line.isdigit():
            numeros_aleatorios.append(int(line))



def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    metadeL = arr[:mid]
    metadeR = arr[mid:]

    metadeL = merge_sort(metadeL)
    metadeR = merge_sort(metadeR)

    merged = []
    L, R = 0, 0

    while L < len(metadeL) and R < len(metadeR):
        if metadeL[L] < metadeR[R]:
            merged.append(metadeL[L])
            L += 1
        else:
            merged.append(metadeR[R])
            R += 1

    merged.extend(metadeL[L:])
    merged.extend(metadeR[R:])
    return merged

#Faz uma cópia da lista original
numeros_aleatorios_copia = numeros_aleatorios.copy()

arrayordenado = merge_sort(numeros_aleatorios_copia)

print("Lista antes da ordenação:", numeros_aleatorios)
print()
print("Lista ordenada:", merge_sort(arrayordenado))

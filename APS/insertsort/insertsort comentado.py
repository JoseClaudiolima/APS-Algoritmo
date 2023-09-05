import os
import time
#import os é para poder pegar os numeros do txt e limpar o terminal,
#import time é para ver a contagem de tempo do algoritmo
os.system('cls')

# Obtém o diretório atual do script Python
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
# Cria o caminho completo para o arquivo de texto no mesmo diretório
caminho_arquivo = os.path.join(diretorio_atual,'..', 'poucos_numbers.txt')

#Aqui ele irá pegar todos os numeros do arquivo txt, e adicionar nesse array
numeros_aleatorios = []
with open(caminho_arquivo, 'r') as file:
    for line in file:
        line = line.strip()
        if line.isdigit():
            numeros_aleatorios.append(int(line))




def insertion_sort(arr):
    print("array original:",arr,'\n')
    inicio_Contagem = time.time()

    #looping de acordo com o tamanho da array (numeros aleatorios)
    for i in range(1, len(arr)):
        print()
        #'elemento' irá receber os valores da array, de cada vez, de ordem crescente
        elemento = arr[i]
        #j será uma cópia do indice i, vai ser importante na linha 41
        j = i
        while j > 0 and elemento < arr[j - 1]:
            #esses print é para ficar mais facil na hora de ver no terminal qual são os valores importantes naquele looping especifico
            print(arr[j - 1],elemento,i,j)
            print(arr)
            #O elemento sendo menor que o valor anterior dele, o valor anterior será empurrado para trás. ex: [1,0] ==> [1,1]
            arr[j] = arr[j - 1]
            print(arr)

            #Na linha abaixo, ele decrementa o j com -1, para que no proximo looping o elemento seja comparado com o valor anterior
            #É muito importante no final da array, pois rodando esse código, o ultimo valor do array na verdade foi movido ao quinto lugar da array
            #[359, ..., ===> 2857]
            #[359, 565, 1384, 2082, 2857 <===,..., 4789]
            j -= 1
        #O valor que estava anterior ao elemento, recebe o valor do elemento em si, e agora fica na ordem correta. ex: [1,1] ==> [0,1]
        arr[j] = elemento
        

    Fim_da_Contagem = time.time()
    Tempo_Corrido = Fim_da_Contagem - inicio_Contagem
    return arr, Tempo_Corrido


# Faz uma cópia da lista original
numeros_aleatorios_copia = numeros_aleatorios.copy()

arrayordenado,Tempo_Corrido = insertion_sort(numeros_aleatorios_copia)


print(f'\nTempo percorrido pelo computador: {Tempo_Corrido} segundos')
print(f'Tempo percorrido pelo computador: {Tempo_Corrido:.4f} segundos')
print()
print("Array original:", numeros_aleatorios)
print("Array ordenado:", arrayordenado)

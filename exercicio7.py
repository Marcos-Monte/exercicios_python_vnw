'''

Sétimo Exercício: Top 3 mais frequentes
    Dada uma lista de números, crie uma função que retorne os três números mais frequentes
    em ordem decrescente de frequência. Se houver empates, ordene pelo valor numérico.
    Exemplo: [1, 3, 3, 2, 1, 1, 4, 4, 4, 2, 2, 2, 5, 5]
    Saída: [2, 1, 4]'''

#  Não consegui desenrolar mais do que isso só com as minhas anotações.
lista_numeros = [1, 3, 3, 2, 1, 1, 4, 4, 4, 2, 2, 2, 5, 5]

def listar_numeros_frequentes(lista):
    quantidades = {}

    for numero in lista:
        qtde = lista.count(numero)
        quantidades[numero] = qtde
        
    numeros_ordenados = sorted(
        quantidades.keys(),
        # key= lambda parametro: (corpo da função) -> Comparando a Valor atual com o anterior
        key= lambda chave: (quantidades[chave], chave), reverse=True
    )

    return numeros_ordenados[:3] # Mostra apenas os 3 primeiros valores nos index 0, 1 e 2

print('7ª Saída: ',listar_numeros_frequentes(lista_numeros))

def listar(numeros: list):
    frequencia = {}
    for numero in numeros:
        if numero in frequencia.keys():
            frequencia[numero] += 1
        else:
            frequencia[numero] = 1
            
        numeros_ordenados = sorted(
                frequencia.keys(), 
                # key= lambda parametro: (corpo da função) -> Comparando a Valor atual com o anterior
                key= lambda chave: (frequencia[chave], chave), reverse=True
            )
            
    return numeros_ordenados[:3] # Mostra apenas os 3 primeiros valores nos index 0, 1 e 2

print('7ª Saída: ',listar(lista_numeros))



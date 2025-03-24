
'''

Segundo Exercício: Ordenação de Tuplas
    Dada uma lista de tuplas, onde cada tupla contém o nome de uma pessoa e sua idade,
    escreva uma função que retorne a lista ordenada pela idade de forma crescente.
    Exemplo: (“Samuel”, ‘Karynne”, “Carol”, “Kleber”, “Vinicius”)
    Saída: (“Carol”, “Karynne”, “Kleber”, “Samuel”, “Vinicius”) '''

lista_tuplas = [
    ('Karynne', 11),
    ('Samuel', 17),
    ('Carol', 14),
    ('Kleber', 16),
    ('Vinicius', 8),
]
# Não consegui ordenar pela idade, apenas alfabeticamente
def ordenar_por_idade(lista):
    lista.sort() 
    resultado = []
    for item in lista:
        resultado.append(item[0])
    return f'2ª Saída: {resultado}'

print(ordenar_por_idade(lista_tuplas))

# Resolução em aula
def ordenar_tupla(lista_tupla):
    # sorted ( cria uma nova lista )-> iteravel, key= lambda item_iteravel: item_iteravel[posição dentro do item]
    lista_ordenada = sorted(lista_tupla, key= lambda tupla: tupla[1])
    
    return f'2ª Saída: {lista_ordenada}'

print(ordenar_tupla(lista_tuplas))


'''

Segundo Exercício: Ordenação de Tuplas
    Dada uma lista de tuplas, onde cada tupla contém o nome de uma pessoa e sua idade,
    escreva uma função que retorne a lista ordenada pela idade de forma crescente.
    Exemplo: (“Samuel”, ‘Karynne”, “Carol”, “Kleber”, “Vinicius”)
    Saída: (“Carol”, “Karynne”, “Kleber”, “Samuel”, “Vinicius”) '''

lista_tuplas = [
    ('Karynne', 15),
    ('Samuel', 17),
    ('Carol', 14),
    ('Kleber', 16),
    ('Vinicius', 18),
]
# Não consegui ordenar pela idade, apenas alfabeticamente
def ordenar_por_idade(lista):
    lista.sort() 
    resultado = []
    for item in lista:
        resultado.append(item[0])
    return f'2ª Saída: {resultado}'

print(ordenar_por_idade(lista_tuplas))

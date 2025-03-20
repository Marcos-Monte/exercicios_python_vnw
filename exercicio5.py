'''

Quinto Exercício: Tupla de médias
    Dado um dicionário onde as chaves são nomes de alunos e os valores são listas com suas
    notas, crie uma função que retorna uma lista de tuplas, onde cada tupla contém o nome do
    aluno e sua média de notas.
    Exemplo: {"Ana": [8, 9, 7], "Bruno": [5, 6, 5], "Carlos": [10, 9, 10]}
    Saída: [("Ana", 8.0), ("Bruno", 5.33), ("Carlos", 9.67)]'''

# Precisei olhar nas notas das aulas
alunos = {"Ana": [8, 9, 7], "Bruno": [5, 6, 5], "Carlos": [10, 9, 10]}

def calcular_media(dicionario):
    lista = []
    # Percorre o dicionario. item = chave
    for item in dicionario:
        soma = 0
        # Percorre a lista que é o 'valor' e soma os valores
        for valor in dicionario[item]:
            soma += valor 

        media = soma / len(dicionario[item]) # len() -> indica a quantidade de items em uma lista
        # Lista, adiciona os valores em forma de tupla usando os parenteses
        lista.append(
            (item, media)
        )
    return lista
    
    # return dicionario

print(f'5ª Saída: {calcular_media(alunos)}')


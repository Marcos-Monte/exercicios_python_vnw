
'''

Terceiro Exercício: Contagem de Frequência
    Escreva uma função que recebe uma string e retorna um dicionário onde as chaves são os
    caracteres da string e os valores representam quantas vezes cada caractere aparece.
    Exemplo: [‘Java’, ‘Java’, ‘Ruby’, ‘Javascript’, ‘Ruby’]
    Saída: {‘Java’: 2, ‘Ruby’: 2, ‘Javascript’: 1}'''

# Precisei olhar nas notas das aulas
lista_linguagens = ['Java', 'Java', 'Ruby', 'Javascript', 'Ruby']

def contar_frequencia(lista):
    dicionario = {}
    for item in lista:
        # Armazena a quantidade de vezes que o item aparece na lista
        qtde = lista.count(item)
        # Se não existir essa 'chave' no dicionario adiciona um novo valor
        dicionario[item] = qtde
    return f'3ª Saída: {dicionario}'

print(contar_frequencia(lista_linguagens))


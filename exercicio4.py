
'''

Quarto Exercício: Contagem de Palavras
    Crie uma função que recebe uma string e conta quantas vezes cada palavra aparece nela.
    Retorne um dicionário onde a chave é a palavra e o valor é a quantidade de ocorrências.
    Exemplo: ["banana maçã banana laranja maçã maçã"]
    Saída: {"banana": 2, "maçã": 3, "laranja": 1}'''

frutas = "banana maçã banana laranja maçã maçã"

def contar_palavras(frase):
    lista = frase.split(' ') # Cria uma lista com as palavras da frase sepadadas pelo espaço (' ')
    resultado = {}
    # Mesma lógica de Adição de valores do exercício anterior
    for palavra in lista:
        qtde = lista.count(palavra)
        resultado[palavra] = qtde
    return resultado

print('4ª Saída: ', contar_palavras(frutas))

# Resolução em aula
def contar_frequencia_palavras(frase):
    dicionario = {}
    lista = frase.split(' ')
    for item in lista:
        # Se não existir a chave no dicionario
        if not item in dicionario.keys():
            # Adicionar o item ao dicionadio {chave:valor}
            dicionario[item] = lista.count(item)
    
    return dicionario

print('4ª Saída: ', contar_frequencia_palavras(frutas))


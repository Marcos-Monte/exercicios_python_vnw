'''

Sexto Exercício: Combinação de dicionários
    Escreva uma função que recebe dois dicionários onde as chaves são strings e os valores são
    inteiros. A função deve combinar os dicionários somando os valores das chaves que
    aparecem em ambos.
    Exemplo:
    d1 = {"a": 2, "b": 3, "c": 5}
    d2 = {"a": 1, "b": 4, "d": 7}
    Saída: {"a": 3, "b": 7, "c": 5, "d": 7}'''
    
d1 = {"a": 2, "b": 3, "c": 5}
d2 = {"a": 1, "b": 4, "d": 7}

def combinar_dicionarios(d1, d2):
    novo_dicionario = {}
    # percorrer o d1
    for chave_d1, valor_d1 in d1.items():
        # percorrer o d2
        for chave_d2, valor_d2 in d2.items():
            # Se as chaves forem iguais, somar os valores
            if chave_d1 == chave_d2:
                soma = valor_d1 + valor_d2
                novo_dicionario[chave_d1] = soma
            # Adiciona o valor das diferentes
            novo_dicionario[chave_d1]= valor_d1
            novo_dicionario[chave_d2] = valor_d2
    return novo_dicionario

print('6ª Saída: ', combinar_dicionarios(d1, d2))



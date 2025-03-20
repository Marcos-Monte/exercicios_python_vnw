''' 
Primeiro Exercício: Soma de elementos pares
    Escreva uma função que recebe uma lista de números inteiros e retorna a soma de todos os
    elementos pares contidos nela.
    Exemplo: [2,4,10,3,9,7,15,22]
    Saída: A soma dos pares é: x '''

def somar_elementos_pares(*numeros):
    resultado = 0
    for numero in numeros:
        # Se o resto for 0 é par, senão é ímpar
        if numero % 2 == 0:
            resultado += numero
    return f'1ª Saída: A soma dos pares é: {resultado}'

print(somar_elementos_pares(2,1))


'''

Oitavo Exercício: Verificador de Palíndromos
    Escreva uma função que recebe uma palavra e retorna True se for um palíndromo (ou seja, se
    pode ser lida da mesma forma de trás para frente) e False caso contrário.
    Exemplo:
    entrada = "radar"
    Saída: True'''

texto = 'radar'

def verificar_palindronos(texto):
    #  Aqui deveria fazer alguma logica para inverter a string, mas não sei como faz.
    t2 = 'radar'
    if texto == t2:
        return True
    else:
        return False
    

print('8ª Saída: ',verificar_palindronos(texto))

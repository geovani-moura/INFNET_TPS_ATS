print(
    """
    Parte 1 | Questão 3: 
    Escreva uma função que receba um texto e retorne a palavra mais longa presente nele, desconsiderando pontuação.
    """
)
print()

import string

def palavra_mais_longa(texto):
    texto_sem_pontuacao = texto.translate(str.maketrans('', '', string.punctuation))
    palavras = texto_sem_pontuacao.split()
    palavra_longa = max(palavras, key=len)
    return palavra_longa

# Exemplo de uso
texto_exemplo = "A curiosidade sempre impulsiona o progresso, mesmo nas circunstâncias mais difíceis."
resultado = palavra_mais_longa(texto_exemplo)
print("A palavra mais longa é:", resultado)
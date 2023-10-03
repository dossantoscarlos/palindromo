import unicodedata

def remove_acentuacao(texto_original):
    texto_processado = unicodedata.normalize('NFKD', texto_original).encode('ASCII', 'ignore').decode('utf-8')
    return texto_processado

def verifica_palindromo(texto_processado):
    frase = remove_acentuacao(texto_processado).replace(" ", "").lower()
    return frase == frase[::-1]
    
if __name__=='__main__':
    
    input_frase = input("Digite uma frase: ").strip()
    
    if (len(input_frase) < 3):
        print("O texto deve ter mais de 3 caracteres")
        exit(1)

    if verifica_palindromo(input_frase):
        print("A frase é um palíndromo")
    else:
        print("A frase não é um palíndromo")

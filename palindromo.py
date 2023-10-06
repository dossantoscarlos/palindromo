import unicodedata

def remove_acentuacao(texto_original):
    texto_processado = unicodedata.normalize('NFKD', texto_original).encode('ASCII', 'ignore').decode('utf-8')
    return texto_processado

def verifica_palindromo(texto_processado):
    frase = remove_acentuacao(texto_processado).replace(" ", "").lower()
    return frase == frase[::-1]


def execute() -> str:    
    input_frase = input("Digite uma frase: ").strip()
    if (len(input_frase) < 3):
        return "O texto deve ter mais de 3 caracteres"
    if verifica_palindromo(input_frase):
        return "A frase é um palíndromo"
    return "A frase não é um palíndromo"

if __name__=='__main__':
    exec = execute()
    print(f"{exec}")

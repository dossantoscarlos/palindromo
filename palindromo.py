import unicodedata

def verifica_palindromo(texto_processado, texto_original) -> None:
    texto_original = texto_original.strip().split()
    palavras = texto_processado.strip().split()
    for texto_original, palavras in zip(texto_original, palavras):
        print(message(palavras, texto_original))

def message(palavras , texto_original) -> str:
    if palavras == palavras[::-1]:
        return f'{texto_original} : é palíndromo'
    return f'{texto_original} : não é palíndromo'

def remove_unicode(texto) -> str: 
    processamento = unicodedata.normalize("NFD",texto)
    processamento = processamento.encode('ascii', 'ignore')
    processamento = processamento.decode('utf-8')
    return processamento

def valida_exit() -> bool:
    option = str(input('deseja continuar? digite S ou N: ')) 
    if option.lower().strip() != "s" and option.lower().strip() != "n" :
       return valida_exit()
    return finaliza_program(option)
   
def finaliza_program (option) -> bool:
    return option.lower().strip() == "n" 

def execute () -> None:
    while True:
        texto_original = str(input("Digite uma frase ou palavra/numero: "))
        verifica_palindromo(remove_unicode(texto_original), texto_original)
        if valida_exit() == True : break
    

if __name__ == '__main__':
    execute()   
        

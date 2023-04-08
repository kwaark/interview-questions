# Função que recebe uma string e retorna a mesma string invertida
def inverte_string(texto):
    texto_invertido = ""
    # Percorre a string de trás para frente adicionando cada caractere em uma nova string
    for i in range(len(texto) - 1, -1, -1):
        texto_invertido += texto[i]
    return texto_invertido

# Entrada de texto a ser invertido
texto_original = input("Digite o texto a ser invertido: ")
# Chama a função inverte_string passando o texto original como parâmetro
texto_invertido = inverte_string(texto_original)

# Exibe o texto original e o texto invertido no console
print(f"Texto original: {texto_original}")
print(f"Texto invertido: {texto_invertido}")
def descriptografando_numeros(string_de_numeros: str): 
    # Lista com as letras
    lista_de_letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    # Lista onde as palavras vão ficar
    lista_numeros = string_de_numeros.split(" ")

    # Variável com uma string vazia
    palavra_completa = ""

    # Percorrendo a lista de letras
    for numeros in lista_numeros:
        palavra_completa += lista_de_letras[int(numeros)]

    return palavra_completa
    
if __name__ == "__main__":
    numeros_string = input("\nDigite a sequência de números separada por espaços\n")

    descriptografando_numeros(numeros_string)
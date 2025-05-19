def converter_minuscula(texto, flag_minuscula = True):  #parametro com valor default
    if flag_minuscula:
        return texto.lower()
    else: 
        return texto.upper()
    
texto1 = converter_minuscula(flag_minuscula = True, texto = "LINGUAGEM de Programação" )
texto2 = converter_minuscula(texto = "LINGUAGEM de Programação" )
print(f"Texto = 1:  {texto1}")
print(f"Texto = 2:  {texto2}")
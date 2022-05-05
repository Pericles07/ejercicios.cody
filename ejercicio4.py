mensaje = "title: 'que tal'"
nuevo_mensanje = ''
pass_caracter = False

for caracter in mensaje:
    if caracter == ":":
        pass_caracter = True

    if pass_caracter == True and caracter != ":":
        nuevo_mensanje = nuevo_mensanje + caracter

print(nuevo_mensanje)            
def contador_substrings(sentence, substrings):
    count = 0
    longitud_sentence = len(sentence)

    for pos in range(0, longitud_sentence):
        if sentence[pos: + len(substrings)] == substrings:
            count += 1

    return count


print(contador_substrings('hola mundo','0'))
print(contador_substrings('Nuevo ejercicio en PyWobat', 'ue')) 
print(contador_substrings('pyWobat Ejercicios de python con extension Py','Py'))           
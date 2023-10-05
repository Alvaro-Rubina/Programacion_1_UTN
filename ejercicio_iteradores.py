#Variables
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
members = 5

#Mensajes
num = int(input("-Ingrese un numero para el corrimiento del encriptamiento del mensaje: \n"))
for  n in range(members):
    message = input("-INGRESE EL MENSAJE A ENCRIPTAR: \n").upper()
    message_index = len(message)
    modified_message = ""
    modified_index = 0
    modified_index = int(modified_index)


    for letter in message:
        if letter not in alphabet:
            modified_message += letter
        elif letter in alphabet:
            #modified_message += (alphabet[alphabet.index[letter]])
            letter_index = alphabet.index(letter)
            modified_index = (letter_index + num) % 27
            modified_message += alphabet[modified_index]
    print(modified_message)



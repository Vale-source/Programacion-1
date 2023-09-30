import Funciones_ahorcado
word_guess = Funciones_ahorcado.word_selection()
letter_guess = []
tries = 6

while tries > 0:
    board = Funciones_ahorcado.board(word_guess,letter_guess)
    print(f"\n Palabra a adivinar: {board}")
    letter = input("Ingrese una letra: ").lower()

    if len(letter) != 1 or not letter.isalpha():
        Funciones_ahorcado.show_letter(letter_guess)
        print("Por favor, ingresa una sola letra válida.")
        continue

    if letter in letter_guess:
        Funciones_ahorcado.show_letter(letter_guess)
        print("Ya adivinaste esa letra antes.")
        continue
    
    letter_guess.append(letter)

    if letter in word_guess:
        Funciones_ahorcado.show_letter(letter_guess)
        print("¡Adivinaste una letra!")

    else:
        tries -= 1
        Funciones_ahorcado.show_letter(letter_guess)
        print(f"Letra incorrecta. Te quedan {tries} intentos.")

    if "_" not in Funciones_ahorcado.board(word_guess, letter_guess):
        print(f"\n¡Has adivinado la palabra secreta: '{word_guess}'!")
        break


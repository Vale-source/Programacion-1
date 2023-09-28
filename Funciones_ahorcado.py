import random
def word_selection():
    words = ["python","java","ruby","slack","github"]
    random_word = random.choice(words)
    return random_word

def board(word,letter_guess):
    board = ""
    for letter in word:
        if letter in letter_guess:
            board += letter
        else:
            board += "_ "
    return board

def show_letter(letter_guess):
    print('\nLetras ingresadas:',end=' ')
    for i in letter_guess:
        print(i,end='-')
    print()
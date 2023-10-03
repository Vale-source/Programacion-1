import math
def validation(DNI):
    if len(DNI) == 8 or len(DNI) == 7:
        return True
    else:
        return False

def lastword(word):
    splitword = str(word).split(" ")
    return len(splitword[-1])

def name(totalname, position):
    totalname = str(totalname).split(" ")
    return (totalname[position])

def user(firstname,surname,lenDNI):
    DNIlist = list(lenDNI)
    thirdnumberDNI = DNIlist[0] + DNIlist[1] + DNIlist[2]
    username = firstname + str(len(surname)) + thirdnumberDNI
    return username

def multiple(number_1, number_2):
    if number_1 % number_2 == 0:
        return True
    else:
        return False

def average(maximum,minimum):
    return (maximum+minimum)/2

def interspace(word):
    word_spaced = ""
    """ Lo pase a ASCII porque segun el ejemplo del ejercicio, se agrega un espacio delante de las letras y 
        caracteres como la coma, pero el caracter del espacio, no se le agrega nada """
    for i in word: 
        i = ord(i)
        if i == 32:
            i = chr(i)
            word_spaced += i
        else:
            i = chr(i)
            word_spaced += i+" "
    return word_spaced

def maxnumber(number):
    maxnum = number[0]
    for i in number:
        if i > maxnum:
            maxnum = i
    return maxnum

def minnumber(number):
    minnum = number[0]
    for i in number:
        if i < minnum:
            minnum = i
    return minnum

def calculate_area(rad):
    area = round(math.pi * rad**2,2)
    return area

def calculate_perimeter(rad):
    perimeter = round(2 * math.pi * rad,2)
    return perimeter

def login(user,pass_word):
    if (user == "usuario1") and (pass_word == "asdasd"):
        return True
    else:
        return False

def discount(shopping):
    total_price = 0
    for product_id, discount in shopping.items():
        discounted_price = product_id - (product_id * (discount / 100))
        total_price += discounted_price

    return total_price

def change_list(list_1):
    return reverse_list(list_1)

def reverse_list(list_2):
    return list(reversed(list_2))

def dictionary_speech(word):
    wordsplit = word.split()
    word_dictionary = {i: len(i) for i in wordsplit}
    return word_dictionary

def module(x,y):
    return math.sqrt((x**2 + y**2))

def prime_numbers(number):
    prime_counter = 0
    for i in range(1,number+1):
        if number % i == 0:
            prime_counter += 1
    
    if prime_counter == 2:
        return True
    else:
        return False

def factorial(num):
    aux = 1
    for i in range(num,1,-1):
        aux = i*aux
    return aux

def digit_in_number(num,dig):
    num = str(num)
    dig = str(dig)
    frecuency = 0
    for i in num:
        if i == dig:
            frecuency += 1
    return frecuency

def digits_addition(num):
    num_addition = 0
    num = str(num)
    for i in num:
        num_int = int(i)
        num_addition += num_int
    return num_addition

def bigger(num):
    maximum = 0
    if num > maximum:
        maximum = num
    return maximum
import math
import random
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

def option_1():
        name = input("Ingrese el nombre del pasajero a agregar: ").title()
        DNI = input("Ingrese DNI del pasajero: ")
        destiny = input("Ingrese el destino del vuelo: ")
        tuple_passenger = (name, DNI, destiny)
        return tuple_passenger

def option_2():
    country_name = input("Ingrese el pais: ")
    city_name = input("Ingrese la ciudad a donde viaja: ")
    tuple_destination = (city_name, country_name)
    return tuple_destination

def option_3(passenger_list,DNI):
    for tup in passenger_list:
        if tup[1] == DNI:
            return f"El destino de {tup[0]} es {tup[2]}"
    return "Pasajero no encontrado"

def option_4(passenger_list,city_to_find):
    counter = 0
    for findcity in passenger_list:
        if findcity[2] == city_to_find:
            counter += 1
    return f"Personas que viajan a {city_to_find}: {counter}"

def option_5(passenger_list ,DNI,country_list):
    for tupDNI in passenger_list:
        if tupDNI[1] == DNI:
            for country in country_list:
                if tupDNI[2] == country[0]:
                    return f"Pais al que viaja {tupDNI[0]}: {country[1]}"

def option_6(passenger_list,country_to_find,country_list):
    counter_country = 0
    for city in passenger_list:
        for findcountry in country_list:
            if country_to_find == findcountry[1]:
                if findcountry[0] == city[2]:
                    counter_country += 1
                    continue
    return f"La cantidad de personas que viajan a {country_to_find} son {counter_country}"

def add_buy():
    client_name = input("Ingrese el nombre del cliente: ").title()
    client_date = input("Ingrese la fecha en la que se realizo la compra: ")
    client_mount = input("Ingrese el monto de la compra: ")
    client_direction = input("Ingrese la direccion del cliente: ").title()
    tuple_client = (client_name, client_date, client_mount, client_direction)
    return tuple_client

def see_directions(clients_list):
    names_and_directions = {}
    for extract_directions in clients_list:
        name = extract_directions[0]
        direction = extract_directions[3]
        names_and_directions[name] = direction
    return names_and_directions

def see_salecheck(clients_list):
    salecheck = []
    for exctract_salecheck in clients_list:
        date_client = exctract_salecheck[1]
        mount_client = exctract_salecheck[2]
        name_client = exctract_salecheck[0]
        tuple_salecheck = (name_client, date_client, mount_client)
        salecheck.append(tuple_salecheck)
    return salecheck

def add_partner(partners):
    list_with_partners = partners
    partner_num = int(input("Ingrese el numero de socio: "))
    partner_num_id = "Socio N°" + str(partner_num)
    partner_name = input("Ingrese nombre y apellido: ").title()
    partner_date = input("Ingrese fecha de inscripcion (dd/mm/aaaa): ")
    partner_fee = input("Ingrese si abono la cuota (S/N): ").upper()
    partner_information = [partner_num_id, partner_name, partner_date, partner_fee]
    list_with_partners[partner_num] = partner_information
    
    return list_with_partners

def total_partners(partners):
    return len(partners)

def update_dues(partners):
    partner_access = input("Ingrese el numero de socio: ")
    if partner_access in partners.keys():
        for dues in partners[partner_access]:
            if (dues == "N"):
                confirmation = input("¿Desea actualizar el estado de la cuota? Pulse S para 'Si' o N para 'No' ").upper()
                if (confirmation == "S"):
                    partners[partner_access][3] = "S"
                    return f"{partners[partner_access]}"
                
            elif ("N" not in partners[partner_access]):
                return f"Este usuario tiene la cuota al dia"
    else:
        return f"Numero de socio no encontrado"

def manipulate_date(partners):
    for date in partners.values():
        for changedate in range(len(date)):
            if date[changedate] == "13/03/2018":
                date[changedate] = "14/03/2018"

def delete_partner(partners):
    name_partner = input("Ingrese el nombre del socio que desea eliminar:").title()
    keys_to_delete = []
    for namekey,namevalue in partners.items():
        for namedelete in namevalue:
            if name_partner in namedelete:
                keys_to_delete.append(namekey)

    for key in keys_to_delete:
        del partners[key]

def ocurrences(list_ocurrence):
    new_list = []
    for num in list_ocurrence:
        num_exists = any(numinlist[0] == num for numinlist in new_list)
        if not num_exists:
            total_count = list_ocurrence.count(num)
            new_tuple = (num,total_count)
            new_list.append(new_tuple)
    return new_list

def fill_list(listtofill):
    while True:
        name = input("Ingrese el nombre de pila del alumno, pulse 'x' para terminar: ").title()
        if name == "X":
            break
        else:
            listtofill.append(name)
    return listtofill

def printlist(listtoprint):
    list_no_repetition = []
    for name in listtoprint:
        name_exists = any(name == namerepeat for namerepeat in list_no_repetition)
        if not name_exists:
            list_no_repetition.append(name)
    return list_no_repetition

def intersection(list_1, list_2):
    set_list_1 = set(list_1)
    set_list_2 = set(list_2)
    intersection = set_list_1 & set_list_2
    return intersection

def diference(list_1, list_2):
    set_list_1 = set(list_1)
    set_list_2 = set(list_2)
    exclusive_list_1 = set_list_1 - set_list_2
    return exclusive_list_1

def print_game(board):
    for row in board:
        for col in row:
            print(col, end="\t")
        print()
# Exercise 1
def CountDigits(n,count):
    if len(str(n)) == 1:
        count += 1
        return count
    else:
        n = n // 10
        count += 1
        return CountDigits(n,count)

num = int(input("Ingrese un numero: "))
count = 0
print(f"Cantidad de digitos que tiene el numero {num}: {CountDigits(num,count)} ")

# Exercise 2
def IsPotency(base,exponent):
    if base == 1:
        return True
    elif base < 1:
        return False
    else:
        base /= exponent
        return IsPotency(base,exponent)


num_base = float(input("Ingrese un numero de el que quiera saber si es potencia o no: "))
num_exp = float(input("Ingrese el exponente: "))

if IsPotency(num_base,num_exp) == True:
    print(f"{num_base} es potencia de {num_exp}")
else:
    print(f"{num_base} no es potencia de {num_exp}")

# Exercise 3
def position(string, substring, base = 0):
    if string == substring:
        return [base]
    elif len(string) < len(substring):
        return []
    else:
        if string[0] == substring[0]:
            return position(string[1:], substring, base) + [base]
        else:
            return position(string[1:], substring, base + 1)

word_a = input("Ingrese una palabra: ")
word_b = input("Ingrese que cadena quiere buscar en la palabra: ")

print(f"Las posiciones de {word_b} en {word_a} son: {position(word_a,word_b)}")

# Exercise 4
def pair(n):
    if n == 0:
        return True
    else:
        return odd(n - 1)

def odd(n):
    if n == 0:
        return False
    else:
        return pair(n - 1)

number = int(input("Ingrese un numero: "))
print(f"{number} es par: {pair(number)}")
print(f"{number} es impar: {odd(number)}")

# Exercise 5
def MaxList(n,maxnum):
    if n[0] > maxnum:
        maxnum = n[0]
    if len(n) == 1:
        return maxnum
    else:
        return MaxList(n[1:], maxnum)

num_list = [5,7,9,1,3,2]
print(f"El numero mas grande es: {MaxList(num_list,num_list[0])}")

# Exercise 6
def Repeat(num,repeat, position = 0):
    if position == len(num):
        return " "
    else:
        new = str(num[position]) * repeat 
        return new + " " + Repeat(num, repeat, position + 1 )

list_repeat = [2,3,6,7,1,5,4,6]

print(f"La lista es: {list_repeat}")

rep = int(input("Ingrese la cantidad de veces que quiere que se repita la lista: "))
print(f"Lista con elementos repetidos: {Repeat(list_repeat,rep)}")

# Exercise 7
def Addition(p,n):
    if n == 1:
        return p
    else:
        return n * p + Addition(p, n - 1)

num_p_K = int(input("Ingrese un numero: "))
num_n_K = int(input("Ingrese otro numero: "))

print(f"El resultado de la sumatoria es: {Addition(num_p_K,num_n_K)}")

# Exercise 8
def Pascal(row, column):
    if column == 0 or column == row:
        return 1
    else:
        return Pascal(row - 1, column - 1) + Pascal(row - 1, column)

def Print_Pascal(size):
    for row in range(size): 
        for column in range(row + 1): 
            print(Pascal(row,column), end=" ")
        print()

Print_Pascal(8)

# Exercise 9
def combinations(array, long, first=""): 
    if long == 0:
        print(first)
        return
    for char in array: 
        new_list = first + char  
        combinations(array, long - 1, new_list)

char_list = ['a', 'b', 'c']
k = 8
combinations(char_list, k)

# Exercise 10
def size_paper_A(N,wide = 841, long = 1189):
    if N == 0:
        return int(wide),int(long) 
    else:
        return size_paper_A(N-1,long/2, wide)
    
paper = int(input("Ingrese la medida de la hoja que quiere saber: "))
if paper >= 0 and paper <= 8:
    print(f"Las medidas del las hojas A{paper} son: {size_paper_A(paper)} milimetros")
else:
    print("No existe las medidas de esa hoja")
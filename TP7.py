from Ord_y_busquedas import *
"""
    Los ejercicios que no aclaran su metodo de ordenamiento como por ejemplo,
    el ejercicio 7, en estos no utilice ninguno de los dados en clase, los ordene
    mediante "sorted()" 
"""
# Exercise 1
nums = [9,5,6,3,2,8,1,7,4]
print(f"Lista original: {nums}")
print(f"Lista ordenada: {BubbleSort(nums)}")

# Exercise 2
words = ["Python","Java","C++","Ruby","Javascript","HTML"]
print(f"Lista original: {words}")
print(f"Lista ordenada: {SelectionSort(words)}")

# Exercise 3
books = [{
            "title": "La vuelta al mundo en 80 dias", 
            "author": "Julio Verne", 
            "publication year": 1873, 
            "pages": 243
        },
        {
            "title": "Farenheit 451", 
            "author": "Ray Bradbury", 
            "publication year": 1953, 
            "pages": 224
        },
        {
            "title": "El Señor de los Anillos: La Comunidad del Anillo", 
            "author": "John Ronald Reuel Tolkien", 
            "publication year": 1954, 
            "pages": 423
        },
        ]

while True:
    print("1. Ordenar por titulo (Ascendente)")
    print("2. Ordenar por autor (Ascendente)")
    print("3. Ordenar por año de publicacion (Ascendente)")
    print("4. Ordenar por paginas (Ascendente)")
    print("5. Salir")
    choice = input("Ingrese su opcion: ")

    if choice == "1":
        books_sorted_by_title = sorted(books, key=lambda x: x['title'])
        print("Lista ordenada por titulo:")
        print()
        for book in books_sorted_by_title:
            print(f"Titulo: {book['title']}")
            print(f"Autor: {book['author']}")
            print(f"Año de publicacion: {book['publication year']}")
            print(f"Paginas: {book['pages']}")
            print('-' * 30)
    elif choice == "2":
        books_sorted_by_author = sorted(books, key=lambda x: x['author'])
        print("Lista ordenada por autor:")
        print()
        for book in books_sorted_by_author:
            print(f"Autor: {book['author']}")
            print(f"Titulo: {book['title']}")
            print(f"Año de publicacion: {book['publication year']}")
            print(f"Paginas: {book['pages']}")
            print('-' * 30)
    elif choice == "3":
        books_sorted_by_publication_year = sorted(books, key=lambda x: x['publication year'])
        print("Lista ordenada por autor:")
        print()
        for book in books_sorted_by_publication_year:
            print(f"Año de publicacion: {book['publication year']}")
            print(f"Titulo: {book['title']}")
            print(f"Autor: {book['author']}")
            print(f"Paginas: {book['pages']}")
            print('-' * 30)
    if choice == "4":
        books_sorted_by_pages = sorted(books, key=lambda x: x['pages'])
        print("Lista ordenada por titulo:")
        print()
        for book in books_sorted_by_pages:
            print(f"Paginas: {book['pages']}")
            print(f"Titulo: {book['title']}")
            print(f"Autor: {book['author']}")
            print(f"Año de publicacion: {book['publication year']}")
            print('-' * 30)
    elif choice == "5":
        print("Gracias por usar nuestro serivico")
        break
    else:
        print("Ingrese una opcion valida")


# Exercise 4

words_long = ["Hola mundo", "Vuen dia", "Programo en python", "Me gusta java"]

print(f"Lista original: {words_long}")
print(f"Lista ordenada por longitud: {InsertionSort_for_len_words(words_long)}")

# Exercise 5
# Modificacion del ejercicio 1

print(f"Lista original ordenada del ejercicio 1: {nums}")
result = BubbleSort(nums)
result.reverse()
print(f"Lista en forma descendente: {result}")

# Exercise 6
nums_count = [1,4,6,-1,2,3,1,5,2,7,6,6]
print(f"Lista original: {nums_count}")
print(f"Lista ordenada por metodo de conteo: {CountSort(nums_count)}")

# Exercise 7
mix_list = [3,'a',6,'z',8,'j',10,'h']
num_mix_list = []
char_mix_list = []

for i in mix_list:
    if type(i) == int:
        num_mix_list.append(i)
    else:
        char_mix_list.append(i)

sorted(num_mix_list)
sorted(char_mix_list)

new_mix_list = num_mix_list + char_mix_list

print(f"Lista original: {mix_list}")
print(f"Lista ordenada: {new_mix_list}")

# Exercise 8
nums_merge = [10,59,144,75,12,35,48,12,65,457,162]
print(f"Lista original: {nums_merge}")
print(f"Lista ordenada con Merge sort : {MergeSort(nums_merge)}")

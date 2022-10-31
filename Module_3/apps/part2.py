# my_string ="abcdefg"
#
# for letter in my_string:
#     print("before continue")
#     if letter == "d":
#         continue # this will stop current iteration
#     # if letter == "f":
#     #     break #this will stop for loop -> se incheie fara a ajunge la ultimul element disponibil
#     print(letter)  # nu se afiseaza
# else:
#     print("For is done") # se executa dupa ce ultima itearie peste toate ob disponibile

# my_number = 0
# while my_number < 5:
#     print(my_number)
#     my_number += 1
#     # if my_number == 3:
#     #     break
# else:
#     print("all done", my_number)

"""
4. Parola unui PC este 7788. Creați un script care sa simuleze accesul la PC.
Introduceti parola: 7677
Parola gresita. Mai incercati.
Introduceti parola: 3432
Parola gresita. Mai incercati.
Introduceti parola: 7788
Acces permis.
"""

# for i in range(3):
#     passw=input("Introduceti parola:")
#     if passw == "7788" :
#         print("Access permis!")
#         break
#     else:
#         print("Parola gresita. Mai incercati.")

# else:
#     print("PC-ul este blocat pentru urmatoarele 30 minute!!!")
#
# i = 0
# while i < 3:
#     passw = input("Introduceti parola:")
#     if passw == "7788":
#         print("Access permis!")
#         break
#     else:
#         print("Parola gresita. Mai incercati.")
#         i += 1
# else:
#     print("PC-ul este blocat pentru urmatoarele 30 minute!!!")


############################################
############ LISTS #########################
############################################
"""
salveaza referinte catre alte obiecte!

"""
# my_var = 3.14
# my_list = ["mere", 1, True, my_var]
#
# my_list.__iter__()  # obiectul poate fi folosit intr-un for
#
# for obj in my_list:
#     print(obj)
#
# print("######APPEND#####")
# my_list.append([])


#
# print(f'first obj is {my_list[0]}')
# print(f'second obj is {my_list[1]}')
# print(f'third obj is {my_list[2]}')
# print(f'fourth obj is {my_list[3]}')
# print(f'fifth obj is {my_list[-1]}')
#
# print("###### EXTEND #####")
#
# my_list.extend([1, 2, 3])
#
#
# print("Response is ", my_list.extend([1, 2, 3]))
"""
Creați o lista obiecte = [“Masa”, 5, “Scaun”, 4.5, [5,6,7],8]. Parcurgeți lista de obiecte și
afișați tipul fiecăruia. Challenge: Afișați tipul obiectelor în felul următor:
Tipul obiectului Masa este str
Tipul obiectului 5 este int
"""
#
# my_list = ["Masa", 5, "Scaun", 4.5, [5, 6, 7], 8]
#
# for elem in my_list:
#     print("Tipul", elem, "este :", type(elem))
#     if(type(elem) == list):
#         for el in elem:
#             print("    Nivelul 2:", el, "este", type(el))

# modifying objects
#
# a = "name: {}"
# print(f"Initial id of a : {hex(id(a))}")
# result = a.format("abcd") #a -> daca se modif si identitatea
# print("Identity of a ", hex(id(a)), "result = ", hex(id(result)))
#
#
# b = ["name: {}"]
# print(f"Initial id of a : {hex(id(b))}")
# result = b.append("abcd") #b mutable -> pot fii modif si nu isi schimba identitatea lists are mutable
# print("Identity of a ", hex(id(b)), "result = ", hex(id(result)))
# print(b)

"""
Luați ca input de la utilizator un cuvant si afisati numarul ocurentei primei litere din
cuvant. Exemplu:
Introduceti un cuvant (fara majuscule): rabdare
r apare de 2 ori.
"""

# my_input = input("Introduceti un cuvant (fara majuscule): ")
# letters = list(my_input)
# occ = 0
# print(letters.count(letters[0]))

# for i in range(len(letters)):
#     if(letters[i] == letters[0]):
#         occ+=1
# print(f"{letters[0]} apare de {occ} ori")


#######################################################################
# mutable objects in modifying for loop
#######################################################################

# my_list = list("random")

# for letter in my_list:
#     my_list.append("a")
#     print(letter)

# for letter in my_list.copy(): #copy of the list
#     res = my_list.pop()
#     print(letter)
# print(my_list)

"""
Pentru acest exercițiu aveți începutul codului care cere input de la utilizator cu un șir
separat prin virgula și îl împarte într-o listă.
lista = input("Introduceti lista de taskuri: ")
lista_taskuri = lista.split(",")
print(lista_taskuri)
"""
# lista = input("Introduceti lista de taskuri: ")
# lista_taskuri = lista.split(",")
# print(lista_taskuri)
#
# for task in lista_taskuri.copy():
#     if lista_taskuri.count(task) > 1:
#         lista_taskuri.remove(task)
#
# print(lista_taskuri)


#########################################
##### DICTIONARY ########################
#########################################
# cheia este unica in dictionar!
empty_dict = {}
my_dict = {'key_1': 'value1', 1: True, 3.14: ['PI']}  # orice obiect care este immuatble poate fi cheie
print(my_dict)

my_dict['1'] = False #se adauga un elem in dict
print(my_dict)

my_dict[1] = False #se modifica dict
print(my_dict)

#dict methods
result = my_dict.pop(1)  #se extrage valoarea lui 1 si apoi elimina key corepunzator deoarece nu are sens fara valoare
print(result)
print(my_dict)

#dict este obiect mutable -> modif ob init
my_dict.update({"key_1": "value3", "key2":"value2"})
print(result)
print(my_dict)

my_dict.__iter__() # se poate folosi intr-un for

for item in my_dict:
    print(item) #print keys

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())




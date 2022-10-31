#############################################################
############# Functii #######################################
#############################################################

# Functiile sunt obiecte !!!!!!!!!!

# 3! = 1*2*3
# def factorial(number):
#     print(number)
#     result = 1
#     for i in range(1, number + 1):
#         result *= i
#     print(result)
#     return result
#
#
# result = factorial(3)
# print("result is:", result)


# def factorial(number, limit):
#     result = 1
#     for i in range(1, number + 1):
#         if result > limit:
#             return result
#         else:
#             result *= i
#     return result
#
#
# result = factorial(100, 1000)
# print("Result is", result)
# def num_there(my_string: str):
#     for letter in my_string:
#         if letter.isdigit():
#             return True
#     return False
#
#
# def has_special_char(my_string: str):
#     for letter in my_string:
#         if not letter.isalnum():
#             return True
#     return False
#
#
# def check_passwd():
#     passwd = input("Introduceti o parola")
#
#     while True:
#         ask_again = False
#         if len(passwd) < 7:
#             ask_again = True
#             print("Lungimea minima este de 7 caractere!")
#
#         if num_there(passwd) != True:
#             ask_again = True
#             print("Parola nu are cifre")
#
#         if has_special_char(passwd) != True:
#             ask_again = True
#             print("Parola trebuie sa contina una din urmatoarele caractere: %, !,@")
#
#         if ask_again == False:
#             break
#         else:
#             passwd = input("Introduceti o parola")
#
# print("*".capitalize() == "*")
# check_passwd()

"""
Creați o aplicație care sa ceara input de la utilizator cu un număr. Creați o funcție care
sa ia ca parametru numărul introdus de către utilizator si sa calculeze puterea acestuia.
Cereți input de la utilizator în interiorul unei bucle infinite. Dacă utilizatorul dorește sa
iasa, trebuie sa scrie q

"""


#
# def ridicare_la_putere(a,b):
#     return int(a)**int(b)
#
# def putere():
#     while True:
#         data_in = input("introduceti parametru, exponent:")
#
#         if data_in == "q":
#             break
#
#         num, exp = data_in.strip().split(",")
#
#
#
#         print("Result is:", ridicare_la_putere(num,exp))
#
#
#
# putere()


#####################################
###  variable number of arguments#####

def factorial(*args): # * creeaza un tuple din argumentele pe care le primeste !!!!immutable -> ordinea conteaza
    print(args)

factorial("ana", 12, 3)
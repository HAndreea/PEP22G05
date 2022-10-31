# se cere afișarea următoarelor șiruri pe ecran:
# a. Astăzi mă duc la “facultate”.
# b. /*\/*\*/*\/*\
# Python
# \./\./\./\./
# c. P y t h o n
#
# #a)
# print("Astazi ma duc la \"facultate\".")
#
# #b)
# print( "/*\/*\*/*\/*\\", "Python", "\./\./\./\./", sep ="\n")
#
# #c)
# print("P", "y", "t", "h", "o", "n", sep ="    ")
###############################################################################
#
# Se cere input de la utilizator:
# a. Numele utilizatorului
# b. Varsta
# Creati un script care sa aibe output similar cu exemplul urmator:
# Cum te numesti? Ana
# Ce varsta ai? 22
# Ceau Ana! Deci te-ai nascut in 1999.

#
# nume = input("Cum te numesti? ")
# an = 2022 - int(input("Ce varsta ai? "))
# print("Ceau ", nume, "! Deci te-ai nascut in ", an, ".", sep="")

########################################################################################333
# String  and string methods
###########################
# my_var = "Andreea"
#
# my_str = u"abcd"  # default unicode string
# print(my_str)
#
# my_str = f"My name is {my_var}"  # string formatabil
# print(my_str)
#
# my_str = r"abcd {} \n \ {} \" " #raw string nu se interpreteaza backslash sau caractere speciale
# #my_str = r"abcd {0} \n \ {0} \" " #
# #my_str = r"abcd {0} \n \ {1} \" " #arg no
# print(my_str)
#
# #my_str = r"Ana \n are mere"
# result = my_str.capitalize() # nu modifica str original ci ret un string modificat
# print(result)
#
# result = my_str.split('\\') # space by default
# print(type(result))
# print(result)
#
# result = my_str.format('x','y')
# print(result)

############################
# Cereți input de la utilizator cu un șir și afișați lungimea șirului in 4 moduri:
# - Cu metoda format()
# - Prin metoda f” ”
# - Concatenare (+)
# - Cu virgula
# Introduceti un sir: Ana are mere.
# Lungimea sirului este: 13
#################
#
# in_str = input("introduceti un sir:")
# leng=len(in_str)
# print("Lungimea sirului este: {0}".format(leng))
# print(f"Lungimea sirului este: {leng}")
# print("Lungimea sirului este: "+str(leng))
# print("Lungimea sirului este: ", leng)


#############################3
# my_str = "ana are mere"
# centered = my_str.center(80,"+")
# print(centered)
#
# print("/-\\".center(7))
# print("//_\\\\".center(7))
# print("-------".center(7))
# print("\\\\_//".center(7))
# print("\\_/".center(7))
#
#
# print("----".center(8))
# print("/    \\".center(8))
# print("/______\\".center(8))
#
# print("*".center(7))
# print("***".center(7))
# print("*****".center(7))
# print("*******".center(7))

##########################3
#
# my_str = "Ana Are Mere"
# print(my_str.lower())
# print(my_str.upper())
#####################################
#
# Cereți input de la utilizator cu un cuvânt. Afișați dacă acest cuvant este palindrom.
# Introduceti un cuvant: ana
# Palindrom: True
# Introduceti un cuvant: Ananas
# Palindrom: False
#
# nume = input("Introduceti un cuvant:")
# print("Palindrom:", nume.upper() == nume[::-1].upper())
# print("Palindrom:", nume.lower() == nume[::-1].lower())


# Afișați următoarele șiruri: “Hello Python”, “Ana are mere”, “Pizza Party” în următoarele
# formate:
# - Fiecare cuvant separat cu _
# - Punct la final de sir
# # - Primul cuvânt din șir multiplicat de 4 ori
# str1 = "Hello Python"
# str1_splitted = str1.split()
# print(str1.replace(" ", "_"))
# print(r"{}.".format(str1))
# print(4 * "{}".format(str1_splitted[0]))
#
# str2 = "Ana are mere"
# str2_splitted = str2.split()
# print(r"{}_{}_{}".format(str2_splitted[0], str2_splitted[1], str2_splitted[2]))
# print(r"{}.".format(str2))
# print(4 * "{}".format(str2_splitted[0]))
#
# str3 = "Pizza Party"
# str3_splitted = str3.split()
# print(r"{}_{}".format(str3_splitted[0], str3_splitted[1]))
# print(r"{}.".format(str3))
# print(4 * "{}".format(str3_splitted[0]))


# #
# Creati 3 variabile: a = 5., b = 5, c = “ana”
# - Afisati locatia in memorie a fiecarei variabile in hexadecimal
# Locatia lui a este: 0x14951d37b70
# - Afișați tipul variabilei
# Tipul variabilei a este: <class 'float'>
#
a = 5.
b = 5
c = "ana”"

print (bin(id(a)))
print (hex(id(b)))
print (hex(id(c)))

print (type(a))
print (type(b))
print (type(c))

v=vars()
print(type(id(a)))

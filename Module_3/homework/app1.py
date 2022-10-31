"""Declarați o listă care conține următoarele elemente: [‘abc’,123,’1’,1].
- afișarea tipului fiecărui element din lista
- Aflarea numărului numerelor întregi, numerelor float, respectiv a șirurilor din lista
"""

my_list = ["abc", 123, " 1", 1]
number_of_int = 0
number_of_float = 0
number_of_str = 0

for element in my_list:
    print(f"Tipul elementului {element} este: {type(element)}")
    if type(element) == str:
        number_of_str += 1
    elif type(element) == int:
        number_of_int += 1
    elif type(element) == float:
        number_of_float += 1

print( "In lista se afla:",
       f" - {number_of_str} elemente de tip string",
       f" - {number_of_int} elemente de tip integer",
       f" - {number_of_float} elemente de tip float", sep="\n")

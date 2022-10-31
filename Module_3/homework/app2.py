"""
Luati ca input un sir de la utilizator. Transformați șirul într-o lista și numarati vocalele din
aceasta. Afisati numarul vocalelor pe consola.
"""

my_input = input("Introduceti un cuvant:")
v = 0

for letter in my_input:
    if letter.lower() in ["a", "e", "i", "o", "u"]:
        v += 1
print("Vocale in cuvantul dvs:", v)

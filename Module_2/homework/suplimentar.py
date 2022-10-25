"""
1)Cereți input de la utilizator cu un cuvânt. Afișați dacă acest cuvant este palindrom cu
True sau False. Găsiți o metoda pentru a valida inclusiv cazurile în care utilizatorul
introduce o literă mare, folosind una din următoarele metode:
- str.upper()
- str.lower()

2) Cereti input de la utilizator un cuvant. Folosind metoda upper(), afisati daca prima litera
din cuvant este o majuscula.
"""

# 1)
var_in = input("Introduceti un cuvant:")
print("Cuvantul introdus este palindrom:", var_in.upper() == var_in[::1].upper())

# 2)
print("M1)Sirul incepe cu o majuscula:", var_in[0].upper() == var_in[0])
print("M2)Sirul incepe cu o majuscula:", var_in[0].isalpha() == (var_in[0].upper() == var_in[0]))
print("M3)Sirul incepe cu o majuscula:", var_in[0].isupper())


"""
3)Folosind codul de la exercitiul 2, mai cereți input de la utilizator cu un număr:
- Afisati primul nume multiplicat de n ori, unde n este numărul introdus de către
utilizator.
Introduceti un nume de referinta: Ana
Introduceti un alt nume: An
Lungimea numelui de referinta este: 3
Numele de referinta este acelasi cu numele dat: False
Numele de referinta este mai lung decat numele dat: True
Initiala numelui de referinta este: A
Numele de referinta inversat este: anA
Introduceti un numar: 3
AnaAnaAna
"""

nume1 = input("Introduceti un nume de referinta:")
nume2 = input("Introduceti un alt nume:")

print("Lungimea primului nume:", len(nume1))
print("Cele doua nume sunt identice:", nume1 == nume2)
print("Primul nume este mai lung decat al doilea:", len(nume1) > len(nume2))
print("Initiala primului nume:", nume1[0])
print("Primul nume inversat:", nume1[::-1])

numar = int(input("Introduceti un numar:"))
print(numar * nume1)

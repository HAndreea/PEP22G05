"""
2) Cereți ca input de la utilizator 2 nume. Verificati si afisati:
- Lungimea primului nume
- Dacă cele doua nume date sunt la fel
- Dacă primul nume este mai lung decat al doilea nume
- Inițiala primului nume
- Primul nume inversat
"""

nume1 = input("Introduceti primul nume:")
nume2 = input("Introduceti al doilea nume:")

print("Lungimea primului nume:", len(nume1))
print("Cele doua nume sunt identice:", nume1 == nume2)
print("Primul nume este mai lung decat al doilea:", len(nume1) > len(nume2))
print("Initiala primului nume:", nume1[0])
print("Primul nume inversat:", nume1[::-1])

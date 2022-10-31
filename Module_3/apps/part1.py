# # # a = 10
# # # b = 50
# # #
# # # if a>b :
# # #  print("a is larger")
# # # elif a>50:
# # #  print("a is larger than 50 ")
# # # elif a>60:
# # #  print("a is larger than 60 ")
# # # else:
# # #  print("b is larger")
# # #
# # a= "100"
# # if a > '101':
# #  print("success >")
# # elif a=='100':
# #  print("success ==")
# #
# # #chr(0 and ord()
# # print(ord("0"))
# # print(ord("1"))
# # print(chr(97))
# #
# # # Trueish -  obiect ce poate fi convertit intr-o conditie
# # a = "101"
# #
# # if True:
# #     print("always True!")
# #
# # a = ""
# # if a:
# #     print("this is true")
# # else:
# #     print("this is false")
#
# # b = 0
# # if b:
# #     print(id(b))
# #     print("b true") # inclusiv pentru numere complexe
# # else:
# #     print(hex(id(b)))
# #     print("b is false")  #when b ==0
#
#
# # #########################
# # #introduceti primele 7 cifre din CNP , de afisat daca major
# # cnp = input("introduceti primele 7 cifre din cnp:")
# # cnp_an = int(cnp[1:3])
# # cnp_luna = int(cnp[3:5])
# # cnp_zi = int(cnp [5:7])
# # azi_zi = 20
# # azi_luna = 10
# # azi_an = 2022
# #
# # if cnp_an >50:
# #     cnp_an = 1900+cnp_an
# # else:
# #     cnp_an= 2000 +cnp_an
# # if((2022- cnp_an)>18):
# #     print("Felicitari ai 18 ani!")
# # elif (2022-cnp_an ==18):
# #     if(cnp_luna < 10):
# #         print("Felicitari ai implinit 18 ani anul acesta!")
# #     elif(cnp_luna == 10):
# #         if(cnp_zi <=20):
# #             print("Felicitari ai implinit 18 ani luna acesta!")
# #         else:
# #             print("Imi pare rau nu ai implinit 18 ani!")
# #     else:
# #         print("Imi pare rau nu ai implinit 18 ani!")
# # else:
# #     print("Imi pare rau nu ai implinit 18 ani!")
# #
# #
# # print(cnp_an,cnp_luna, cnp_zi)
#
#
# # FOR Loops
# # b = 5
# # b.__iter__()
#
#
# # a = "my_string"
# # a.__iter__()
#
# #
# # result = range(10)  # gen un interval de numere de la [0 : 10)
# # print(result)
# # print(type(result))
# # print(result.__iter__())
# #
# # for i in result:
# #     print(i)
#
# # while loop
# a= 100
# while a<200:
#     print("  inf")
#     a = a+1
#
# #input nr-> interval (0, nr) -> afiseaza nr pare
# #
# # nr = int(input("Introduceti un nr:"))
# # for i in range(nr):
# #     if(i%2==0):
# #         print(i)
#
# #
# cappuccino = 4
# espresso= 3.5
# opt = input(f"1. Cappuccino  ... {cappuccino} lei\n2. Espresso  ...{espresso} lei\nCe optiune alegeti? [1,2]: ").strip()
# opt= int(opt)
# while not (opt == 1 or opt == 2):
#     opt = int("Introduceti")
# if opt == 1 or opt == 2 :
#     bancnota = int(input("Introduceti o bancnota [5,10]:"))
#     if(bancnota == 5 or bancnota == 10):
#         if (opt ==1):
#             print("Veti primi rest:", bancnota - cappuccino)
#             print("Produsul se livreaza...")
#         else:
#             print("Veti primi rest:", bancnota - espresso)
#             print("Produsul se livreaza...")
#     else:
#         print("Bancnota invalida")
# else:
#     print("Optiune invalida!")
#
# # 4. Parola unui PC este 7788. Creați un script care sa simuleze accesul la PC.
# # Introduceti parola: 7677
# # Parola gresita. Mai incercati.
# # Introduceti parola: 3432
# # Parola gresita. Mai incercati.
# # Introduceti parola: 7788
# # Acces permis.
#
# for i in range(3):
#     passw = input("Introduceti parola:")
#     if(passw != "7677"):
#         print("Parola gresita. Mai incercati.")
#     else:
#         print("Access permis.")
#         break
#





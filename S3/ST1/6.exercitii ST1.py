#1.Funcție care să calculeze și să returneze suma a două numere

# def sum(a, b):
#     return a + b
# print(sum(3, 4))
# print(sum(-1, -10))

#2. Funcție care să returneze TRUE dacă un număr este par, FALSE pentru impar

# def paritate(x):
#     if x % 2 == 0:
#         print(f'{x} este numar par')
#     else:
#         print(f'{x} este numar impar')
# paritate(10)
# paritate(-11)

#3. Funcție care returnează numărul total de caractere din numele tău complet. (nume, prenume, nume_mijlociu)

# def lungime_nume_complet(nume, prenume, nume_mijlociu=None):
#     lungime_totala = len(nume) + len(prenume)
#     if nume_mijlociu:
#         lungime_totala += len(nume_mijlociu)
#     return lungime_totala
#
# print(lungime_nume_complet('Popescu', 'Ion', 'Vasile'))
# print(lungime_nume_complet('Alexandru', 'Raluca', 'Gabriela'))

#4. Funcție care returnează aria dreptunghiului

# def aria_dreptunghi(lungime, latime):
#     aria = lungime * latime
#     return aria
# print(aria_dreptunghi(10, 5))
# print(aria_dreptunghi(10, 0))

#5. Funcție care returnează aria cercului

# def aria_cercului(r):
#     pi = 3.14
#     a = pi * r**2
#     return a
# print(aria_cercului(5))
# print(aria_cercului(-1))

#6. Funcție care returnează True dacă un caracter x se găsește într-un string dat și False dacă nu găsește.

# def gaseste_caracter(string, caracter):
#     if caracter in string:
#         return True     # return True if caracter in string else False
#     else:
#         return False
# print(gaseste_caracter("Hello, world!", "o"))
# print(gaseste_caracter("Hello, world!", "z"))

"""
7. Funcție fără return, primește un string și printează pe ecran:
Numărul de caractere lower case este x
Numărul de caractere upper case exte y
"""
    #varinata 1
# def count_case_characters(string):
#     count_lower = 0
#     count_upper = 0
#     for char in string:
#         if char.islower():
#             count_lower += 1
#         elif char.isupper():
#             count_upper += 1
#     print(f"Numarul de caractere lower case este {count_lower}")
#     print(f"Numarul de caractere upper case este {count_upper}")
# count_case_characters('AlAbala PORtocala')

    #varinata 2
# def upperlower(string):
#     upper = 0
#     lower = 0
#     for c in range(len(string)):
#         if string[c] == ' ':
#             string[c] == 0
#         elif string[c].upper() == string[c] and string[c].isalpha():
#             upper += 1
#         else:
#             string[c].lower() == string[c] and string[c].isalpha()
#             lower += 1
#     print(f"Numarul de caractere lower case este {lower}")
#     print(f"Numarul de caractere upper case este {upper}")
# upperlower('AlAbala ORPtocala')

#8. Funcție care primește o LISTĂ de numere și returnează o LISTĂ doar cu numerele pozitive.

# def numere_pozitive(lista):
#     lista_pozitive = []
#     for numar in lista:
#         if numar > 0:
#             lista_pozitive.append(numar)
#     return lista_pozitive
# print(numere_pozitive([-1, 2, 0, 10]))

"""
9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZĂ
Primul număr x este mai mare decat al doilea număr y
Al doilea număr y este mai mare decat primul număr x
Numerele sunt egale. 
"""
# def comparare_numere(x, y):
#     if x > y:
#         print(f"Primul numar {x} este mai mare decat al doilea numar {y}")
#     elif y > x:
#         print(f"Al doilea numar {y} este mai mare decât primul numar {x}")
#     else:
#         print("Numerele sunt egale.")
# comparare_numere(3, 4)
# comparare_numere(0, 0)
# comparare_numere(-3, -1)

"""
10. Funcție care primește un număr și un set de numere.
Printează ‘am adaugat numărul nou în set’ + returnează True
Printează ‘nu am adaugat numărul în set. Acesta există deja’ + returnează False
"""
# def adauga_in_set(numar, set_numere):
#     if numar in set_numere:
#         print("Nu am adaugat numarul in set. Acesta exista deja")
#         return False
#     else:
#         set_numere.add(numar)
#         print("Am adaugat numarul nou in set")
#         return True
# numere = {1, 3, 5}
# adauga_in_set(3, numere)
# adauga_in_set(7, numere)
# print(numere)

"""
11. Funcție care primește o lună din an și returnează câte zile are acea lună.
"""
# def zile_in_luna(luna):
#     if luna in ["aprilie", "iunie", "septembrie", "noiembrie"]:
#         return 30
#     elif luna in ["ianuarie", "martie", "mai", "iulie", "august", "octombrie", "decembrie"]:
#         return 31
#     elif luna == "februarie":
#         return 28
#     else:
#         return None  # daca numele lunii nu este valid
# print(zile_in_luna("ianuarie"))
# print(zile_in_luna("ian"))

"""
12. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea, împărțirea a două numere.

În final vei putea face:
a, b, c, d = calculator(10, 2)
print("Suma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)
"""
# def calculator(x, y):
#     suma = x + y
#     diferenta = x - y
#     inmultirea = x * y
#     if y == 0:
#         impartirea = "Nu se poate imparti la 0"
#     else:
#         impartirea = x / y
#     return suma, diferenta, inmultirea, impartirea
# a, b, c, d = calculator(10, 2)
# print("Suma: ", a)
# print("Diferenta: ", b)
# print("Inmultirea: ", c)
# print("Impartirea: ", d)

"""
13. Funcție care primește o listă de cifre (adică doar 0-9) 
Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
Returnează un DICT care ne spune de câte ori apare fiecare cifră
=> dict {
0: 0
1 :2
2: 0
3: 1
4: 0
5: 3
6: 0
7: 2
8: 0
9: 1
}
"""
    #varinata 1
# def count_digits(lst):
#     counts = {i: 0 for i in range(10)}
#     for digit in lst:
#         counts[digit] += 1
#     return counts
#
# digits = [1, 3, 1, 5, 9, 7, 7, 5, 5]
# digit_counts = count_digits(digits)
#
# for digit, count in digit_counts.items():
#     print("{}: {}".format(digit, count))

    #varianta 2
# def numar_aparitii_cifre(lista_cifre):
#     dict_cifre = {i: 0 for i in range(10)}
#     for cifra in lista_cifre:
#         dict_cifre[cifra] += 1
#     return dict_cifre
#
# lista_cifre = [1, 3, 1, 5, 9, 7, 7, 5, 5]
# print(numar_aparitii_cifre(lista_cifre))
"""
14. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele.
"""
# def max_value(a, b, c):
#     return max(a, b, c)
# print(max_value(1, -3, 0))

"""
15. Funcție care să primească un număr și să returneze suma tuturor numerelor de la 0 la acel număr.
Exemplu: dacă dăm numărul 3, suma va fi 6 (0+1+2+3)
 """
    #varinata 1
# def suma_la_n(numar):
#     suma = 0
#     for i in range(numar+1):
#         suma += i
#     return suma
# print(suma_la_n(10))

    #varinata 2
# n = int(input("Introduce a number:\n"))
# def compute_sum(n):
#     return f'{n*(n+1)/2:.0f}' # 0f ca sa controlam nr de zecimale
# print(compute_sum(n))

"""
16.Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați numerele comune.

Exemplu:
list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]
Răspuns: {2, 3}
"""
# def numere_comune(list1, list2):
#     set1 = set(list1)
#     set2 = set(list2)
#     numere_comune = set1.intersection(set2)
#     return numere_comune
# list1 = [1, 1, 2, 3]
# list2 = [2, 2, 3, 4]
# print(numere_comune(list1, list2))

"""
17. Funcție care să aplice o reducere de preț.
Dacă produsul costă 100 lei și aplicăm reducere de 10%. Pretul va fi 90 de lei.
Tratează cazurile în care reducerea e invalidă. De exemplu o reducere de 110% e invalidă.
"""
# def aplicare_reducere(pret_initial, procent_reducere):
#     if pret_initial < 0 or procent_reducere > 100:
#         raise ValueError("Reducere invalida! Pretul initial trebuie sa fie > 0 si procentul reducerii < 100!")
#     return pret_initial - procent_reducere/100 * pret_initial
#
# pret_initial = 10
# procent_reducere = 10
# print(f"Pretul final este: {aplicare_reducere(pret_initial, procent_reducere)}")

"""
 18.Funcție care să afișeze data și ora curentă din România.
(bonus: afișazăi și data și ora curentă din China)
"""
# from datetime import datetime #data si ora locala
# import pytz #data si ora China
#
# def get_current_datetime():
#     # data si ora curenta din Romania
#     current_datetime_ro = datetime.now()
#     print("Data și ora curentă în România:", current_datetime_ro)
#
#     # data si ora curenta din China
#     tz = pytz.timezone('Asia/Shanghai')
#     current_datetime_china = datetime.now(tz)
#     print("Data și ora curentă în China:", current_datetime_china)
#
# get_current_datetime()

"""
19. Funcție care să afișeze câte zile mai sunt până la ziua ta / sau până la Crăciun dacă nu vrei să ne 
zici cand e ziua ta :)
"""
# import datetime
#
# def zile_ramase_pana_la_ziua_mea():
#     anul_curent = datetime.date.today().year
#     ziua_mea = datetime.date(anul_curent, 6, 15)
#     zile_ramase = (ziua_mea - datetime.date.today()).days
#     return zile_ramase
#
# def zile_ramase_pana_la_craciun():
#     anul_curent = datetime.date.today().year
#     craciun = datetime.date(anul_curent, 12, 25)
#     zile_ramase = (craciun - datetime.date.today()).days
#     return zile_ramase
#
# print("Zile ramase pana la ziua mea:", zile_ramase_pana_la_ziua_mea())
# print("Zile ramase pana la Craciun:", zile_ramase_pana_la_craciun())






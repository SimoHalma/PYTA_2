"""
10.Transformă și printează notele din sistem românesc în >
Peste 9 => A
Peste 8 => B
Peste 7 => C
Peste 6 => D
Peste 4 => E
4 sau sub => F
"""

# grade = float(input("Introdu nota:\n"))
# american_grade = ""

"""
In general, input checks sunt PRIMELE chestii pe care le facem:
fail-fast, adica daca utilizatorul a introdus date gresite, vrem sa "scapam"
de acest use-case cat mai repede.
"""

# if grade > 10 or grade <= 0:
#     print("Ai introdus o valoare gresita!")
# else:
#     if grade <= 4:
#         american_grade = "F"
#     elif grade < 6:
#         american_grade = "E"
#     elif grade < 7:
#         american_grade = "D"
#     elif grade < 8:
#         american_grade = "C"
#     elif grade < 9:
#         american_grade = "B"
#     else:
#         american_grade = "A"
#     # afisam mesajul doar daca nota introdusa a fost corecta!
#     print(f"Felicitari, ai luat nota {american_grade}")


"""
14.      x, y, z (int)
Afișează care este cel mai mare dintre ele?
"""
# x = int(input("Introdu x:\n"))
# y = int(input("Introdu y:\n"))
# z = int(input("Introdu z:\n"))

"""
Evitati sa folositi max, min, sum, ca si nume de variabile in python,
deoarece sunt functii, si daca le folosim ca nume de variabile,
nu le mai putem folosi ca functii (se face shadowing)
"""
# maxi = x     # presupunem ca valoarea maxima este x
# if maxi < y:
#     maxi = y
# if maxi < z:
#     maxi = z
# print(f"Valoarea maxima este {maxi}")
# print(f"Verificare: {max(x, y, z)}")

"""
Solutia 2: fara folosirea unei variabile auxiliare!
"""
# if x >= y and x >= z:
#     print(x)
# elif y >= x and y >= z:
#     print(y)
# else:
#     print(z)

"""
Solutia 3: cu if-uri imbricate si fara variabila aux
# """
# if x >= y:
#     # aici il comparam pe x cu z, deoarece y sigur nu este cel mai mare
#     if x >= z:
#         print(x)
#     else:
#         print(z)
# else:
#     # aici il comparam pe y cu z, deoarece x sigur nu este cel mai mare
#     if y >= z:
#         print(y)
#     else:
#         print(z)

"""
1.Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if else.
Instructiunea permite executarea unor blocuri de cod diferite in functie de valoarea expresiei logice.
"""

"""
2. Verifică și afișează dacă x este număr natural sau nu.
3. Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.
4. Verifică și afișează dacă x este între -2 și 13.
5. Verifică și afișează dacă diferența dintre x și y este mai mică de 5.
"""
# x = input("Introduceti o valoare pentru x: ")
#
# if float(x) % 1 == 0 and float(x) >= 0:
#     print(x, "este un numar natural")
# else:
#     print(x, "nu este un numar natural")
# varianta 1
# x = int(x)
# if x >= 1:
#     print("Numarul este pozitiv")
# elif x <= 1 and x != 0:
#     print("Numarul este negativ")
# else:
#     print("Numarul este neutru")
# #varianta 2
# x = int(x)
# if x > 0:
#     print("Numarul este pozitiv")
# elif x < 0:
#     print("Numarul este negativ")
# else:
#     print("Numarul este neutru")
#
# ifx >= -2 and x <= 13:
#     print("Adevarat")
# else:
#     print("Fals")
#
#Varianta 1
# y = input("Introduceti o valoare pentru y: ")
# y = int(y)
# if (x - y) < 5 and (y - x) < 5:
#     print("Diferenta este mai mica")
# else:
#     print("Diferenta este mai mare")
#Varianta 2
# while True:
#     x = input('Valoare x: ')
#     y = input('Valoare y: ')
#     try:
#         x = float(x)
#         y = float(y)
#     except:
#         print('Mai incearca!')
#         continue
#     if x - y < 5:
#         print('Diferenta este mai mica')
#         break
#     else
#         print('Diferenta este mai mare')
#         break

"""
6. Verifică dacă x NU este între 5 și 27  - a se folosi ‘not’.
"""
# x = input("Introduceti o valoare pentru x: ")
# x = int(x)
# if not 5 <= x <= 27:
#     print(f"{x} nu este intre 5 si 27")
# else:
#     print(f"{x} este intre 5 si 27")

"""
7. x și y (int)
Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai mare.
"""
#varianta 1
# x = int(input("x = "))
# y = int(input("y = "))
# if x == y:
#     print("Sunt egale")
# elif x > y:
#     print(f'{x} este mai mare decat {y}')
# else:
#     print(f'{y} este mai mare decat {x}')

#varianta 2
# x = int(input("x = "))
# y = int(input("y = "))
# if x == y:
#     print("Sunt egale")
# else:
#     print(f'Numarul mai mare este {max(x,y)}')

"""
8. X, y, z - laturile unui triunghi.
Afișează dacă triunghiul este isoscel, echilateral sau oarecare.
"""
# x = float(input("Introduceti lungimea primei laturi: "))
# y = float(input("Introduceti lungimea celei de-a doua laturi: "))
# z = float(input("Introduceti lungimea celei de-a treia laturi: "))
#
# if x == y == z:
#     print("Triunghiul este echilateral.")
# elif x == y or y == z or z == x:
#     print("Triunghiul este isoscel.")
# else:
#     print("Triunghiul este oarecare.")

"""
9. Citește o literă de la tastatură.
    Verifică și afișează dacă este vocală sau nu.
"""
# litera = input("Litera este: ")
# if litera in ('a', 'e', 'i', 'o', 'u'):
#     print("Litera este vocala.")
# else:
#     print("Litera este consoana.")

"""
11.Verifică dacă x are minim 4 cifre (x e int).
(ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
12. Verifica daca x are 6 cifre.
"""
#varianta 1
# while True:
#     x = input('Introduceti valoarea lui x\n')
#     if x.isdigit():
#         if int(x[0]) == 0:
#             print(f'{x} are valori de 0')
#             continue
#         else:
#             break
#     elif not x.isdigit():
#             print('Ai introdus litere')
#     else:
#         break
# cifre = int(len(x))
# if cifre == 4:
#     print(f'{x} are 4 cifre!')
# elif cifre == 6:
#     print(f'{x} are exact 6 cifre!!')
# else:
#     print(f'{x} nu are 4 cifre si nici exact 6!')

#varianta 2
# numar = int(input("Introdu numarul 'x' de la tastatura "))
# if numar >= 100000 and numar < 1000000:
#     print(f"x are exact 6 cifre ")
# else:
#     print(f"Numarul 'x' nu are exact 6 cifre ")

"""
13.Verifică dacă x este număr par sau impar (x e int).
"""
# x = int(input("Introduceti un numar intreg: "))
#
# if x % 2 == 0:
#     print("Numarul este par.")
# else:
#     print("Numarul este impar.")
# print('_' * 80)

"""
15.
X, y, z - reprezintă unghiurile unui triunghi
Verifică și afișează dacă triunghiul este valid sau nu.
"""
# x = float(input("Introduceti unghiul x: "))
# y = float(input("Introduceti unghiul y: "))
# z = float(input("Introduceti unghiul z: "))
#
# if x + y + z == 180 and x > 0 and y > 0 and z > 0:
#     print("Triunghiul este valid.")
# else:
#     print("Triunghiul nu este valid.")
# print('_' * 80)

"""
16. Având stringul: 'Coral is either the stupidest animal or the smartest rock'
Citește de la tastatură un int x
Afișează stringul fără ultimele x caractere
Exemplu: dacă ai ales 7 => 'Coral is either the stupidest animal or the smarte'
"""
# x = int(input('Introduceti numarul de caractere: '))
# s = 'Coral is either the stupidest animal or the smartest rock'
# new_s = s[:-x]
# print(new_s)
# print('_' * 80)

"""
17. Același string. Declară un string nou care să fie format din primele 5 caractere + ultimele 5.
"""
# s = 'Coral is either the stupidest animal or the smartest rock'
# new_s = s[:5] + s[-5:]
# print(new_s)  # 'Coral rock'

"""
18. Același string. 
Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint: este o funcție care te ajuta sa faci asta)
Folosind această variabilă + slicing, afișează tot stringul până la acest cuvânt
output: 'Coral is either the stupidest animal or the smartest' 
"""
# s = 'Coral is either the stupidest animal or the smartest rock'
# index = s.find('rock')
# print(index)
# print(s[:index])

"""
19. Joc ghicit zarul
Caută pe net și vezi cum se generează un număr random
Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll
Ia numărul ghicit de la utilizator
Verifică și afișează dacă utilizatorul a ghicit
Vei avea 3 opțiuni
Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y.
Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y.
Ai ghicit. Felicitări! Ai ales x si zarul a fost y.
"""
# import random
# dice_roll = random.randint(1,6)
# user_guess = int(input("Introdu un numar de la 1 la 6:\n"))
# if user_guess < dice_roll and user_guess < 7:
#     print(f"Ai pierdut. Ai ales un numar mai mic. Ai ales {user_guess} dar a fost {dice_roll}.")
# elif user_guess > dice_roll and user_guess < 7:
#     print(f"Ai pierdut. Ai ales un numar mai mare. Ai ales {user_guess} dar a fost {dice_roll}.")
# elif user_guess == dice_roll:
#     print(f"Ai ghicit. Felicitări! Ai ales {user_guess} si zarul a fost {dice_roll}")
# # elif user_guess > 6:
# else:
#     print(f"Numarul {user_guess} nu este valid.")
# import random
# print("Ready for a round of Dice? Yes/No ")
# while True:
#     choice_check = input("")
#     if choice_check.lower() != "no":
#         # print(choice_check)
#         roll_dice = random.randint(1, 6)
#         # print(roll_dice)
#         user_guess = int(input("Guess the computer's roll: "))
#         if user_guess == roll_dice:
#             print("Congrats! You guessed it!")
#         else:
#             print(f"Such shame! Much sad! The roll was {roll_dice}")
#     else:
#         print("Byeeee!")
#         break
#     print("Wanna play again? Yes/No")
#
# print("-"*70)

"""
20.  Citește de la tastatură un string
Verifică dacă primul și ultimul caracter sunt la fel. Se va folosi un assert
Atenție: se dorește ca programul să fie case insensitive - 'apA' e accepta
"""
# input_str = input("Introdu un string: ")
# assert input_str[0].lower() == input_str[-1].lower(), "Primul si ultimul caracter nu sunt la fel."
# print("Primul si ultimul caracter sunt la fel.")

"""
21. Având stringul '0123456789'
Afișează doar numerele pare 
Afișează doar numerele impare
(hint: folosește slicing, controlează din pas)
"""
#varianta 1
# numbers = '0123456789'
# even_numbers = numbers[::2]
# odd_numbers = numbers[1::2]
# print(even_numbers)
# print(odd_numbers)

#varianta 2
# s = "0123456789"
# pare = list()
# impare = list()
#
# for n in list(s):
#     if int(n) % 2 == 0:
#         pare.append(n)
#     else:
#         impare.append(n)
#
# print(pare)
# print(impare)


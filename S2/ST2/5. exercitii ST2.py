"""
2. Aceeași listă:
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

Folosește un for else
În for
Modifică elementele din listă astfel încât să fie scrise cu majuscule, exceptând primul și ultimul.
În else:
  Printează lista.
"""
# cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
#             #ca sa pot modifica lista, am nevoie de indecsii acesteia, asa ca for-ul meu va fi pe indecsi
#
# for idx in range(len(cars)):
#     print(f'{idx}: {cars[idx]}')
#
#    # asa fac un element al listei sa devina scris cu masjuscule -  cars[0] = cars[0].upper()
#
# for idx in range(len(cars)):
#     if idx == 0 or idx == len(cars) - 1:    # daca indexul este 0 sau len-1 (Adica daca suntem la primul SAU ultimul element
#         continue    # sarim peste
#     cars[idx] = cars[idx].upper()   # transformam masina de la indexul idx in majuscule
# else:
#     print(cars)


"""
6. Având dict:
pret_masini = {
    'Dacia': 6800,
    'Lăstun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}

Vine un client cu un buget de 15000 euro.
Prezintă doar mașinile care se încadrează în acest buget.
"""
# pret_masini = {
#     'Dacia': 6800,
#     'Lăstun': 500,
#     'Opel': 1100,
#     'Audi': 19000,
#     'BMW': 23000
# }
# buget = 15000
# for masina, pret in pret_masini.items():
#     if pret <= buget:
#         print(f'Masina {masina} costa {pret} si se incadreaza in buget')

"""
1.Având lista:
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel'] 

Folosește un for că să iterezi prin toată lista și să afișezi;
‘Mașina mea preferată este x’.
Fă același lucru cu un for each.
Fă același lucru cu un while.
"""
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# for marca in masini: #for-each, printeaza in functie de index
#     print(f'Masina mea preferata este {marca}')
#
# print('*' * 80)
#
# [print("Mașina mea preferată este", masina) for masina in masini]
#
# print('*' * 80)
#
# for marca in range(len(masini)): #simplu doar cu for
#     print(f'Masina mea preferata este {masini[marca]}')
#
# print('*' * 80)
# i = 0
# while i < len(masini):
#     print(f'Masina mea preferata este {masini[i]}')
#     i += 1

"""
3. Având lista:
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel'] 
Vine un cumpărător care dorește să cumpere un Mercedes.
Iterează prin ea prin modalitatea aleasă de tine.
Dacă mașina e mercedes:
   Printează ‘am găsit mașina dorită de dvs’
   Ieși din ciclu folosind un cuvânt cheie care face acest lucru
Altfel:
   Printează ‘Am găsit mașina X. Mai căutam‘
"""
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# for i in masini:
#     if i == 'Mercedes':
#         print('Am gasit masina dorita de dvs.')
#         break
#     else:
#         print(f'Am gasit masina {i}. Mai cautam')

"""
4. Aceeași listă;
Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu excepția Trabant și Lăstun. 

Dacă mașina e Trabant sau Lăstun:
   Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie else).
Printează S-ar putea să vă placă mașina x.
"""
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# for i in masini:
#     if i == 'Trabant' or i == 'Lăstun':
#         continue
#     print(f'S-ar putea sa va placa masina {i}')

"""
5. Modernizează parcul de mașini:

Crează o listă goală, masini_vechi.
Iterează prin mașini.
Când găsesti Lăstun sau Trabant:
Salvează aceste mașini în masini_vechi.
Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
Printează Modele vechi: x.
Modele noi: x.
"""
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# masini_vechi = []
# for i in masini:
#     if i == 'Trabant' or i == 'Lăstun':
#         masini_vechi.append(i)
#         masini[masini.index(i)] = 'Tesla'
# print('Modele vechi:', masini_vechi)
# print('Modele noi:', masini)

"""
7. Având lista:
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
Iterează prin ea.
Afișează de câte ori apare 3 (nu ai voie să folosești count).
"""
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# suma = 0
# for i in range(len(numere)):
#     suma = suma + numere[i]
# print(suma)

"""
8. Aceeași listă:
Iterează prin ea
Calculează și afișează suma numerelor (nu ai voie să folosești sum).
"""
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# s = 0
# for i in numere:
#     s += i
#     print(f'Noua suma este {s}')
# print(f'Suma finala este {s}')

"""
9. Aceeași listă:
Iterează prin ea.
Afișază cel mai mare număr (nu ai voie să folosești max).
"""
# numere = [-5, -7, -3, -9, -3, -3, -1, -4, -3]
# maxi = numere[0]
# for i in numere:
#     while i > maxi:
#         maxi = i
# print(maxi)

"""
10. Aceeași listă:
Iterează prin ea.
Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
Ex: dacă e 3, să devină -3
Afișază noua listă.
"""
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
for i in range(len(numere)):
    if numere[i] > 0:
        numere[i] = -numere[i]
print(numere)

"""
11.
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
Itereaza prin listă alte_numere 
Populează corect celelalte liste
Afișează cele 4 liste la final
"""
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
# for i in alte_numere:
#     if i % 2 == 0:
#         numere_pare.append(i)
#     if i % 2 == 1:
#         numere_impare.append(i)
#     if i > 0:
#         numere_pozitive.append(i)
#     if i < 0:
#         numere_negative.append(i)
# print(numere_pare)
# print(numere_impare)
# print(numere_pozitive)
# print(numere_negative)

"""
12. Aceeași listă:
Ordonează crescător lista fară să folosești sort.
Te poți inspira vizual de aici.
https://www.youtube.com/watch?v=lyZQPjUT5B4
"""
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# for i in range(len(numere)):
#     for j in range(0, len(numere)-i-1): #itereaza prin lista ramasa dupa fiecare pas
#         print(len(numere)-i-1)
#         if numere[j] > numere[j + 1]:
#             numere[j], numere[j + 1] = numere[j + 1], numere[j]
#             print(numere)
# print(numere)

#sau folosim numere.sort()

"""
13. Ghicitoare de număr:
numar_secret = Generați un număr random între 1 și 30
Numar_ghicit = None
Folosind un while
   User alege un număr
   Programul îi spune:
Nr secret e mai mare
Nr secret e mai mic
Felicitări! Ai ghicit!
"""
# import random
#
# numar_secret = random.randint(1, 30) #functia radint genereaza un nr aleatoriu
# numar_ghicit = None
#
# while numar_ghicit != numar_secret:
#     numar_ghicit = int(input("Ghiceste numarul secret (intre 1 si 30): "))
#     if numar_ghicit > numar_secret:
#         print("Numarul secret este mai mic.")
#     elif numar_ghicit < numar_secret:
#         print("Numarul secret este mai mare.")
#     else:
#         print("Felicitari! Ai ghicit numarul secret.")

"""
14. Alege un număr de la tastatură
Ex: 7
Scrie un program care să genereze în consolă următoarea piramidă
1
22
333
4444
55555
666666
7777777

Ex:3
1
22
333
"""
#Varinata 1
# numar = int(input('Introduceti un numar pozitiv:'))
# while numar <= 0:
#     numar = int(input('Introduceti un numar pozitiv:'))
#
# for i in range(numar+1):
#     for j in range(i):
#         print(i, end='')
#     print()

# #Varianta 2
# numar = int(input('Introduceti un numar pozitiv:'))
# while numar <= 0:
#     numar = int(input('Introduceti un numar pozitiv:'))
# for i in range(1, numar+1):
#     print(str(i) * i) #sir format din i repetat de i ori

# #Varinata 3
# numar = int(input('Introduceti un numar pozitiv:'))
# while numar <= 0:
#      numar = int(input('Introduceti un numar pozitiv:'))
# i = 1
# while i <= numar:
#     print()
#     for j in range(i):
#         j = i
#         print(j, end='')
#         j += 1
#     i += 1
"""
15.
tastatura_telefon = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]
Iterează prin listă 2d
Printează ‘Cifra curentă este x’
(hint: nested for - adică for în for)
"""
# tastatura_telefon = [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9],
#   [0]
# ]
# for row in tastatura_telefon:
#     for digit in row:
#         print(f'Cifra curentă este {digit}')
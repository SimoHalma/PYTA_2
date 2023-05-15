"""
Pentru toate exercițiile se va folosi noțiunea de if în rezolvare.
Indirect vei exersa și operatorii în cadrul condițiilor ramurilor din if.
X poate fi inițializat direct în cod sau citit de la tastatură, după preferințe.
X este un int.

1. Declară o listă note_muzicale în care să pui do re mi etc până la do
Afișeaz-o.
Inversează ordinea folosind slicing și suprascrie această listă.
Printează varianta actuală (inversată).
Pe această listă aplică o metodă care bănuiești că face același lucru, adică să îi inverseze ordinea.
Nu trebuie să o suprascrii în acest caz, deoarece metoda face asta automat.
Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta inițială.

Concluzii: slicing e temporar, dacă vrei să păstrezi nouă variantă va trebui să suprascrii lista sau
să o salvezi într-o listă nouă. Metoda găsită de tine face suprascrierea automat și permanentizează aceste modificări.
 Ambele variante își găsesc utilitatea în funcție de ce ne dorim în acel moment.
"""
# note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
# print(f'Lista este: {note_muzicale}')
# note_muzicale = note_muzicale[::-1] #slicing
# print(f'Lista citita invers este: {note_muzicale}')
# note_muzicale.reverse() #prin metoda
# print(f'Lista citita invers este: {note_muzicale}')

"""
2. De câte ori apare ‘do’?
"""
# note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
# count_do = note_muzicale.count('do')
# print(count_do)

"""
3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
   Găsește 2 variante să le unești într-o singură listă.
"""
# list1 = [3, 1, 0, 2]
# list2 = [6, 5, 4]
# list3 = list1 + list2
# print('Prima varanta este:', list3)
#
# list1.extend(list2)
# print('A doua varianta este: ', list1)
"""
4.
Sortează și afișează lista generată la exercițiul anterior.
Sortează numărul 0 folosind o funcție.
Afișaza iar lista.
"""
# list1.sort()
# print(list1)
# list1.sort(key=lambda x: x == 0)
# """
# Explicația este că key primește o funcție care calculează o valoare pentru fiecare element înainte de sortare.
# În acest caz, folosim o funcție lambda care va evalua la True pentru orice element care nu este 0 și la False pentru
# elementul 0. Astfel, elementele care nu sunt 0 vor fi sortate înainte de elementul 0.
# """
# print(list1)

"""
5. Folosind un if verifică lista generată la exercițiul 3 și afișează:
Lista este goală.
Lista nu este goală.
"""
# list1 = [3, 1, 0, 2]
# list2 = [6, 5, 4]
# list1.extend(list2)
# if list1 == []:
#     print('Lista esye goala.')
# else:
#     print('Lista nu este goala.')
"""
6. Folosește o funcție care să șteargă lista de la exercițiul 3.
"""
# list1.clear()

"""
7. Copy paste la exercițiul 5. Verifică încă o dată.
Acum ar trebui să se afișeze că lista e goală.
"""
# if list1 == []:
#     print('Lista este goala.')
# else:
#     print('Lista nu este goala.')

"""
8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
Folosește o funcție că să afișezi Elevii (cheile)
"""
# dictionar ={
#     'Ana': 8,
#     'Gigel': 10,
#     'Dorel': 5
# }
# print(dictionar.keys())

"""
9. Printează cei 3 elevi și notele lor
Ex: ‘Ana a luat nota {x}’
Doar nota o vei lua folosindu-te de cheie
"""
# dictionar ={
#     'Ana': 8,
#     'Gigel': 10,
#     'Dorel': 5
# }
# for keys, values in dictionar.items():
#     print(f'Ana a luat nota: {dictionar.get("Ana")}')
#     print(f'Gigel a luat nota: {dictionar.get("Gigel")}')
#     print(f'Dorel a luat nota: {dictionar.get("Dorel")}')
#     break

"""
10. Dorel a făcut contestație și a primit 6
Modifică nota lui Dorel în 6
Printează nota după modificare
"""
# dictionar ={
#     'Ana': 8,
#     'Gigel': 10,
#     'Dorel': 5
# }
# dictionar['Dorel'] = 6
# print(dictionar)

"""
11. Gigel se transferă din clasă
Căuta o funcție care să îl șteargă
Vine un coleg nou. Adaugă Ionică, cu nota 9
Printează noii elevi
"""
# dictionar.pop('Dorel')
# dictionar.update({'Ionica': 9})
# print(dictionar.keys())

"""
12. Ne imaginăm o echipă de fotbal pt teren sintetic.
3 Schimbări maxime admise:
Declară o Listă cu 5 jucători
Schimbari_efectuate = te joci tu cu valori diferite
Schimbari_max = 3
Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
Efectuează schimbarea 
Șterge jucătorul scos din listă
Adaugă jucătorul intrat
Afișază a intrat x, a ieșit y, mai ai z schimbări

Dacă jucătorul nu e în teren:
Afișază ‘nu se poate efectua schimbarea deoarece jucătorul x nu e în teren’
Afișază ‘mai ai z schimbări’

Testează codul cu diferite valori

Google search hint
“how to check if item is in list python”
"""
#Varianta 1
# jucatori = ['Andrei', 'Bogdan', 'Cristian', 'David', 'Eduard']
# schimbari_efectuate = 0
# schimbari_max = 3
# jucator_in_teren = 'Andrei'
#
# if jucator_in_teren in jucatori:
#     index_jucator_in_teren = jucatori.index(jucator_in_teren)
#     jucator_iesit = jucatori.pop(index_jucator_in_teren)
#     jucator_intrat = 'Florin'
#     jucatori.append(jucator_intrat)
#     schimbari_efectuate += 1
#     print(f'A intrat {jucator_intrat}, a iesit {jucator_iesit}, mai ai {schimbari_max - schimbari_efectuate} schimbari.')
# else:
#     print(f'Nu se poate efectua schimbarea deoarece jucatorul {jucator_in_teren} nu e in teren.')
#     print(f'Mai ai {schimbari_max - schimbari_efectuate} schimbari.')

#Varianta 2
# jucatori = input("Introduceti numele jucatorilor separati prin virgula: ").split(",")
# teren = jucatori[:5]
# schimbari_efectuate = 0
# schimbari_max = 3
#
# while True:
#     print(f"Jucatorii in teren: {teren}")
#     if schimbari_efectuate < schimbari_max:
#         jucator_iesit = input("Introduceti numele jucatorului care iese: ")
#         if jucator_iesit not in teren:
#             print(f"Nu se poate efectua schimbarea deoarece jucatorul {jucator_iesit} nu este in teren.")
#         else:
#             teren.remove(jucator_iesit)
#             jucator_intrat = input("Introduceti numele jucatorului care intra: ")
#             teren.append(jucator_intrat)
#             schimbari_efectuate += 1
#             print(f"A intrat {jucator_intrat}, a iesit {jucator_iesit}, mai ai {schimbari_max - schimbari_efectuate} schimbari disponibile.")
#     else:
#         print("Nu mai ai schimbari disponibile.")
#         break

"""
13.
Set
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
Adaugă în zilele_sapt ‘luni’
Afișează zile_sapt
"""
# # Valorile din set sunt unice!!!
# zile_sapt = {'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
# weekend = {'sâmbăta', 'duminică'}
# zile_sapt.add('luni')
# print(zile_sapt)

"""
14.Folosește un if și verifică dacă:
Weekend este un subset al zilelor din săptămânii.
Weekend nu este un subset al zilelor din săptămânii.
"""
# Varianta 1
# zile_sapt = {'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
# weekend = {'sâmbăta', 'duminică'}
# if weekend.intersection(zile_sapt) == weekend:
#     print('Weekend este un subset al zilelor din săptămânii.')
# else:
#     print('Weekend nu este un subset al zilelor din săptămânii.')

# Varianta 2
# zile_sapt = {'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
# weekend = {'sâmbăta', 'duminică'}
# if weekend.issubset(zile_sapt):
#     print('Weekend este un subset al zilelor din săptămânii.')
# else:
#     print('Weekend nu este un subset al zilelor din săptămânii.')

"""
15. Afișează diferențele dintre aceste 2 seturi.
"""
# zile_sapt = {'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
# weekend = {'sâmbăta', 'duminică'}
# print(zile_sapt - weekend)
# print(weekend - zile_sapt)

"""
16. Afișează intersecția elementelor din aceste 2 seturi.
"""
# zile_sapt = {'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
# weekend = {'sâmbăta', 'duminică'}
# print(zile_sapt.intersection(weekend))
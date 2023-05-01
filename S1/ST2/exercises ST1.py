"""
1. În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă. 

Variabila este o locatie din memorie care tine o valoare si are un nume sugestiv.

2. Declară și initializează câte o variabilă din fiecare din următoarele tipuri de variabilă:
string
int 
float
bool
Observație: Valorile vor fi alese de tine după preferințe.
"""
# nume = 'Simona'
# varsta = 24
# inaltime = 1.80
# pisici = True

"""
3. Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.
"""
# print(type(nume), type(varsta), type(inaltime), type(pisici))

"""
4. Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în aceeași variabilă (suprascriere):
Verifică tipul acesteia.
"""
# inaltime = round(inaltime)
# print(inaltime)
# print(type(inaltime))

"""
5. Folosește print() și printează în consolă 4 propoziții folosind cele 4 variabile.
Rezolvă nepotrivirile de tip prin ce modalitate dorești.
"""
# varsta = 18
# inaltime = 1.88
# nume = "Ion"
# e_adult = True
# job = "Aviator"
# print(f"Numele este {nume} an {varsta} ani.")
# print(f"Am inaltime de {inaltime}")
# print(f"Sunt adult = {e_adult}")
# print(f"Jobul meu este de {job}")

"""
6. Citește de la tastatură:
numele;
prenumele.
    Afișează: 'Numele complet are x caractere'.
"""
# last_name = input("Introduceti numele:\n")
# first_name = input("Introduceti prenumele:\n")
# print("Numele complet are", len(last_name) + len(first_name), "caractere.")

"""
7. Citește de la tastatură:
lungimea;
lățimea.
   Afișează: 'Aria dreptunghiului este x'.
"""
# lungime_dreptunghi = input("L = ")
# latime_dreptunghi = input("l = ")
# print("Aria dreptunghiului este", lungime_dreptunghi * latime_dreptunghi)

"""
8. Având stringul: 'Coral is either the stupidest animal or the smartest rock':
afișează de câte ori apare cuvântul 'the';
"""
s = "Coral is either the stupidest animal or the smartest rock"
print(s.count("the"))

"""
10. Folosește un assert ca să verifici dacă acest string conține doar numere.
"""

"""
11. Exercițiu:
citește de la tastatură un string de dimensiune impară;
afișează caracterul din mijloc.
"""
# nume_pisica = input("Numele pisicii este: ")
# index_mijloc = len(nume_pisica) // 2
# caracter_mijloc = nume_pisica[index_mijloc]
# print("Caracterul din mijloc este: ", caracter_mijloc)

# int_string = input("Introdu un sir de caractere:\n")
# print(len(inp_string))
# print(inp_string[len(inp_string) // 2]) #indexul este pozitia caracterului din str

"""
12. Folosind o singură linie de cod :
citește un string de la tastatură (ex: 'alabala portocala');
salvează fiecare cuvânt într-o variabilă;
printează ambele variabile pentru verificare.
"""
#varianta 1
# var1, var2 = input("Introduceti un sir de caractere: ").split()
# print(var1)
# print(var2)

#varianta 2 - Analogie cu C++
# var = input("Intrudceti un string: \n")
# var2 = var.split()
# for i in var2:
#     print(i)

"""
13. Exercițiu:
citește un string de la tastatură (ex: alabala portocala);
salvează primul caracter într-o variabilă - indiferent care este el, încearcă cu 2 stringuri diferite;
capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul caracter => alAbAlA portocAla.
"""
# tastatura = input("Introduceti in string: \n")
# x = tastatura[0]
# y = tastatura.replace(x, x.upper()) #facem variabila din x cu litera mare
# print(y[0].replace(y[0],y[0].lower())+y[1:-1]+y[-1].replace(y[-1],y[-1].lower()))

"""
14. Exercițiu:
citește un user de la tastatură;
citește o parolă;
afișează: 'Parola pt user x este ***** și are x caractere';
***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să afișeze corect.
eg: parola abc => ***
      parola abcd => ****
"""
user = input("Introduceti un user: ")
parola = input("Introduceti o parola: ")
lungime_parola = len(parola)
indicator = '*' * lungime_parola
print(f"Parola pt userul {user} este {indicator} și are {lungime_parola} caractere.") #varianta 1
print(f"Parola pt userul {user} este {'*' * len(parola)} și are {len(parola)} caractere.") #varianta 2
print(f"Parola pt userul {user} este {parola.replace(parola, '*' * len(parola))} si are {len(parola)} caractere.") #varianta 3
print(parola)

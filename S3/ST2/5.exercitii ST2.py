"""
1.Clasa Cerc
    Atribute: rază, culoare
    Constructor pentru ambele atribute
    Metode:
descrie_cerc() - va PRINTA culoarea și raza
aria() - va RETURNA aria
diametru()
circumferinta()
"""
import math

class Cerc:
    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descrie_cerc(self):
        print(f"Cercul are raza {self.raza} și culoarea {self.culoare}.")

    def aria(self):
        return math.pi * self.raza ** 2

    def diametru(self):
        return self.raza * 2

    def circumferinta(self):
        return 2 * math.pi * self.raza
c = Cerc(5, "albastru")
c.descrie_cerc()
print(c.aria())
print(c.diametru())
print(c.circumferinta())

"""
2. Clasa Dreptunghi
     Atribute: lungime, lățime, culoare
     Constructor pentru toate atributele
     Metode:
descrie()
aria()
perimetrul()
schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic. Ea va lua ca și parametru o nouă culoare și 
va suprascrie atributul self.culoare. Poți verifica schimbarea culorii prin apelarea metodei descrie().
"""
# class Dreptunghi:
#     def __init__(self, lungime, latime, culoare):
#         self.lungime = lungime
#         self.latime = latime
#         self.culoare = culoare
#
#     def descrie(self):
#         print(f"Acest dreptunghi are o lungime de {self.lungime} și o latime de {self.latime}. "
#               f"Este de culoare {self.culoare}.")
#
#     def aria(self):
#         return self.lungime * self.latime
#
#     def perimetrul(self):
#         return 2 * (self.lungime + self.latime)
#
#     def schimba_culoare(self, noua_culoare):
#         self.culoare = noua_culoare
#
# dreptunghi = Dreptunghi(5, 10, "rosu")
#
# dreptunghi.descrie()
# print("Aria dreptunghiului este:", dreptunghi.aria())
# print("Perimetrul dreptunghiului este:", dreptunghi.perimetrul())
# dreptunghi.schimba_culoare("albastru")
# dreptunghi.descrie()

"""
3. Clasa Angajat
     Atribute: nume, prenume, salariu
     Constructor pentru toate atributele
     Metode:
descrie()
nume_complet()
salariu_lunar()
salariu_anual()
marire_salariu(procent)
"""
# class Angajat:
#     def __init__(self, nume, prenume, salariu):
#         self.nume = nume
#         self.prenume = prenume
#         self.salariu = salariu
#
#     def descrie(self):
#         print(f"Angajatul {self.nume} {self.prenume} are un salariu de {self.salariu} lei.")
#
#     def nume_complet(self):
#         return f"{self.nume} {self.prenume}"
#
#     def salariu_lunar(self):
#         return self.salariu
#
#     def salariu_anual(self):
#         return self.salariu * 12
#
#     def marire_salariu(self, procent):
#         self.salariu *= (1 + procent / 100)
#         print(f"Salariul angajatului {self.nume} {self.prenume} a fost marit cu {procent}% si este acum de {self.salariu} lei.")
#
# angajat1 = Angajat("Popescu", "Ion", 5000)
# angajat1.descrie()
# print(angajat1.nume_complet())
# print(angajat1.salariu_lunar())
# print(angajat1.salariu_anual())
# angajat1.marire_salariu(10)
# angajat1.descrie()

"""
4. Clasa Cont
   Atribute: iban, titular_cont, sold
   Constructor pentru toate atributele
   Metode:
afisare_sold() - Titularul x are în contul y suma de n lei
debitare_cont(suma)
creditare_cont(suma)
"""
# class Cont:
#     def __init__(self, iban, titular_cont, sold):
#         self.iban = iban
#         self.titular_cont = titular_cont
#         self.sold = sold
#
#     def afisare_sold(self):
#         print(f"Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei")
#
#     def debitare_cont(self, suma):
#         if suma > self.sold:
#             print("Fonduri insuficiente")
#         else:
#             self.sold -= suma
#             print(f"{suma} lei au fost debitati din contul {self.iban}. Soldul curent este {self.sold} lei")
#
#     def creditare_cont(self, suma):
#         self.sold += suma
#         print(f"{suma} lei au fost creditati in contul {self.iban}. Soldul curent este {self.sold} lei")
#
# cont = Cont("RO123456789", "John Doe", 1000)
# cont.afisare_sold()  # Titularul John Doe are in contul RO123456789 suma de 1000 lei
# cont.debitare_cont(500)  # 500 lei au fost debitati din contul RO123456789. Soldul curent este 500 lei
# cont.creditare_cont(200)  # 200 lei au fost creditati in contul RO123456789. Soldul curent este 700 lei
# cont.afisare_sold()

"""
 5. Clasa Factură
     Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor avea aceeași serie), număr, 
     nume_produs, cantitate, pret_buc
     Constructor: toate atributele, fără serie
     Metode:
schimbă_cantitatea(cantitate)
schimbă_prețul(pret)
schimbă_nume_produs(nume)
generează_factura() - va printa tabelar dacă reușiți

Factura seria x număr y
Data: generează automat data de azi
Produs | cantitate | preț bucată | Total 
Telefon |      7       |       700       | 49000   
"""
# import datetime
#
# class Factura:
#     # atribut constant
#     SERIE = 'X'
#
#     def __init__(self, numar, nume_produs, cantitate, pret_buc):
#         self.numar = numar
#         self.nume_produs = nume_produs
#         self.cantitate = cantitate
#         self.pret_buc = pret_buc
#
#     def schimba_cantitatea(self, cantitate):
#         self.cantitate = cantitate
#
#     def schimba_pretul(self, pret):
#         self.pret_buc = pret
#
#     def schimba_nume_produs(self, nume):
#         self.nume_produs = nume
#
#     def genereaza_factura(self):
#         total = self.cantitate * self.pret_buc
#         data_curenta = datetime.date.today().strftime('%d/%m/%Y')
#         print(f"Factura seria {self.SERIE} număr {self.numar}\nData: {data_curenta}\n"
#               f"Produs      | Cantitate | Preț bucată | Total\n"
#               f"{self.nume_produs: <12}| {self.cantitate: <9}| {self.pret_buc: <12}| {total: <5}")
#
# f = Factura(1, 'Telefon', 7, 700)
# f.genereaza_factura()
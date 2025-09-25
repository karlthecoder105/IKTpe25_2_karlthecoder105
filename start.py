# Ülesanne 1
# Kirjuta enda esimene programm, mis väljastab käsureale teksti: “Tere, maailm!”. 
# Küsi kasutaja nimi ja muuda tekst, et ta näeks välja nii: “Tere, maailm! Tervitan sind Mati”, kui kasutaja nimi on Mati.
# Küsi kasutajalt sisend tema vanuse kohta ning väljasta see ekraanile:
# “Tere, maailm! Tervitan sind Mati! Sa oled N aastat vana.”

print("Tere, Maailm!")
nimi =input("Mis su nimi on?").capitalize()   
print(f"Tere, maailm! Tervitan sind {nimi}")
vanus = int(input("Kui vana sa oled? "))
print(f"Tere, maailm! Tervitan sind {nimi}! Oled {vanus} + aastat vana.".upper())

# Ülesanne2 Mis tüüpi on järgnevad muutujad:
# a) vanus = 18
# b) eesnimi = "Jaak"
# c) pikkus = 16.5
# d) kas_käib_koolis = True
# Mis võimalus veel peale True oleks viimast muutujat väärtustada? Kuidas võiks nende muutujate väärtusi koodis kontrollida?
# Kirjuta kood tüüpide kontrollimiseks.

vanus=18 #täisarv
print(f"Muutuja vanus on tüübilt {type(vanus)}")
eesnimi="Jaak" #sõne
print(f"Muutuja eesnimi on tüübilt {type(vanus)}")
pikkus=166.5 #ujukomaarv
print(f"Muutuja pikkus on tüübilt {type(eesnimi)}")
kas_käib_koolis=True #Loogikaväärtus
print(f"Muutuja kas_käib_koolis on tüübilt {type(kas_käib_koolis)}")





# Ülesanne 3
# Kirjuta enda koodis laual olevate kommide arv muutujasse(kommide arv on juhuslik). Seejärel kuva muutujas olev kommide arv ekraanile kasutades print() käsku.
# Küsi kasutajalt sisendit, 
# mitu kommi ta soovib laualt ära võtta. 
# Eemalda soovitud kommide arv laual olevate kommide arvust ja kuva ekraanile, 
# kui palju komme laual nüüd on. 


from multiprocessing.spawn import import_main_path
from random  import *
kommide_arv=randint(10,100)
print(f"Laual on {kommide_arv} kommi")
võetud_kommide_arv=int(input("Mitu kommi sa soovid laualt ära võtta? "))
if võetud_kommide_arv>kommide_arv:
    print(f"´Laual pole nii palju komme. ")
else:
    kommide_arv=võetud_kommide_arv
    print(f"Nüüd on laual {kommide_arv} kommi.")

#Ülesanne 4
#Puu läbimõõdu arvutamine
#Kirjuta programm, mis küsib kasutaja käest puu ümbermõõdu ning teatab selle peale puu läbimõõdu.

from random import *
puu_läbimõõt=randint(10,1000)
print(f"Puu mõõt on {puu_läbimõõt} m")
lõigatud_puu_läbimõõt=int(input("Kui palju on puu läbimõõt siis, kui sa seda lõikad?"))
if lõigatud_puu_läbimõõt>puu_läbimõõt :
    print(f"Puu on liiga lühike")
else:
    lõigatud_puu_läbimõõt=puu_läbimõõt
    print(f"Nüüd on puu {puu_läbimõõt} m.")








print ("saame tuttavaks!")
nimi =input("mis on su nimi?").capitalize()       # sõne
print("tere," +nimi +   "!")
vanus = int(input("kui vana sa oled"))            #  täisarv
print ("oled " +str(vanus) + "aastat vana.")
print (f"järgmine aasta oled {vanus +1} aastat vana.") 
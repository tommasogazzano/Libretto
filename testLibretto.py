from Voto.voto import Libretto, Voto

from scuola import Student
Harry = Student(nome="Harry", cognome="Potter", eta=11, capelli="castani", occhi="azzurri", casa="Grifondoro", animale="civetta", incantesimo="Expecto Patronum")

myLib = Libretto(Harry, [])
myLib.append(Voto("Trasfigurazione", 24, "2022-02-13", False))
myLib.append(Voto("Babbanologia", 30, "2022-02-17", False))
myLib.append(Voto("Pozioni", 21, "2022-02-18", False))

print(myLib.calcolaMedia())
votiFiltrati = myLib.getVotiByPunti(21, False)
print(votiFiltrati) #Se faccio print(VotiFiltrati[0]) utilizza il toString

votoTrasfigurazione = myLib.getVotoByName("Trasfigurazione")
if votoTrasfigurazione is None:
    print("Voto non trovato")
else:
    print(votoTrasfigurazione)

print(f"Verifico metodo hasVoto:")
#print(myLib.hasVoto(v1))
print(myLib.hasVoto(Voto("Trasfigurazione", 24, "2022-02-13", False)))
print(myLib.hasVoto(Voto("Aritmanzia", 30, "2022-02-17", False)))
print(f"Verifico metodo hasConflitto:")
print(myLib.hasConflitto(Voto("Trasfigurazione", 30, "2022-02-13", True)))

print(f"Verifico self.append modificata:")
myLib.append(Voto("Aritmanzia", 30, "2022-02-17", False))
##myLib.append(Voto("Trasfigurazione", 24, "2022-02-13", False))

myLib.append(Voto("Divinazione", 27, "2021-02-08", False))
myLib.append(Voto("Cura delle creature magiche", 28, "2021-06-13", False))

print(f"-------------------------------")
print(f"print il Libretto Modificato:")
nuovoLib = myLib.creaMigliorato()
print(nuovoLib)
print(f"printo il libretto Originario")
print(myLib)


print(f"--------------------")
print(f"Verifico libretto ordinato per materia:")
nuovoLib1 = myLib.creaLIbOrdinatoPerMateria()
print(nuovoLib1)

print(f"--------------------")
print(f"Verifico libretto ordinato per punteggio:")
nuovoLib2 = myLib.creaLibOrdinatoPerVoto()
print(nuovoLib2)

print(f"--------------------")
print(f"Verifico libretto cancellando i voti <24:")
nuovoLib2.cancellaInferiori(24)
print(nuovoLib2)

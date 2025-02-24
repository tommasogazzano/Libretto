# Harry = ["Harry", "Potter", 11,
#          "capelli castani", "occhi azzurri",
#          "Grifondoro", ""]
#
# print(Harry)
# print("Il nome è ", Harry[0])
#
# Harry[6] = "Expecto Patronum"
#
# print(Harry)
#
# Ron = ["Ron", "Weasley", 11,
#          "capelli rossi", "occhi marroni",
#          "Grifondoro", ""]
#
# Grifondoro = [Harry, Ron]

class Person:
    def __init__(self, nome, cognome, eta,
                 capelli, occhi, casa, incantesimo="Non ancora definito"):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        self.capelli = capelli
        self.occhi = occhi
        self.casa = casa
        self.incantesimo = incantesimo

    def __str__(self):
        return f"{self.nome} {self.cognome}"

class Student(Person):
    def __init__(self,nome, cognome, eta,
                 capelli, occhi, casa, animale, incantesimo="Non ancora definito"):
        super().__init__(nome, cognome, eta, capelli, occhi, casa, incantesimo)
        self.animale = animale

    def __str__(self):
        return f"Studente: {self.nome} - {self.cognome} - {self.casa} "

    def __repr__(self):
        return f"Student(nome, cognome, eta, capelli, occhi, casa, animale)"

    def prettyPrint(self):
        print("Voglio stampare meglio")

class Teacher(Person):
    def __init__(self, nome, cognome, eta,
                 capelli, occhi, casa, materia, incantesimo="Non ancora definito"):
        super().__init__(nome, cognome, eta, capelli, occhi, casa, incantesimo)
        self.materia = materia

class Casa:
    def __init__(self, nome, studenti = [] ):
        self.nome = nome
        self.studenti = studenti

    def addStudente(self, studente):
        self.studenti.append(studente) # --> [ x,x,x [s1, s2]]

        # self.studenti.extend(studente) # --> [ x,x,x, s1, s2 ]

    def __str__(self):
        if len(self.studenti) == 0:
            return "La casa {self.nome} + è vuota."

        mystr = f"Lista degli studenti iscritti alla casa {self.nome} \n"
        for s in self.studenti:
            mystr += str(s) + "\n"

        return mystr

Harry = Person("Harry", "Potter", 11,
               "castani", "azzurri", "Grifondoro")
Ron = Student("Ron", "Weasley", 11, "rossi", "castani",
              "Grifondoro", "topo")
Severus = Teacher("Severus", "Snape", 45, "neri", "neri",
                  "Serpeverde", "Pozioni", "Sectumsempra")
print(Harry)
print(Ron)
print(Severus)

grifondoro = Casa("Grifodnoro", [Harry])
print(grifondoro)
grifondoro.addStudente(Ron)
print(grifondoro)

from dataclasses import dataclass

@dataclass
class Voto:
    materia: str
    punteggio: int
    data: str
    lode: bool

    def __str__(self):
        if self.lode:
            return f"In {self.materia} hai preso {self.punteggio} con lode, il {self.data}"
        else:
            return f"In {self.materia} hai preso {self.punteggio}, il {self.data}"

class Libretto:
    def __init__(self, proprietario, voti = []):
        self.proprietario = proprietario
        self.voti = voti

    def append(self, voto): #Duck Type
        self.voti.append(voto)

    def __str__(self):
        mystr = f"Libretto voti di {self.proprietario}"
        for v in self.voti:
            mystr += f"{v} \n"
        return mystr

    def __len__(self):
        return len(self.voti)

'''
class Voto:
    def __init__(self, materia, punteggio, data, lode):
        if punteggio== 30:
            self.materia = materia
            self.punteggio = punteggio
            self.data = data
            self.lode = lode
        elif punteggio < 30:
            self.materia = materia
            self.punteggio = punteggio
            self.data = data
            self.lode = False
        else:
            raise ValueError(f"Attenzione, non posso creare un voto con punteggio {self.punteggio}")

    def __str__(self):
        if self.lode:
            return f"In {self.materia} hai preso {self.punteggio} con lode, il {self.data}"
        else:
            return f"In {self.materia} hai preso {self.punteggio}, il {self.data}"
'''

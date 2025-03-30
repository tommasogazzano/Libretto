from dataclasses import dataclass


@dataclass(order=True)
class Voto:
    materia: str
    punteggio: int
    data: str
    lode: bool

    def __str__(self):
        if self.lode:
            return f"In {self.materia} hai preso {self.punteggio} e lode il {self.data}"
        else:
            return f"In {self.materia} hai preso {self.punteggio} il {self.data}"

    def copy(self):
        return Voto(self.materia, self.punteggio,
                    self.data, self.lode)
    # def __eq__(self, other):
    #     return (self.materia == other.materia and
    #             self.punteggio == other.punteggio and
    #             self.lode == other.lode)

    def __eq__(self, other):
        return self.materia == other.materia

    def __hash__(self):
        # return hash((self.materia, self.punteggio, self.lode))
        return hash(self.materia)
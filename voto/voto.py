import operator
from dataclasses import dataclass

cfuTot = 180

@dataclass
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

    def __eq__(self, other):
        return(self.materia == other.materia and
               self.punteggio == other.punteggio and
               self.lode == other.lode)

    def copy(self):
        return Voto(self.materia, self.punteggio, self.data, self.lode)

class Libretto:
    def __init__(self, proprietario, voti = []):
        self.proprietario = proprietario
        self.voti = voti

    def append(self, voto): # duck!
        if(self.hasVoto(voto) is False
            and self.hasConflitto(voto) is False):
            self.voti.append(voto)
        else:
            raise ValueError(f"Voto già presente o in conflitto")

    def __str__(self):
        mystr = f"Libretto voti di {self.proprietario} \n"
        for v in self.voti:
            mystr += f"{v} \n"
        return mystr
    def __len__(self):
        return len(self.voti)


    def calcolaMedia(self):

        '''
        restituisce il valore della media degli esami
        :return: valore numerico della media, oppure ValueError se non ci sono esami sostenuti
        '''
        #numEsami = len(self.voti) --> uguale a len(v)
        if len(self.voti) == 0:
            raise ValueError("Attenzione, lista esami vuota")

        v = [v1.punteggio for v1 in self.voti] #equivalente di un ciclo for normale --> creando una lista!!
        return  sum(v)/len(v)

    def getVotiByPunti(self, punti, lode):
        '''
        resistuisce una lista di esami con punteggio uguale a punti (e lode se applicabile)
        :param punti: variabile di tipo intero che rappresenta il punteggio
        :param lode: booleano che indica se presente la lode
        :return: lista di voti
        '''
        votiFiltrati = []
        for v in self.voti:
            if v.punteggio == punti and v.lode == lode:
                votiFiltrati.append(v)
        return votiFiltrati

    def getVotoByName(self, name):
        '''
        resistuisce il voto il cui campo materia è uguale a name
        :param name: stringa che indica il nome della materia
        :return: oggetto di tipo Voto
        '''
        for v in self.voti:
            if v.materia == name:
                return v



    def hasVoto(self, voto):
        '''
        questo metodo verifica se il libretto contiene già il voto "voto". Due voti sono considerati uguali se hanno
        lo stesso campo materia e lo stesso campo punteggio (voto formato da punteggio e lode)
        :param: voto: instanza dell'oggetto di tipo Voto
        :return: True se voto presente, False altrimenti
        '''
        for v in self.voti:
            if (v.materia == voto.materia and
                    v.punteggio == voto.punteggio and
                    v.lode == voto.lode):
                return True #quando lo trovo esco --> la traccia dice che dobbiamo vedere se ce n'è UNO
        return False

    def hasConflitto(self, voto):
        '''
        Questo metodo controlla che il voto "voto" non vada in conflitto con i voti
        già presenti nel libretto, consideriamo due voti in conflitto quando hanno lo stesso campo materia
        ma diverso punteggio e diversa lode
        :param voto: istanza dell'oggetto di tipo Voto
        :return: True se voto in conflitto, False altrimenti
        '''
        for v in self.voti:
            if (v.materia == voto.materia and
                not (v.punteggio == voto.punteggio and v.lode == voto.lode)):
                return True
        return False

    def copy(self):
        '''
        crea una nuova copia del libretto
        :return: istanza della classe Libretto
        '''
        nuovo = Libretto(self.proprietario, [])
        for v in self.voti:
            nuovo.append(v.copy())

        return nuovo

    def creaMigliorato(self):
        '''
        Crea un nuovo Oggetto libretto, in cui i voti sono migliorati secondo
        la seguente logica:
        se il voto è >= 18 e <24 aggiungo +1
        se il voto è >= 24 e <29 aggiunto +2
        se il voto è 29 aggiunto +1
        se il voto è 30 rimane 30
        :return: nuovo Libretto
        '''

        nuovo = self.copy()

        for v in nuovo.voti:
            if 18 <= v.punteggio < 24:
                v.punteggio += 1
            elif 24<= v.punteggio < 29:
                v.punteggio += 2
            elif v.punteggio== 29:
                v.punteggio = 30
        return nuovo


    def creaLIbOrdinatoPerMateria(self):
        '''
        crea un nuovo oggetto Libretto e lo ordina per materia
        :return: nuova istanza dell'oggetto Libretto
        '''
        nuovo = self.copy()
        nuovo.voti.sort(key = lambda v: v.materia)
        return nuovo

    def creaLibOrdinatoPerVoto(self):
        '''
        Creo un nuovo oggetto Libretto, e lo ordina per punteggio
        :return: nuova istanza dell'oggetto Libretto
        '''
        nuovo = self.copy()
        nuovo.voti.sort(key = lambda v: (v.punteggio, v.lode),reverse = True)
        return nuovo

    def cancellaInferiori(self, punteggio):
        '''
        Questo metodo agisce sul libretto corrente, eliminando tutti i voti inferiori
        al parametro punteggio
        :param punteggio: intero indicante il valore minimo accettato
        :return: Null
        '''
        #nuovo = []
        #for v in self.voti:
        #    if v.punteggio >= punteggio:
        #        nuovo.append(v)
        #self.voti = nuovo

        return[v for v in self.voti if v.punteggio >= punteggio]

def testVoto():
    print("Ho usato Voto in maniera standalone")
    v1 = Voto("Trasfigurazione", 24, "2022-02-13", False)
    v2 = Voto("Pozioni", 30, "2022-02-17", True)
    v3 = Voto("Difesa contro le arti oscure", 27, "2022-04-13", False)
    print(v1)

    mylib = Libretto(None, [v1, v2])
    print(mylib)
    mylib.append(v3)
    print(mylib)

if __name__ == "__main__":
    testVoto()



# class Voto:
#     def __init__(self, materia, punteggio, data, lode):
#         if  punteggio == 30:
#             self.materia = materia
#             self.punteggio = punteggio
#             self.data = data
#             self.lode = lode
#         elif punteggio < 30:
#             self.materia = materia
#             self.punteggio = punteggio
#             self.data = data
#             self.lode = False
#         else:
#             raise ValueError(f"Attenzione, non posso creare un voto con punteggio {punteggio}")
#     def __str__(self):
#         if self.lode:
#             return f"In {self.materia} hai preso {self.punteggio} e lode il {self.data}"
#         else:
#             return f"In {self.materia} hai preso {self.punteggio} il {self.data}"

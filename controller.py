from scuola import Student
from view import View
from Voto.voto import Libretto, Voto
import flet as ft


class Controller:

    def __init__(self, v: View):
        self._view = v
        self._student = Student(nome="Harry", cognome="Potter", eta=11, capelli="castani", occhi="azzurri", casa="Grifondoro", animale="civetta", incantesimo="Expecto Patronum")

        self._model = Libretto(self._student, [])
        self._fillLibretto()

    def handleAdd(self, e):
        nome = self._view._txtInName.value
        if nome == "":
            self._view._txtOut.controls.append(ft.Text("Attenzione il campo nome non può essere vuoto", color ="red"))
            return

        punti = self._view._ddVoto.value
        if punti is None:
            self._view._txtOut.controls.append(ft.Text("Attenzione il campo voto non può essere vuoto", color ="red"))
            return

        data = self._view._dp.value
        if data is None:
            self._view._txtOut.controls.append(ft.Text("Attenzione selezionare una data", color = "red"))
            return
        if punti == "30L":
            self._model.append(Voto(nome, 30, f"{data.year}-{data.month}-{data.day}", True))

        else:
            self._model.append(Voto(nome, punti, f"{data.year}-{data.month}-{data.day}", False))


    def getStudent(self):
        '''
        Restituisce informazioni dello studente usando il __str__ dell'oggetto
        student
        :return:
        '''
        return str(self._student)

    def handlePrint(self, e):
        self._view._txtOut.controls.append(ft.Text(str(self._model)))
        self._view._page.update()

    def _fillLibretto(self):
        self._model.append(Voto("Trasfigurazione", 24, "2022-02-13", False))
        self._model.append(Voto("Babbanologia", 30, "2022-02-17", False))
        self._model.append(Voto("Pozioni", 21, "2022-02-18", False))
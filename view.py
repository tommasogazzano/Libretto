import datetime

import flet as ft

class View:
    def __init__(self, page: ft.Page):
        self._btnAdd = None
        self._btnCal = None
        self._dp = None
        self._ddVoto = None
        self._txtInName = None
        self._btnPrint = None
        self._student = None
        self._title = None
        self._txtOut = None
        self._btnIn = None
        self._controller = None
        self._txtIn = None
        self._page = page


    def loadInterface(self):
        '''
        In questo metodo definiamo e carichiamo tutti i controlli dell'interfaccia
        :return:
        '''
        #self._page.bgColor = "white"
        self._title = ft.Text("Libretto Voti", color= "red", size= 24)
        self._student = ft.Text(self._controller.getStudent(), color="brown")
        row1 = ft.Row([self._title], alignment=ft.MainAxisAlignment.CENTER)
        row2 = ft.Row([self._student], ft.MainAxisAlignment.END)

        self._txtIn = ft.TextField(label="Name")
        self._btnIn = ft.ElevatedButton("Add", on_click=self._controller.handleAdd)

        #RIGA DEI CONTROLLI
        self._txtInName = ft.TextField(label="Name",
                                       hint_text="Inserisci il nome dell'esame",
                                       width=300)
        self._ddVoto = ft.Dropdown(label="Voto",width=120)
        self._fillDDVoto()
        self._dp = ft.DatePicker(
            first_date= datetime.datetime(2022, 1, 1),
            last_date= datetime.datetime(2022, 12, 31),
            on_change = lambda e: print(f"Giorno selezionato:{self._dp.value} "),
            on_dismiss = lambda e: print(f"Data non selezionata"),
        )
        self._btnCal = ft.ElevatedButton("Pick Data", icon=ft.icons.CALENDAR_MONTH,
                                         on_click= lambda e: self._page.open(self._dp))
        self._btnAdd = ft.ElevatedButton("Add", on_click=self._controller.handleAdd)
        self._btnPrint = ft.ElevatedButton("Print", on_click=self._controller.handlePrint)

        row3 = ft.Row(controls = [self._txtInName, self._ddVoto, self._btnCal,
                                  self._btnAdd, self._btnPrint],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._txtOut = ft.ListView(expand=True)
        self._page.add(row1, row2, row3, self._txtOut)

        pass

    def setController(self, c):
        self._controller = c

    def _fillDDVoto(self):
        for i in range(18,31):
            self._ddVoto.options.append(ft.dropdown.Option(str(i)))
        self._ddVoto.options.append(ft.dropdown.Option("30L"))

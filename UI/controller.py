import time

import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDDProvider(self):
        providers = self._model._providers
        for p in providers:
            self._view._DD_provider.options.append(ft.dropdown.Option(data=p, text=p, on_click=self._choice_provider))
        self._view.update_page()




    def _choice_provider(self, e):
        if e.control.data is None:
            self._selected_provider = None
        else:
            self._selected_provider = e.control.data



    def handleGrafo(self, e):
        distanza = self._view._txtIn_distanza.value
        try:
            floatDistanza = float(distanza)
        except ValueError:
            self._view.txt_result1.controls.clear()
            self._view.txt_result1.controls.append(ft.Text(f"Errore, inserire un valore numerico in 'Distanza'."))
            self._view.update_page()
            return
        self._model._crea_grafo(self._selected_provider, floatDistanza)
        nNodi, nArchi = self._model.get_dettagli_grafo()
        self._view.txt_result1.controls.clear()
        self._view.txt_result1.controls.append(ft.Text(f"Grafo correttamente creato. Il grafo ha {nNodi} nodi e {nArchi} archi."))
        self._view.update_page()

    def handleAnalisi(self, e):
        pass
    def handlePercorso(self, e):
        pass


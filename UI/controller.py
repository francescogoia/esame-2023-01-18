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
        self._view.txt_result1.controls.append(
            ft.Text(f"Grafo correttamente creato. Il grafo ha {nNodi} nodi e {nArchi} archi."))
        self._view._btn_analisi.disabled = False
        self._view._txtIn_stringa.disabled = False
        self._view._btn_percorso.disabled = False
        self._view._DD_target.disabled = False
        self._fillDDTarget()
        self._view.update_page()

    def handleAnalisi(self, e):
        most_vicini = self._model.get_most_vicini()
        self._view.txt_result1.controls.append(ft.Text(f"Vertici con più vicini:"))
        for v in most_vicini:
            self._view.txt_result1.controls.append(ft.Text(f"{v[0]}, #vicini = {v[1]}"))
        self._view.update_page()

    def _fillDDTarget(self):
        for l in self._model._nodes:
            self._view._DD_target.options.append(ft.dropdown.Option(data=l, text=l, on_click=self._choice_target))
        self._view.update_page()

    def _choice_target(self, e):
        if e.control.data is None:
            self._selected_target = None
        else:
            self._selected_target = e.control.data


    def handlePercorso(self, e):
        stringa = self._view._txtIn_stringa.value
        path = self._model._handle_percorso(self._selected_target, stringa)
        self._view.txt_result2.controls.clear()
        self._view.txt_result2.controls.append(ft.Text(f"Trovato percorso di lunghezza {len(path)}:"))
        for p in path:
            self._view.txt_result2.controls.append(ft.Text(f"{p[0]} --> {p[1]}"))
        self._view.update_page()

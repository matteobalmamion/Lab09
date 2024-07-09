import flet as ft

from model.tratta import Tratta


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizza(self,e):
        self._view._txt_result.controls.clear()
        graph=self._model.analizza(int(self._view._txtIn.value))
        self._view._txt_result.controls.append(ft.Text(f"Sono stati trovati {graph.number_of_nodes()} Aereoporti"))
        self._view._txt_result.controls.append(ft.Text(f"Sono stati trovate {graph.number_of_edges()} Tratte"))
        for u,v in graph.edges:
            self._view._txt_result.controls.append(ft.Text(f"{u}-{v}: {graph.edges[u,v]['distance']}"))
        self._view.update_page()

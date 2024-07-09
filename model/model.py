import networkx as nx
from database.DAO import DAO
from model.tratta import Tratta


class Model:
    def __init__(self):
        self._graph=None
        self._flights=None
        self._airports=DAO.getAllAirports()


    def analizza(self,distanceMin):
        self._flights=DAO.getAllFlights()
        self._graph=nx.Graph()
        for tupla in self._flights:
            somma=0
            for flight in self._flights[tupla]:
                somma+=flight.distance
            distance=somma/len(self._flights[tupla])
            tratta=Tratta(self._airports[tupla[0]],self._airports[tupla[1]],distance)
            if distance>=distanceMin:
                self._graph.add_edge(tratta.start,tratta.arrive,distance=tratta.distance)
                self._graph.add_node(tratta.start)
                self._graph.add_node(tratta.arrive)
                print(tratta)
        return self._graph


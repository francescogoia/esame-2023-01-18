import copy

import networkx as nx

from database.DAO import DAO
from geopy import distance


class Model:
    def __init__(self):
        self._idMap = {}
        self._grafo = nx.Graph()
        self._providers = DAO.getAllProviders()

    def _crea_grafo(self, provider, soglia):
        self._nodes = DAO.getAllLocation(provider)
        self._grafo.add_nodes_from(self._nodes)
        # creare oggetti Location che abbiano lat e long, e poi verificare se due Location sono collegate verificando la distanza tra di loro con doppio for
        for u in self._nodes:
            for v in self._nodes:
                if u != v:
                    coord_u = (u.Latitude, u.Longitude)
                    coord_v = (v.Latitude, v.Longitude)
                    distanza_u_v = distance.distance(coord_u, coord_v).km
                    if distanza_u_v <= soglia:
                        self._grafo.add_edge(u, v, weight=distanza_u_v)

    def get_dettagli_grafo(self):
        return len(self._grafo.nodes), len(self._grafo.edges)

import copy
import random

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

    def get_most_vicini(self):
        vicini = []
        for n in self._nodes:
            n_vicini = nx.degree(self._grafo, n)
            vicini.append((n, n_vicini))
        vicini.sort(key=lambda x: x[1], reverse=True)
        n_max = vicini[0][1]
        result = []
        self._nodi_most_vicini = []
        for v in vicini:
            if v[1] == n_max:
                result.append(v)
                self._nodi_most_vicini.append(v[0])
            else:
                return result
        return result

    def _handle_percorso(self, target, stringa):
        self.get_most_vicini()
        self._bestPath = []
        partenza = self._nodi_most_vicini[random.randint(0, len(self._nodi_most_vicini) -1)]
        self._ricorsione(partenza, [], target, stringa)

        return self._bestPath

    def _ricorsione(self, nodo, parziale, target, stringa):
        if len(parziale) > len(self._bestPath) and parziale[-1][1] == target:
                self._bestPath = copy.deepcopy(parziale)
        vicini = self._grafo.neighbors(nodo)
        for v in vicini:
            if stringa not in v.Location and self._filtro_nodi(v, parziale):
                parziale.append((nodo, v))
                self._ricorsione(v, parziale, target, stringa)
                parziale.pop()

    def _filtro_nodi(self, v, parziale):
        for a in parziale:
            if a[0] == v or a[1] == v:
                return False
        return True



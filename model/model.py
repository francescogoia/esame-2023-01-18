import copy

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._idMap = {}
        self._grafo = nx.Graph()
        self._providers = DAO.getAllProviders()

    def _crea_grafo(self, provider, distanza):
        self._nodes = DAO.getAllNodes(provider)
        self._grafo.add_nodes_from(self._nodes)
        # creare oggetti Location che abbiano lat e long, e poi verificare se due Location sono collegate verificando la distanza tra di loro con doppio for


    def get_dettagli_grafo(self):
        return len(self._grafo.nodes), len(self._grafo.edges)

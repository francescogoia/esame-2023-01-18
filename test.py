from model.model import Model

myModel = Model()
myModel._crea_grafo("QPL", 7)
print(myModel.get_dettagli_grafo())
most_vicini = myModel.get_most_vicini()
for v in most_vicini:
    print(v)
path = myModel._handle_percorso(4, 2)
print("Percorso lungo: ", len(path))
for p in path:
    print(p)

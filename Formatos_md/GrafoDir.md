#este codigo cre un grafo dirigido con 4 vertices (a, b, c, d) y 4 aristas ()
import mathplotlib.pyplot as plt
#Creamos un grafo vacio
grafo = {}

#agregamos vertices al grafo
grafo["A"] = ["B", "C"]
grafo["B"] = ["D"]
grafo["C"] = ["D"]
grafo["D"] = []

#imprimimos el grafo
print("Grafos:")
for vertice, adyecente in grafo.items():
    print(f"Vertice {vertice} -> {adyecente}")
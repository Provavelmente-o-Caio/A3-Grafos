import math
import itertools
from src.Vertice import Vertice
from src.Aresta import Aresta
from src.GrafoNaoDirigido import GrafoNaoDirigido


def lawler(G: GrafoNaoDirigido):
    n = int(math.pow(2, G.qtdVertices()))
    cores_subconjuntos = [0] * n
    subconjuntos = []
    subconjuntos.append(listarSubconjuntos(G.get_vertices()))

    for subconjunto in subconjuntos:
        if len(subconjunto) != 0:
            index_subconjunto = subconjuntos.index(subconjunto)
            cores_subconjuntos[index_subconjunto] = math.inf
            GG = GrafoNaoDirigido(subconjunto)
            subconjuntos_maximais = listarConjuntosIndependentesMaximais(GG)
            for subconjunto_maximal in subconjuntos_maximais:
                subconjunto_menor = [x for x in subconjunto if x not in subconjunto_maximal]
                index_subconjunto_maximal = subconjuntos.index(subconjunto_menor)
                if cores_subconjuntos[index_subconjunto_maximal] + 1 < cores_subconjuntos[index_subconjunto]:
                    cores_subconjuntos[index_subconjunto] = cores_subconjuntos[index_subconjunto_maximal] + 1
    return cores_subconjuntos


def listarConjuntosIndependentesMaximais(G: GrafoNaoDirigido):
    s = listarSubconjuntos(G.get_vertices())
    s.reverse()
    conjuntos_independentes = []
    for subset in s:
        c = True
        for v in subset:
            for u in subset:
                if G.haAresta(v.get_index(),u.get_index()):
                    c = False
                    break
        if c:
            conjuntos_independentes.append(subset)
    return conjuntos_independentes

def listarSubconjuntos(vertices):
    subconjuntos = []
    for i in range(1, len(vertices)+1):
        subconjunto = [list(x) for x in itertools.combinations(vertices, i)]
        subconjuntos.extend(subconjunto)

    return subconjuntos

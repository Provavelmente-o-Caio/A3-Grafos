from src.GrafoNaoDirigido import GrafoNaoDirigido
from queue import Queue

INF = 2147483647
NIL = 0

def hopcroftKarp(g: GrafoNaoDirigido):
    verticesDeCadaLado = g.qtdVertices() // 2

    # Armazena o index do vértice com o qual o vértice
    # do lado esquerdo está pareado
    pares_x = [0 for _ in range(verticesDeCadaLado + 1)]

    # Armazena o index do vértice com o qual o vértice do
    # lado direito está pareado
    pares_y = [0 for _ in range(verticesDeCadaLado + 1)]

    # Armazena as distancias dos vérticos do lado esquerdo
    distancias = [0 for _ in range(verticesDeCadaLado + 1)]

    # Armazena quantos pareamentos são possiveis
    result = 0

    # Fique atualizando o resultado enquanto ainda tiver caminhos aumentantes
    while bfs(g, pares_x, pares_y, distancias):
        # Encontre um vértice livre
        for u in range(1,verticesDeCadaLado +1):
            # Verificar se tem um caminho aumentante alternante a partir do vértice atual
            if pares_x[u] == NIL and dfs(g, pares_x, pares_y, u, distancias):
                result += 1

    # Printar resultado da função
    printHopcroft(result, pares_x[1:])

# Função que retorna se há um caminho aumentante ou não
def bfs(g:GrafoNaoDirigido, pares_x, pares_y, distancias):
    Q = Queue()
    for u in range(1, g.qtdVertices()//2 + 1):
        # Enfileirar vértices livres
        if pares_x[u] == NIL:
            distancias[u] = 0
            Q.put(u)
        else:
            distancias[u] = INF

    # Setar distancia para NIL/null como infinito
    distancias[NIL] = INF

    while not Q.empty():
        u = Q.get()

        if distancias[u] < distancias[NIL]:
            for v in g.vizinhos(u):
                v_index = v.get_index() - g.qtdVertices()//2
                # Se o caminho ainda não tiver sido explorado, adicionar à fila
                if distancias[pares_y[v_index]] == INF:
                    distancias[pares_y[v_index]] = distancias[u] + 1
                    Q.put(pares_y[v_index])

    # Se conseguimos voltar para NIL usando caminhos alternando
    # então há um caminho aumentante
    return distancias[NIL] != INF

# Retorna se há um caminho aumentante alternante a partir do vertice u
def dfs(g:GrafoNaoDirigido, pares_x, pares_y, u, distancias):
    if u != NIL:
        for v in g.vizinhos(u):
            v_num = v.get_index()
            v_index = v_num - g.qtdVertices() // 2
            if distancias[pares_y[v_index]] == distancias[u] + 1:
                if dfs(g, pares_x, pares_y, pares_y[v_index], distancias):
                    pares_y[v_index] = u
                    pares_x[u] = v_num
                    return True
        # Se nao há caminho aumentante a partir de u
        distancias[u] = INF
        return False
    return True

def printHopcroft(result, pares_x):
    print(result)

    strings_pares = list()
    for i in range(len(pares_x)):
        strings_pares.append(f"{i+1}-{pares_x[i]}")
    print(", ".join(strings_pares))

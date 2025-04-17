# a_star.py

import heapq
from constants import CUSTO_TERRENO, POKEMON_BONUS

def heuristica(a, b):
    """Distância Manhattan"""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_estrela(mapa, inicio, objetivo, pokemons_capturados):
    """Busca o melhor caminho de inicio até objetivo."""
    fila = []
    heapq.heappush(fila, (0, inicio))
    veio_de = {}    # Guarda de onde o agente veio para reconstruir o caminho no final.
    custo_atual = {inicio: 0}   # Armazena o custo para chegar em cada célula

    while fila: #Loop Principal
        _, atual = heapq.heappop(fila) #enquanto tiver nós ele remove o de menor custo estimado

        if atual == objetivo:  
            caminho = []
            total_custo = 0

            while atual in veio_de:
                caminho.append(atual)
                anterior = veio_de[atual]
                terreno = mapa[atual[0]][atual[1]]
                custo = CUSTO_TERRENO[terreno]

                # Aplica bônus de pokémon se tiver
                for p in pokemons_capturados:
                    if terreno in POKEMON_BONUS.get(p, {}):
                        custo -= POKEMON_BONUS[p][terreno]
                        custo = max(custo, 1)

                total_custo += custo
                atual = anterior

            caminho.reverse()
            return caminho, total_custo

        x, y = atual
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            vizinho = (x + dx, y + dy)
            if 0 <= vizinho[0] < len(mapa) and 0 <= vizinho[1] < len(mapa[0]): #garante q esta dentro do mapa
                terreno = mapa[vizinho[0]][vizinho[1]]
                custo = CUSTO_TERRENO[terreno]

                for p in pokemons_capturados:
                    if terreno in POKEMON_BONUS.get(p, {}):
                        custo -= POKEMON_BONUS[p][terreno]
                        custo = max(custo, 1)

                novo_custo = custo_atual[atual] + custo

                if vizinho not in custo_atual or novo_custo < custo_atual[vizinho]:
                    custo_atual[vizinho] = novo_custo
                    prioridade = novo_custo + heuristica(vizinho, objetivo)
                    heapq.heappush(fila, (prioridade, vizinho))
                    veio_de[vizinho] = atual

    return [], float('inf')  

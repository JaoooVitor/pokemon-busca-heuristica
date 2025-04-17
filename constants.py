# Custos base dos terrenos
CUSTO_TERRENO = {
    "G": 10,
    "A": 100,
    "C": 120,
    "M": 120,
    "V": 150,
}

# Reduções de custo ao capturar pokémons específicos
POKEMON_BONUS = {
    "agua": {"A": 10},
    "eletrico": {"C": 12},
    "voador": {"M": 12},
    "fogo": {"V": 15},
    "grama": {"G": 0},
}

# Tamanho do mapa (42x42)
TAMANHO_MAPA = 42
TAMANHO_CELULA = 15

# Radar da Pokédex
ALCANCE_RADAR = 4

# Quantidade de pokémons por tipo
QUANTIDADE_POKEMONS = {
    "grama": 20,
    "agua": 10,
    "voador": 8,
    "fogo": 6,
    "eletrico": 4,
}

# Tipos de terrenos (para carregar sprites)
TIPOS_TERRENO = ["G", "A", "M", "C", "V"]

from collections import OrderedDict

INSIGNIAS_POSICOES = OrderedDict([
    ((2, 4), "alma"),
    ((2, 19), "trovao"),
    ((4, 36), "vulcao"),
    ((19, 14), "cascata"),
    ((22, 2), "arcoiris"),
    ((37, 19), "lama"),
    ((20, 39), "terra"),
    ((40, 32), "rocha"),
])

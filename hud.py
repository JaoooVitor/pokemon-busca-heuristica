# hud.py

import pygame
from constants import TAMANHO_CELULA

def desenhar_hud(tela, agente, sprite_pokemon, sprite_insignias):
    """Desenha informações no topo da tela: HUD com tempo, custo, pokémons e insígnias."""
    font = pygame.font.SysFont("Arial", 18)
    branco = (255, 255, 255)
    preto = (0, 0, 0)

    pygame.draw.rect(tela, preto, (0, 0, 42 * TAMANHO_CELULA, 50))

    # ⏱️ Tempo
    tempo_texto = font.render(f"Tempo: {agente.tempo_decorrido():.1f}s", True, branco)
    tela.blit(tempo_texto, (10, 5))

    # 💰 Custo total
    custo_texto = font.render(f"Custo: {agente.custo_total:.0f}", True, branco)
    tela.blit(custo_texto, (10, 25))

    # 🎖️ Insígnias
    for i in range(agente.insignias_conquistadas):
        tela.blit(sprite_insignias[i], (180 + i * 25, 8))

    # 🧩 Pokémons capturados
    base_x = 450
    for i, tipo in enumerate(agente.contador_pokemons):
        if agente.contador_pokemons[tipo] > 0:
            tela.blit(sprite_pokemon[tipo], (base_x + i * 30, 8))

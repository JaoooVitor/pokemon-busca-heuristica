import pygame
from constants import TAMANHO_CELULA, INSIGNIAS_POSICOES

HUD_ALTURA = 50  # precisa ser igual ao usado no main.py

def desenhar_hud(tela, agente, sprite_pokemon, sprite_insignias):
    """Desenha informações no topo da tela: HUD com tempo, custo, pokémons e insígnias."""
    font = pygame.font.SysFont("Arial", 16)
    branco = (255, 255, 255)
    preto = (0, 0, 0)

    # Fundo da HUD
    pygame.draw.rect(tela, preto, (0, 0, 42 * TAMANHO_CELULA, HUD_ALTURA))

    # ⏱️ Tempo
    tempo_texto = font.render(f"Tempo: {agente.tempo_decorrido():.1f}s", True, branco)
    tela.blit(tempo_texto, (10, 5))

    # 💰 Custo total
    custo_texto = font.render(f"Custo: {agente.custo_total:.0f}", True, branco)
    tela.blit(custo_texto, (10, 25))

    # 🎖️ Insígnias conquistadas
    for i, pos in enumerate(agente.insignias_conquistadas):
        nome = INSIGNIAS_POSICOES.get(pos)
        if nome:
            tela.blit(sprite_insignias[nome], (180 + i * (TAMANHO_CELULA + 5), 8))

    # 🧩 Pokémons capturados
    base_x = 420
    i = 0
    for tipo in agente.contador_pokemons:
        qtd = agente.contador_pokemons[tipo]
        if qtd > 0:
            x = base_x + i * (TAMANHO_CELULA + 10)
            y = 8
            tela.blit(sprite_pokemon[tipo], (x, y))

            if qtd > 1:
                qtd_texto = font.render(f"x{qtd}", True, branco)
                tela.blit(qtd_texto, (x + TAMANHO_CELULA // 2, y + TAMANHO_CELULA // 2 - 2))

            i += 1

# tela_relatorio.py

import pygame
from constants import TAMANHO_CELULA, TAMANHO_MAPA

def mostrar_tela_final(tela, agente, sprite_pokemon, sprite_insignias):
    font_titulo = pygame.font.SysFont("Arial", 32, True)
    font = pygame.font.SysFont("Arial", 20)
    tela.fill((0, 0, 0))

    branco = (255, 255, 255)
    azul = (0, 150, 255)

    # Título
    titulo = font_titulo.render("🏁 Fim da Jornada Pokémon!", True, branco)
    tela.blit(titulo, (80, 20))

    # Tempo e custo
    tempo = font.render(f"⏱️ Tempo: {agente.tempo_decorrido():.2f} s", True, branco)
    custo = font.render(f"💰 Custo total: {agente.custo_total:.0f}", True, branco)
    tela.blit(tempo, (80, 80))
    tela.blit(custo, (80, 110))

    # Insígnias
    insig_titulo = font.render("🎖️ Insígnias conquistadas:", True, branco)
    tela.blit(insig_titulo, (80, 150))
    for i in range(agente.insignias_conquistadas):
        tela.blit(sprite_insignias[i], (300 + i * 30, 145))

    # Pokémons capturados
    poke_titulo = font.render("🧩 Pokémons capturados:", True, branco)
    tela.blit(poke_titulo, (80, 190))
    i = 0
    for tipo, qtd in agente.contador_pokemons.items():
        if qtd > 0:
            tela.blit(sprite_pokemon[tipo], (300 + i * 30, 185))
            i += 1

    # Caminho pontilhado (em mini mapa)
    mini = 6  # tamanho da célula no mini mapa
    offset_x = 80
    offset_y = 250
    for pos in agente.historico_caminho:
        x = offset_x + pos[1] * mini
        y = offset_y + pos[0] * mini
        pygame.draw.rect(tela, azul, (x, y, 2, 2))

    mapa_texto = font.render("🗺️ Caminho percorrido (mini mapa):", True, branco)
    tela.blit(mapa_texto, (80, offset_y - 30))

    pygame.display.flip()

    # Espera uma tecla
    esperando = True
    while esperando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                esperando = False
            elif event.type == pygame.KEYDOWN:
                esperando = False

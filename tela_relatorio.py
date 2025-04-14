import pygame
from constants import TAMANHO_CELULA, TAMANHO_MAPA, INSIGNIAS_POSICOES

def mostrar_tela_final(tela, agente, sprite_pokemon, sprite_insignias):
    font_titulo = pygame.font.SysFont("Arial", 32, True)
    font = pygame.font.SysFont("Arial", 18)
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

    # Insígnias conquistadas
    insig_titulo = font.render("🎖️ Insígnias conquistadas:", True, branco)
    tela.blit(insig_titulo, (80, 150))
    i = 0
    for pos in agente.insignias_conquistadas:
        nome = INSIGNIAS_POSICOES.get(pos)
        if nome:
            x = 300 + i * (TAMANHO_CELULA + 15)
            y = 145
            tela.blit(sprite_insignias[nome], (x, y))
            i += 1

    # Pokémons capturados
    poke_titulo = font.render("🧩 Pokémons capturados:", True, branco)
    tela.blit(poke_titulo, (80, 190))
    i = 0
    for tipo, qtd in agente.contador_pokemons.items():
        if qtd > 0:
            x = 300 + i * (TAMANHO_CELULA + 10)
            y = 185
            tela.blit(sprite_pokemon[tipo], (x, y))
            if qtd > 1:
                qtd_texto = font.render(f"x{qtd}", True, branco)
                tela.blit(qtd_texto, (x + TAMANHO_CELULA // 2, y + TAMANHO_CELULA // 2))
            i += 1

    # Caminho pontilhado (mini mapa)
    mini = 6
    offset_x = 80
    offset_y = 250
    mapa_texto = font.render("🗺️ Caminho percorrido (mini mapa):", True, branco)
    tela.blit(mapa_texto, (offset_x, offset_y - 30))
    for pos in agente.historico_caminho:
        x = offset_x + pos[1] * mini
        y = offset_y + pos[0] * mini
        pygame.draw.rect(tela, azul, (x, y, 2, 2))

    pygame.display.flip()

    # Espera uma tecla
    esperando = True
    while esperando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                esperando = False
            elif event.type == pygame.KEYDOWN:
                esperando = False

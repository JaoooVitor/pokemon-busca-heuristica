import pygame
from constants import TAMANHO_CELULA, TAMANHO_MAPA, INSIGNIAS_POSICOES
from collections import defaultdict
import math


def mostrar_tela_final(tela, agente, sprite_insignias):
    clock = pygame.time.Clock()
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
    tela.blit(tempo, (80, 70))
    tela.blit(custo, (80, 100))

    # Mini mapa com trajeto + animação da Pokébola
    mini = 5
    offset_x = 80
    offset_y = 150
    caminho = agente.historico_caminho[:]
    pokeball = pygame.image.load("assets/pokeball.png")
    pokeball = pygame.transform.scale(pokeball, (10, 10))

    passo_idx = 0
    animando = True
    while animando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                animando = False

        tela.fill((0, 0, 0))
        tela.blit(titulo, (80, 20))
        tela.blit(tempo, (80, 70))
        tela.blit(custo, (80, 100))

        mapa_texto = font.render("🗌️ Caminho percorrido:", True, branco)
        tela.blit(mapa_texto, (offset_x, offset_y - 25))

        for pos in caminho[:passo_idx]:
            x = offset_x + pos[1] * mini
            y = offset_y + pos[0] * mini
            pygame.draw.rect(tela, azul, (x, y, 2, 2))

        if passo_idx < len(caminho):
            pos = caminho[passo_idx]
            x = offset_x + pos[1] * mini
            y = offset_y + pos[0] * mini
            tela.blit(pokeball, (x, y))
            passo_idx += 1
        else:
            animando = False

        # Insígnias com efeito de brilho
        insig_y = 420
        for i, pos in enumerate(agente.insignias_conquistadas):
            nome = INSIGNIAS_POSICOES.get(pos)
            if nome:
                img = sprite_insignias[nome]
                scale = 1.2 + 0.1 * math.sin(pygame.time.get_ticks() / 200 + i)
                size = int(TAMANHO_CELULA * scale)
                insig = pygame.transform.scale(img, (size, size))
                tela.blit(insig, (80 + i * (size + 10), insig_y))

        # Pokémons capturados (os 5 mais capturados)
        contador = defaultdict(int)
        for p in agente.pokemons_capturados:
            if isinstance(p, dict):
                contador[p["tipo"]] += 1
            else:
                contador[p] += 1

        top_5 = sorted(contador.items(), key=lambda x: -x[1])[:5]

        centro = (650, 320)
        raio = 130
        for i, (tipo, qtd) in enumerate(top_5):
            angulo = i * (360 / len(top_5))
            rad = math.radians(angulo)
            px = int(centro[0] + raio * math.cos(rad)) - 30
            py = int(centro[1] + raio * math.sin(rad)) - 30

            poke_sprite = pygame.image.load(f"assets/pokemon_{tipo}_tela.png")
            poke_resized = pygame.transform.scale(poke_sprite, (60, 60))
            tela.blit(poke_resized, (px, py))

            quant = font.render(f"x{qtd}", True, branco)
            tela.blit(quant, (px + 15, py + 55))

        # Jogador no centro
        jogador_img = pygame.image.load("assets/jogador_tela.png")
        jogador_img = pygame.transform.scale(jogador_img, (100, 100))
        tela.blit(jogador_img, (centro[0] - 50, centro[1] - 50))

        pygame.display.flip()
        clock.tick(20)

    # Espera final
    esperando = True
    while esperando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                esperando = False

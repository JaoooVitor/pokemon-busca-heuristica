import pygame
import ctypes
import os
from constants import TAMANHO_MAPA, TAMANHO_CELULA, ALCANCE_RADAR, CORES_TERRENO, INSIGNIAS_POSICOES
from environment import Ambiente
from hud import desenhar_hud
from tela_relatorio import mostrar_tela_final

HUD_ALTURA = 50

# === MENU INTERATIVO ===
print("=== Escolha o agente ===")
print("[1] Agente Simples")
print("[2] Agente Inteligente")
escolha = input("> ")

if escolha == "1":
    from agent_simples import Agente
    print("🟢 Rodando com agente SIMPLES...\n")
elif escolha == "2":
    from agent_inteligente import Agente
    print("🔵 Rodando com agente INTELIGENTE...\n")
else:
    print("Opção inválida.")
    exit()

# === INICIALIZAÇÃO ===
pygame.init()
tela = pygame.display.set_mode((TAMANHO_MAPA * TAMANHO_CELULA, TAMANHO_MAPA * TAMANHO_CELULA + HUD_ALTURA))
pygame.display.set_caption("Agente Pokémon - Busca Heurística com A*")

# === FORÇA A JANELA PARA O FOCO ===
try:
    hwnd = pygame.display.get_wm_info()['window']
    ctypes.windll.user32.ShowWindow(hwnd, 5)
    ctypes.windll.user32.SetForegroundWindow(hwnd)
except:
    pass

# === SPRITES ===
def carregar_sprites():
    sprite_jogador = pygame.image.load("assets/jogador.png")
    sprite_jogador = pygame.transform.scale(sprite_jogador, (TAMANHO_CELULA, TAMANHO_CELULA))

    tipos_pokemon = ["agua", "fogo", "voador", "eletrico", "grama"]
    sprite_pokemon = {
        tipo: pygame.transform.scale(pygame.image.load(f"assets/pokemon_{tipo}.png"), (TAMANHO_CELULA, TAMANHO_CELULA))
        for tipo in tipos_pokemon
    }

    nomes_insignias = ["alma", "trovao", "vulcao", "cascata", "arcoiris", "lama", "terra", "rocha"]
    sprite_insignias = {
        nome: pygame.transform.scale(pygame.image.load(f"assets/insignia_{nome}.png"), (TAMANHO_CELULA, TAMANHO_CELULA))
        for nome in nomes_insignias
    }

    return sprite_jogador, sprite_pokemon, sprite_insignias

sprite_jogador, sprite_pokemon, sprite_insignias = carregar_sprites()
ambiente = Ambiente()
agente = Agente(ambiente)

rodando = True
pokemons_visiveis = []

while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    novos = ambiente.radar_pokedex(agente.posicao, ALCANCE_RADAR)
    for p in novos:
        if p not in pokemons_visiveis:
            pokemons_visiveis.append(p)

    alvo, tipo = agente.decidir_proxima_acao(ambiente, pokemons_visiveis)

    if tipo == "fim":
        rodando = False
        continue

    caminho, _ = agente.mover_para(alvo, ambiente)

    for passo in caminho:
        tela.fill((255, 255, 255))

        # Desenha o mapa com offset
        for x in range(TAMANHO_MAPA):
            for y in range(TAMANHO_MAPA):
                letra = ambiente.mapa[x][y]
                cor = CORES_TERRENO.get(letra, (255, 255, 255))
                pygame.draw.rect(tela, cor, (
                    y * TAMANHO_CELULA,
                    x * TAMANHO_CELULA + HUD_ALTURA,
                    TAMANHO_CELULA,
                    TAMANHO_CELULA
                ))

        # Caminho do agente
        for i in range(1, len(caminho)):
            p1 = caminho[i - 1]
            p2 = caminho[i]
            pygame.draw.line(
                tela,
                (200, 200, 200),
                (p1[1] * TAMANHO_CELULA + TAMANHO_CELULA // 2, p1[0] * TAMANHO_CELULA + TAMANHO_CELULA // 2 + HUD_ALTURA),
                (p2[1] * TAMANHO_CELULA + TAMANHO_CELULA // 2, p2[0] * TAMANHO_CELULA + TAMANHO_CELULA // 2 + HUD_ALTURA),
                2
            )

        # Pokémons visíveis
        for pos in pokemons_visiveis:
            tipo_poke = ambiente.pokemons_na_posicao.get(pos)
            if tipo_poke:
                tela.blit(sprite_pokemon[tipo_poke], (
                    pos[1] * TAMANHO_CELULA,
                    pos[0] * TAMANHO_CELULA + HUD_ALTURA
                ))

        # Insígnias visíveis
        for pos, nome in INSIGNIAS_POSICOES.items():
            if pos not in agente.insignias_conquistadas:
                tela.blit(sprite_insignias[nome], (
                    pos[1] * TAMANHO_CELULA,
                    pos[0] * TAMANHO_CELULA + HUD_ALTURA
                ))

        # Jogador
        tela.blit(sprite_jogador, (
            passo[1] * TAMANHO_CELULA,
            passo[0] * TAMANHO_CELULA + HUD_ALTURA
        ))

        # HUD
        desenhar_hud(tela, agente, sprite_pokemon, sprite_insignias)

        pygame.display.flip()
        pygame.time.delay(50)

    if tipo == "pokemon":
        pokemons_visiveis.remove(alvo)
        agente.capturar_pokemon(alvo, ambiente)
    elif tipo == "ginasio":
        agente.conquistar_insignia(alvo)
        ambiente.ginasios.remove(alvo)

mostrar_tela_final(tela, agente, sprite_pokemon, sprite_insignias)
pygame.quit()

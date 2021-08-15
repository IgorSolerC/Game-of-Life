"""
Igor Soler Cavalcanti (15/08/2021)

Implementação do Game of Life de Conway
"""

import pygame as pg
import variaveis as var
import grid

# Inicia a engine
pg.init()

# Nome da Janela
pg.display.set_caption("Game of Life") # Titulo da janela

# Constantes
pausado = True

# Variaveis
tabuleiro = grid.Tabuleiro(0, 50)

# Velocidade
frame = 0
velocidadeAtt = 30
velocidadeAttSelecao = 1

# Mouse Over
mouseOverRect = 0
mouseOverRectLinha = 0
mouseOverRectColuna = 0

# Texto
fonte = pg.font.SysFont('Bahnschrift ', 20)

# ---------- MAIN LOOP ---------- 
jogoRodando = True
clock = pg.time.Clock() # Framerate (Velocidade que a tela da update)

while jogoRodando:
    # --------- MAIN EVENT (O usuario entrou algum input?)
    for evento in pg.event.get(): # User entrou um input
        if evento.type == pg.QUIT: # Se o jogador fechou o jogo
            jogoRodando = False

        if evento.type == pg.MOUSEMOTION:
            # Ve se o mouse está em cima de algum grid
            mouseOverRect = 0
            for coluna in range(len(tabuleiro.rects)):
                for linha in range(len(tabuleiro.rects)):
                    grid = tabuleiro.rects[linha][coluna]
                    gridDentro = tabuleiro.grid[linha][coluna]
                    if grid.collidepoint(pg.mouse.get_pos()):
                        break
                    else:
                        mouseOverRect = 0
                if grid.collidepoint(pg.mouse.get_pos()):
                    mouseOverRect = grid
                    mouseOverRectLinha = linha
                    mouseOverRectColuna = coluna
                    break
                
        if evento.type == pg.MOUSEBUTTONDOWN: # Jogador apertou botão do mouse
            mouseBotEsquerdo = pg.mouse.get_pressed()[0] # Update estado BEM
            mouseBotMeio = pg.mouse.get_pressed()[1] # Update estado BMM
            mouseBotDireito = pg.mouse.get_pressed()[2] # Update estado BDM
            if mouseBotEsquerdo:
                if pausado and mouseOverRect != 0:
                    if tabuleiro.grid[mouseOverRectLinha][mouseOverRectColuna] == 1:
                        tabuleiro.grid[mouseOverRectLinha][mouseOverRectColuna] = 0
                    else:
                        tabuleiro.grid[mouseOverRectLinha][mouseOverRectColuna] = 1
        if evento.type == pg.KEYDOWN:
            if pg.key.get_pressed()[pg.K_RETURN]:
                if pausado:
                    pausado = False
                else:
                    pausado = True
            if pg.key.get_pressed()[pg.K_r]:
                tabuleiro.grid = tabuleiro.definirGrid(var.quantidadeGrid)
                tabuleiro.randomGrid()
            if pg.key.get_pressed()[pg.K_1]:
                velocidadeAtt = 30
                velocidadeAttSelecao = 1
            if pg.key.get_pressed()[pg.K_2]:
                velocidadeAtt = 15
                velocidadeAttSelecao = 2
            if pg.key.get_pressed()[pg.K_3]:
                velocidadeAtt = 7
                velocidadeAttSelecao = 3
            if pg.key.get_pressed()[pg.K_4]:
                velocidadeAtt = 2
                velocidadeAttSelecao = 4
            if pg.key.get_pressed()[pg.K_c]:
                tabuleiro.salvaGrid()
            if pg.key.get_pressed()[pg.K_v]:
                tabuleiro.lerGrid()
                
    # --------- GAME LOGIC (O que ocorre entre frames)
    frame += 1
    if not pausado:
        if frame % velocidadeAtt == 0:
            frame = 0
            tabuleiro.attGrid()
            
    hudVelocidade = fonte.render("Velocidade: {0}".format(velocidadeAttSelecao), 1, var.BRANCO) # Update informação velocidade texto
    hudPausado = fonte.render("Pausado: {0}".format(pausado), 1, var.BRANCO) # Update informação velocidade texto
    hudControleVel = fonte.render("Alterar Vel: 1 a 4", 1, var.BRANCO) # Update informação velocidade texto
    hudControleRandom = fonte.render("Aleatorizar: R", 1, var.BRANCO) # Update informação velocidade texto
    hudControlePause = fonte.render("Pause: ENTER", 1, var.BRANCO) # Update informação velocidade texto
    hudControlaInteracao = fonte.render("Interagir: BEM", 1, var.BRANCO) # Update informação velocidade texto
    hudControleSalvar = fonte.render("Salvar tela: C", 1, var.BRANCO) # Update informação velocidade texto
    hudControleCarregar = fonte.render("Carregar tela: V", 1, var.BRANCO) # Update informação velocidade texto
    
    # --------- DRAWING CODE (Update da tela)
    var.TELA.fill(var.CINZA)

    # Draw Texto
    var.TELA.blit(hudVelocidade, (20, 0)) # Draw Velocidade
    var.TELA.blit(hudPausado, (20, 25))# Draw Status Pausado
    var.TELA.blit(hudControleVel, (170, 0)) # Draw Controles Velocidade
    var.TELA.blit(hudControleRandom, (170, 25)) # Draw Controles Random
    var.TELA.blit(hudControlePause, (340, 0)) # Draw Controles Pause
    var.TELA.blit(hudControlaInteracao, (340, 25)) # Draw Controles interagir
    var.TELA.blit(hudControleSalvar, (490, 0)) # Draw Controles Salvar
    var.TELA.blit(hudControleCarregar, (490, 25)) # Draw Controles Carregar
    
    tabuleiro.draw()
    # --------- UPDATE SCREEN
    pg.display.flip()
    
    # --------- FRAME RATE
    clock.tick(var.FRAMES_POR_SEGUNDO)

# Para a engine quando o jogo para
pg.quit()

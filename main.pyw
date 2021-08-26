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

# Objetos
tabuleiro = grid.Tabuleiro(50)

# Variaveis
frame = 0
velocidadeAtt = 30
velocidadeAttSelecao = 1

mouseOverRect = 0
mouseOverRectLinha = 0
mouseOverRectColuna = 0

# Texto
fonte = pg.font.SysFont('Bahnschrift ', 20)

hudVelocidade = fonte.render("Velocidade: {0}".format(velocidadeAttSelecao), 1, var.BRANCO)
hudPausado = fonte.render("Pausado: {0}".format(pausado), 1, var.BRANCO)
hudControleVel = fonte.render("Alterar Vel: 1 a 4", 1, var.BRANCO) 
hudControleRandom = fonte.render("Aleatorizar: R", 1, var.BRANCO)
hudControlePause = fonte.render("Pause: ENTER", 1, var.BRANCO) 
hudControlaInteracao = fonte.render("Interagir: BEM", 1, var.BRANCO) 
hudControleSalvar = fonte.render("Salvar tela: C", 1, var.BRANCO) 
hudControleCarregar = fonte.render("Carregar tela: V", 1, var.BRANCO) 

# ---------- MAIN LOOP ---------- 
jogoRodando = True
clock = pg.time.Clock() # Framerate (Velocidade que a tela da update)

while jogoRodando:
    # --------- MAIN EVENT (O usuario entrou algum input?)
    for evento in pg.event.get(): # User entrou um input
        if evento.type == pg.QUIT: # Se o jogador fechou o jogo
            jogoRodando = False

        if evento.type == pg.MOUSEMOTION:
            mousePos = pg.mouse.get_pos()
            if tabuleiro.rectGeral.collidepoint(mousePos) and pausado: # Se o mouse está no tabueiro e o jogo está pausado
                # Salva o retangulo no grid que ele esta em cima
                mouseOverRect = 1 # Mouse está em cima de um retangulo
                mouseOverRectLinha = tabuleiro.colisaoParticoesX(mousePos)
                mouseOverRectColuna = tabuleiro.colisaoParticoesY(mousePos)
            else:
                mouseOverRect = 0 # Mouse não está em cima de um retangulo
                
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
                hudPausado = fonte.render("Pausado: {0}".format(pausado), 1, var.BRANCO) # Update informação pausado texto
            if pg.key.get_pressed()[pg.K_r]:
                tabuleiro.randomGrid()
            if pg.key.get_pressed()[pg.K_1]:
                velocidadeAtt = 30
                velocidadeAttSelecao = 1
                # Update informação velocidade texto
                hudVelocidade = fonte.render("Velocidade: {0}".format(velocidadeAttSelecao), 1, var.BRANCO)
            if pg.key.get_pressed()[pg.K_2]:
                velocidadeAtt = 13
                velocidadeAttSelecao = 2
                # Update informação velocidade texto
                hudVelocidade = fonte.render("Velocidade: {0}".format(velocidadeAttSelecao), 1, var.BRANCO)
            if pg.key.get_pressed()[pg.K_3]:
                velocidadeAtt = 4
                velocidadeAttSelecao = 3
                # Update informação velocidade texto
                hudVelocidade = fonte.render("Velocidade: {0}".format(velocidadeAttSelecao), 1, var.BRANCO)
            if pg.key.get_pressed()[pg.K_4]:
                velocidadeAtt = 1
                velocidadeAttSelecao = 4
                # Update informação velocidade texto
                hudVelocidade = fonte.render("Velocidade: {0}".format(velocidadeAttSelecao), 1, var.BRANCO)
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

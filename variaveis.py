import pygame as pg

TAMANHO_TELA = (640, 690) # Tamanho da Janela (x, y)
TELA = pg.display.set_mode(TAMANHO_TELA) # Gera tela

FRAMES_POR_SEGUNDO = 60

# Cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
CINZA = (50, 50, 50)
quantidadeGrid = 64 # Só aceita potencias de 2 maiores que 1

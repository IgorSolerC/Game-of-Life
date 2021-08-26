import pygame as pg
import variaveis as var
from random import randint
import numpy as np
import copy

# Classe que gerencia o tabuleiro do jogo
class Tabuleiro():
    def __init__(self, gapY):
        # Constantes
        self.VIVO = 1   # Representa uma celula viva
        self.MORTO = 0  # Representa uma celula morta
        

        # Distancia entre o tabuleiro e as bordas no eixo Y
        self.gapY = gapY 

        # self.grid salva o estado de cada posição do tabuleiro.
        # Ex: Se self.grid[0][0] == self.MORTO
        # então a primeira celula do tabuleiro está morta
        self.grid = self.definirGrid(var.quantidadeGrid)

        # gridFuturo é o grid que guarda o próximo estado do programa
        # Ele existe para que proximo estado possa ser armazernado progressivamente
        # sem interferir no grid original até que o gridFuturo esteja completo
        self.gridFuturo = self.definirGrid(var.quantidadeGrid)

        # Define o tamanho dos retangulos que compões o grid
        self.tamanhoRectGrid = (var.TAMANHO_TELA[0])/len(self.grid)

        # Armazena um tabuleiro vazio como o tabuleiro salvo
        self.saveGrid = self.definirGrid(var.quantidadeGrid)

        # Define a hitbox de cada retangulo 
        self.rects = self.definirRect()

        # Retangulo do tabuleiro inteiro
        self.rectGeral = pg.Rect((0, gapY), (self.tamanhoRectGrid*var.quantidadeGrid, self.tamanhoRectGrid*var.quantidadeGrid))

    def salvaGrid(self):
        # Salva o estado atual do grid
        self.saveGrid = copy.deepcopy(self.grid)
        """
        # Esse código é utilizado para gerar um arquivo de texto
        # que guarda o estado atual do tabuleiro.

        arquivo = open("gridSalvos.txt", "w")
        for x in range(var.quantidadeGrid):
            for y in range(var.quantidadeGrid):
                if y > 0:
                    arquivo.write(",")
                arquivo.write(str(self.grid[x][y]))
            arquivo.write("\n")
        arquivo.close()
        """

    def lerGrid(self):
        # Transforma o grid em um estado salvo previamente
        self.grid = copy.deepcopy(self.saveGrid)
        """
        # Esse código é utilizado para ler um arquivo de texto
        # que guarda o estado atual do tabuleiro e substituir o atual
        # tabuleiro pelo lido.

        arquivo = open("gridSalvos.txt", "r")
        gridLido = []
        for x in range(var.quantidadeGrid):
            linha = arquivo.readline().split(",")
            for elemento in range(len(linha)):
                linha[elemento] = int(linha[elemento])
            gridLido.append(linha)
        arquivo.close()
        self.grid = gridLido
        """
        
    def randomGrid(self):
        # Gera uma matriz aleatoria de celulas vivas ou mortas
        # Esssa matriz tem o mesmo tamanho que o grid
        # A matriz é utilizada como grid para gerar um tabuleiro aleatorio
        for x in range(var.quantidadeGrid):
            for y in range(var.quantidadeGrid):
                estadoRandom = randint(0, 1)
                if estadoRandom == 1:
                    self.grid[x][y] = self.VIVO
                else:
                    self.grid[x][y] = self.MORTO

    def definirGrid(self, tamanho):
        # Define a matriz (Preenchida de células mortas) que representa o grid
        matriz = [[self.MORTO for linhas in range(tamanho)] for colunas in range(tamanho)]
        return matriz
    
    def definirRect(self):
        # Define a hitbox de cada retangulo armazenando um objeto pg.Rect()
        # em cada posição de uma matriz com o tamanho do grid.
        # Cada Rect() nesta matriz representa a interface gráfica do valor
        # de mesmo índice armazenado na matriz self.grid

        # Cria uma matriz do tamanho do grid
        rects = self.definirGrid(var.quantidadeGrid)
        for linha in range(len(self.grid)):
            for coluna in range(len(self.grid[linha])):
                # A posição X e Y de cada Rect() é igual ao seu index X ou Y
                # multiplicado pelo tamanho dos retangulos.

                # O eixo Y é acrescido ao valor self.gapY, para que os retangulos
                # sejam desenhados mais para baixo, dando espaço para que o menu
                # seja desenhado.
                x = linha*self.tamanhoRectGrid
                y = coluna*self.tamanhoRectGrid + self.gapY
                rects[linha][coluna] = pg.Rect((x, y), (self.tamanhoRectGrid, self.tamanhoRectGrid))
        return rects

    def draw(self):
        # Desenha as células na tela
        for linha in range(len(self.rects)):
            for coluna in range(len(self.rects[linha])):
                if self.grid[linha][coluna] == self.MORTO:
                    # Desenha Células Mortas
                    pg.draw.rect(var.TELA, var.PRETO, self.rects[linha][coluna], 0)
                else:
                    # Desenha Células Vivas
                    pg.draw.rect(var.TELA, var.BRANCO, self.rects[linha][coluna], 0)
                # Desenha Borda das células
                pg.draw.rect(var.TELA, var.CINZA, self.rects[linha][coluna], 1)

        """
        # Esse código desenha as linhas utilizadas como base para o algoritmo de divisão para conquistar
        
        for passo in range(1, 6):
            tamParticaoX = self.tamanhoRectGrid*var.quantidadeGrid//(2**passo)
            tamParticaoY = self.tamanhoRectGrid*var.quantidadeGrid
            particao = pg.Rect((0, self.gapY), (tamParticaoX, tamParticaoY))
            pg.draw.rect(var.TELA, (255, 40*passo, 0), particao, 1)

        for passo in range(1, 6):
            tamParticaoX = self.tamanhoRectGrid*var.quantidadeGrid
            tamParticaoY = self.tamanhoRectGrid*var.quantidadeGrid//(2**passo)
            particao = pg.Rect((0, self.gapY), (tamParticaoX, tamParticaoY))
            pg.draw.rect(var.TELA, (0, 40*passo, 255), particao, 1)
        """

    def attGrid(self):
        # Limpa o grif futuro
        for x in range(var.quantidadeGrid):
            for y in range(var.quantidadeGrid):
                self.gridFuturo[x][y] = 0

        # Verifica cada célula do tabuleiro
        for x in range(var.quantidadeGrid):
            for y in range(var.quantidadeGrid):
                numBrancos = 0
                # Checa a quantidade de células vivas em volta da célula
                if y != var.quantidadeGrid-1 and x != var.quantidadeGrid-1:
                    if self.grid[x+1][y+1] == self.VIVO:
                        numBrancos += 1
                if y != var.quantidadeGrid-1 and x != 0:
                    if self.grid[x-1][y+1] == self.VIVO:
                        numBrancos += 1
                if y != 0 and x != 0:
                    if self.grid[x-1][y-1] == self.VIVO:
                        numBrancos += 1
                if y != 0 and x != var.quantidadeGrid-1:
                    if self.grid[x+1][y-1] == self.VIVO:
                        numBrancos += 1
                if y != var.quantidadeGrid-1:
                    if self.grid[x][y+1] == self.VIVO:
                        numBrancos += 1
                if x != var.quantidadeGrid-1:
                    if self.grid[x+1][y] == self.VIVO:
                        numBrancos += 1
                if y != 0:
                    if self.grid[x][y-1] == self.VIVO:
                        numBrancos += 1
                if x != 0:
                    if self.grid[x-1][y] == self.VIVO:
                        numBrancos += 1

                # Aplica as condições para matar, manter viva ou criar uma célula
                if numBrancos == 3:
                    self.gridFuturo[x][y] = self.VIVO
                elif numBrancos > 3 or numBrancos < 2:
                    self.gridFuturo[x][y] = self.MORTO
                elif self.grid[x][y] == self.VIVO:
                    self.gridFuturo[x][y] = self.VIVO

        # Substitui o grid pelo grid futuro
        self.grid = copy.deepcopy(self.gridFuturo)

    # Checa se indice X do retangulo em que o mouse colide
    # divisão para conquistar
    def colisaoParticoesX(self, mousePos, x=0, index=0, passo=1):
        # Caso base. Todos os indices X foram checados
        if 2**(passo-1) == var.quantidadeGrid:
            return index
        else:
            tamParticaoX = self.tamanhoRectGrid*var.quantidadeGrid//(2**passo)
            tamParticaoY = self.tamanhoRectGrid*var.quantidadeGrid
            particao = pg.Rect((x, self.gapY), (tamParticaoX, tamParticaoY))
            
            if not particao.collidepoint(mousePos):
                index += var.quantidadeGrid//(2**passo)
                
            passo += 1
            x = self.tamanhoRectGrid * index
            return self.colisaoParticoesX(mousePos, x, index, passo)

    # Checa se indice Y do retangulo em que o mouse colide
    # divisão para conquistar
    def colisaoParticoesY(self, mousePos, y=0, index=0, passo=1):
        # Caso base. Todos os indices Y foram checados
        if 2**(passo-1) == var.quantidadeGrid:
            return index
        else:
            tamParticaoX = self.tamanhoRectGrid*var.quantidadeGrid
            tamParticaoY = self.tamanhoRectGrid*var.quantidadeGrid//(2**passo)
            particao = pg.Rect((0, y + self.gapY), (tamParticaoX, tamParticaoY))
            
            if not particao.collidepoint(mousePos):
                index += var.quantidadeGrid//(2**passo)
                
            passo += 1
            y = self.tamanhoRectGrid * index
            return self.colisaoParticoesY(mousePos, y, index, passo)


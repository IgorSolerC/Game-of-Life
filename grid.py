import pygame as pg
import variaveis as var
from random import randint
import numpy as np
import copy

class Tabuleiro():
    def __init__(self, gapX, gapY):
        self.contador = 0
        self.VIVO = 1
        self.MORTO = 0
        self.gapX = gapX
        self.gapY = gapY

        self.grid = self.definirGrid(var.quantidadeGrid)
        
        if var.TAMANHO_TELA[0] < var.TAMANHO_TELA[1]:
            indexTela = 0
            self.tamanhoGrid = int((var.TAMANHO_TELA[indexTela]-self.gapX)/len(self.grid))
        else:
            indexTela = 1
            self.tamanhoGrid = int((var.TAMANHO_TELA[indexTela]-self.gapY)/len(self.grid))

        self.saveGrid = self.definirGrid(var.quantidadeGrid)
        self.rects = self.definirRect()

    def salvaGrid(self):
        self.saveGrid = copy.deepcopy(self.grid)
        """
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
        self.grid = copy.deepcopy(self.saveGrid)
        """
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
        for x in range(var.quantidadeGrid):
            for y in range(var.quantidadeGrid):
                estadoRandom = randint(0, 1)
                if estadoRandom == 1:
                    self.grid[x][y] = self.VIVO
                else:
                    self.grid[x][y] = self.MORTO

    def definirGrid(self, tamanho):
        matriz = [[self.MORTO for linhas in range(tamanho)] for colunas in range(tamanho)]
        return matriz
    
    def definirRect(self):
        rects = self.definirGrid(var.quantidadeGrid)
        for linha in range(len(self.grid)):
            for coluna in range(len(self.grid[linha])):
                x = coluna*self.tamanhoGrid + self.gapX
                y = linha*self.tamanhoGrid + self.gapY
                rects[linha][coluna] = pg.Rect((x, y), (self.tamanhoGrid, self.tamanhoGrid))
        return rects

    def draw(self):
        for linha in range(len(self.rects)):
            for coluna in range(len(self.rects[linha])):
                if self.grid[linha][coluna] == self.MORTO:
                    pg.draw.rect(var.TELA, var.PRETO, self.rects[linha][coluna], 0) # HIT BOX
                else:
                    pg.draw.rect(var.TELA, var.BRANCO, self.rects[linha][coluna], 0)
                pg.draw.rect(var.TELA, var.CINZA, self.rects[linha][coluna], 1) # linhas
    def attGrid(self):
        self.gridFuturo = self.definirGrid(var.quantidadeGrid)
        for x in range(var.quantidadeGrid):
            for y in range(var.quantidadeGrid):
                numBrancos = 0
                # Checa posições
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

                # Consequencias
                if numBrancos == 3:
                    self.gridFuturo[x][y] = self.VIVO
                elif numBrancos > 3 or numBrancos < 2:
                    self.gridFuturo[x][y] = self.MORTO
                elif self.grid[x][y] == self.VIVO:
                    self.gridFuturo[x][y] = self.VIVO
        self.grid = copy.deepcopy(self.gridFuturo)



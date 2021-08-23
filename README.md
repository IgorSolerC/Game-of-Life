# Game of Life

<!-- LOGO -->
<p align="center">
  <a href="https://github.com/IgorSolerC/Game-of-Life">
    <img src="Imagens/ConwayLogo.png" alt="Logo">
  </a>
  
  <h3 align="center">Implementação em Python do Jogo da Vida de Conway</h3>
</p>

<!-- TABELA DE CONTEUDO -->
<details open="open">
  <summary>Conteúdos</summary>
  <ol>
    <li>
      <a href="#sobre-o-projeto">Sobre o Projeto</a>
      <ul>
        <li><a href="#criado-com">Criado com</a></li>
      </ul>
      <ul>
        <li><a href="#regras">Regras</a></li>
      </ul>
    </li>
    <li>
      <a href="#como-utilizar">Como utilizar</a>
      <ul>
        <li><a href="#download">Download</a></li>
      </ul>
      <ul>
        <li><a href="#comandos">Comandos</a></li>
      </ul>
    </li>
  </ol>
</details>  

# Sobre o Projeto

O Jogo da Vida de conway é descrito com frequencia como um jogo de zero jogadores.

Este jogo é uma simulação de células que podem morrer ou viver com base em simples condições. Este jogo se tornou famoso por conta da complexidade das criações que podem ser feitas com estas simples condições.

Esta implementação foi feita em Python como forma de estudo.

## Criado com

O pacote [PyGame](https://www.pygame.org/) foi utilizado para o desenvolvimento de toda a interface gráfica deste projeto.

## Regras

Neste Jogo, células vivem e morrem em um tabuleiro com tamanho de 50x50. A cada passo do jogo determinadas células permanem vivas, outras morrem e outras nascem.

Uma célula viva neste jogo é representada como um quadrado branco, já uma morta é representada como um quadrado preto.

As condições de vida ou morte de uma célula são dependentes do estado dos vizinhos desta célula. Os vizinhos de uma célula são as 8 outras células em volta desta, ou seja, as células que estão em contato direto com ela.

Para que uma célula viva ou morra ela deve passar pelas seguintes condições:
* Morre

   Uma célula morre se não é vizinha de pelo menos 2 células vivas, ou se é vizinha de mais de 3 células vivas.
   
* Vive

  Uma célula viva continua neste estado se é vizinha de 2 ou 3 outras células vivas.
* Nasce

  Uma célula morta se torna uma célula viva caso seja vizinha de exatamente 3 células vivas

# Como utilizar

## Download



## Comandos

* Adicionar e Remover células

Ao apertar com o botão esquerdo do mouse em cima de uma célula no tabuleiro quando o jogo está pausado, o estado da célula clicada é alterado (de vivo para morto ou de morto para vivo)

<img src="Imagens/GifConway1.gif" width="200" height="200" />
<img src="Imagens/GifConway2.gif" width="200" height="200" />
<img src="Imagens/GifConway3.gif" width="200" height="200" />
<img src="Imagens/GifConway4.gif" width="400" height="400" />
<img src="Imagens/GifConway5.gif" width="200" height="200" />
<img src="Imagens/GifConway6.gif" width="200" height="200" />

#importa o pygame e sys
# o pygame é uma biblioteca para criar jogos em python
# o sys é uma biblioteca para interagir com o sistema operacional
import pygame,sys

from game import Game #importa a classe Game do arquivo game.py
from cores import Colors #importa a classe Colors do arquivo cores.py

pygame.init() #inicializa o pygame


title_font = pygame.font.Font(None, 40)	#cria uma fonte para o texto
score_surface = title_font.render("Score", True, Colors.white)	#cria uma superfície para o texto "Score"
next_surface = title_font.render("Next", True, Colors.white)	#cria uma superfície para o texto "Next"
game_over_surface = title_font.render("GAME OVER", True, Colors.white)	#cria uma superfície para o texto "GAME OVER"

score_rect = pygame.Rect(320, 55, 170, 60)	#cria um retângulo para o texto "Score"
next_rect = pygame.Rect(320, 215, 170, 180)	#cria um retângulo para o texto "Next"

screen = pygame.display.set_mode((500, 620))	#cria uma tela de 500x620 pixels
pygame.display.set_caption("Python Tetris")		#define o título da tela como "Python Tetris"

clock = pygame.time.Clock()	#cria um clock para controlar os quadrados por segundo

game = Game()	#cria um objeto da classe Game

GAME_UPDATE = pygame.USEREVENT #define um evento de atualização do jogo
pygame.time.set_timer(GAME_UPDATE, 200)	#define o tempo de atualização do jogo como 200ms

while True:	#loop principal do jogo
	for event in pygame.event.get():	#pega todos os eventos do pygame
		if event.type == pygame.QUIT:	#se o usuario fechar a tela o jogo fecha
			pygame.quit()	#fecha o pygame
			sys.exit() 	#sai do programa
		if event.type == pygame.KEYDOWN:	#se o usuario apertar uma tecla
			if game.game_over == True:	#se o jogo estiver acabado
				game.game_over = False	#reinicia o jogo
				game.reset()	
			if event.key == pygame.K_LEFT and game.game_over == False:	#se o jogo não estiver acabado e o usuario apertar a tecla esquerda
				game.move_left()	#move o bloco para a esquerda
			if event.key == pygame.K_RIGHT and game.game_over == False:	#se o jogo não estiver acabado e o usuario apertar a tecla direita
				game.move_right()	#move o bloco para a direita
			if event.key == pygame.K_DOWN and game.game_over == False:	#se o jogo não estiver acabado e o usuario apertar a tecla para baixo
				game.move_down()	#move o bloco para baixo
				game.update_score(0, 1)	#aumenta a pontuação
			if event.key == pygame.K_UP and game.game_over == False:	#se o jogo não estiver acabado e o usuario apertar a tecla para cima
				game.rotate() 	#roda o bloco
		if event.type == GAME_UPDATE and game.game_over == False:	#se o jogo não estiver acabado
			game.move_down()	#aumenta a pontuação

	#Desenhando os elementos na tela
	score_value_surface = title_font.render(str(game.score), True, Colors.white)
	#desenhando o valor da pontuação
	screen.fill(Colors.dark_blue)	#preenche a tela com a cor azul escuro
	screen.blit(score_surface, (365, 20, 50, 50))	#desenha o texto "Score" na tela
	screen.blit(next_surface, (375, 180, 50, 50))	#desenha o texto "Next" na tela

	if game.game_over == True:	#se o jogo estiver acabado
		screen.blit(game_over_surface, (320, 450, 50, 50))	#desenha o texto "GAME OVER" na tela

	pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)	#desenha um retângulo azul claro na tela
	screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx, 	
		centery = score_rect.centery))	#desenha o valor da pontuação na tela
	pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)	#desenha um retângulo azul claro na tela
	game.draw(screen)	#desenha o bloco atual na tela

	pygame.display.update()	#atualiza a tela
	clock.tick(60)	#controla a taxa de atualização da tela para 60 quadros por segundo


# Primeiro, eu criei uma grade de 20 linhas por 10 colunas, tipo um tabuleiro onde os blocos caem.
# Cada quadradinho da grade é como uma célula que pode estar vazia ou ocupada por um pedaço de bloco.
# Depois, eu defini sete blocos diferentes (aqueles L, J, I, O, S, T, Z que todo mundo conhece).
# Cada um tem uma forma específica e pode girar em até quatro posições. Quando o jogo começa,
# eu escolho um bloco aleatoriamente pra ser o atual e outro pra ser o próximo, que fica aparecendo ali do lado na tela.
# Aí, o bloco atual começa a descer sozinho, devagarzinho, a cada 0,2 segundos.
# Eu posso usar as teclas de seta pra controlar: esquerda e direita pra mover pros lados,
# baixo pra fazer descer mais rápido (e ganhar 1 pontinho), e cima pra girar o bloco.
# Antes de cada movimento, eu checo se ele é válido: o bloco não pode sair da grade nem bater em outros blocos já travados.
# Quando o bloco não consegue descer mais (porque bateu no fundo ou em outro bloco),
# eu o travo na grade, fixando suas partes nas células certas.
# Aí, eu pego o próximo bloco da fila e escolho outro aleatoriamente pra ser o próximo.
# Enquanto isso, eu fico de olho se alguma linha da grade ficou cheia.
# Se tiver, eu apago ela e deslizo todas as linhas de cima pra baixo.
# Isso me dá pontos: 100 por uma linha, 300 por duas, 500 por três.
# Se o novo bloco que entra não couber na grade (tipo, se a pilha chegou no topo), o jogo mostra "Game Over".
# Aí, é só apertar qualquer tecla pra zerar tudo e começar de novo.
# Pra deixar visual, eu uso o Pygame pra desenhar a grade, o bloco atual caindo, o próximo bloco do lado e a pontuação.
# Cada bloco tem uma cor diferente, tipo o I laranja e o T roxo, pra ficar bonito e fácil de entender.
# É basicamente isso: blocos caem, eu controlo, linhas somem, e tento não deixar a grade encher.
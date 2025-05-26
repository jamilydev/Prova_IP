from grid import Grid	# importa a classe Grid do arquivo grid.py
from blocks import *	# importa as classes dos blocos do arquivo blocks.py
import random	# importa a biblioteca random para gerar números aleatórios
import pygame	# importa a biblioteca pygame para criar jogos em python

class Game:	# classe que representa o jogo
	def __init__(self):	# construtor da classe Game
		self.grid = Grid()	# cria um objeto da classe Grid
		self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]	# cria uma lista de blocos
		self.current_block = self.get_random_block()	# cria um bloco aleatório para o jogador
		self.next_block = self.get_random_block()	# cria um bloco aleatório para o próximo bloco
		self.game_over = False	# indica se o jogo acabou
		self.score = 0	# inicializa a pontuação

	def update_score(self, lines_cleared, move_down_points):	# função que atualiza a pontuação do jogador
		if lines_cleared == 1:	# se o jogador limpar uma linha
			# adiciona 100 pontos à pontuação
			self.score += 100
		elif lines_cleared == 2:	# se o jogador limpar duas linhas
			# adiciona 300 pontos à pontuação
			self.score += 300
		elif lines_cleared == 3:	# se o jogador limpar três linhas
			# adiciona 500 pontos à pontuação
			self.score += 500
		self.score += move_down_points	# adiciona 1 ponto à pontuação para cada movimento para baixo

	def get_random_block(self):	# função que retorna um bloco aleatório
		# se a lista de blocos estiver vazia, cria uma nova lista de blocos
		if len(self.blocks) == 0:
			self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
		block = random.choice(self.blocks)
		self.blocks.remove(block)
		return block

	def move_left(self):	#função que move o bloco para a esquerda
		self.current_block.move(0, -1)	#move o bloco para a esquerda
		if self.block_inside() == False or self.block_fits() == False:	#verifica se o bloco está dentro da grade e se ele cabe na grade
			self.current_block.move(0, 1)	#se não estiver, move o bloco para a direita

	def move_right(self):	#função que move o bloco para a direita
		self.current_block.move(0, 1)	#move o bloco para a direita
		if self.block_inside() == False or self.block_fits() == False:	#verifica se o bloco está dentro da grade e se ele cabe na grade
			self.current_block.move(0, -1)	#se não estiver, move o bloco para a esquerda

	def move_down(self):	#função que move o bloco para baixo
		self.current_block.move(1, 0)	#move o bloco para baixo
		if self.block_inside() == False or self.block_fits() == False:	#verifica se o bloco está dentro da grade e se ele cabe na grade
			self.current_block.move(-1, 0)	#se não estiver, move o bloco para cima
			self.lock_block()

	def lock_block(self):	#função que trava o bloco na grade
		tiles = self.current_block.get_cell_positions()	# pega as posições das células do bloco
		for position in tiles:	# percorre as posições das células
			self.grid.grid[position.row][position.column] = self.current_block.id	# trava o bloco na grade
		self.current_block = self.next_block	# troca o bloco atual pelo próximo bloco
		self.next_block = self.get_random_block()	# cria um novo bloco aleatório
		rows_cleared = self.grid.clear_full_rows()	# verifica se o jogador limpou alguma linha
		if rows_cleared > 0:	# se o jogador limpou alguma linha
			self.update_score(rows_cleared, 0)	# atualiza a pontuação
		if self.block_fits() == False:	
			self.game_over = True # se o bloco não couber na grade, o jogo acaba

	def reset(self):	# função que reinicia o jogo
		self.grid.reset()	# reinicia a grade
		self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]	# cria uma nova lista de blocos
		self.current_block = self.get_random_block()	# cria um bloco aleatório para o jogador
		self.next_block = self.get_random_block()	# cria um bloco aleatório para o próximo bloco
		self.score = 0	# inicializa a pontuação

	def block_fits(self):	# função que verifica se o bloco cabe na grade
		tiles = self.current_block.get_cell_positions()	# pega as posições das células do bloco
		for tile in tiles:	# percorre as posições das células
			if self.grid.is_empty(tile.row, tile.column) == False:	# verifica se a célula está vazia
				return False	# se a célula não estiver vazia, o bloco não cabe na grade
		return True

	def rotate(self):	# função que rotaciona o bloco
		self.current_block.rotate()	# rotaciona o bloco
		if self.block_inside() == False or self.block_fits() == False:	# verifica se o bloco está dentro da grade e se ele cabe na grade
			self.current_block.undo_rotation()	# se não estiver, desfaz a rotação do bloco

	def block_inside(self):	# função que verifica se o bloco está dentro da grade
		tiles = self.current_block.get_cell_positions()	# pega as posições das células do bloco
		for tile in tiles:	# percorre as posições das células
			if self.grid.is_inside(tile.row, tile.column) == False:	# verifica se a célula está dentro da grade
				return False	# se a célula não estiver dentro da grade, o bloco não está dentro da grade
		return True

	def draw(self, screen):	# desenha o bloco atual e a grade na tela
		self.grid.draw(screen)		# desenha a grade na tela
		self.current_block.draw(screen, 11, 11)	# desenha o bloco atual na tela

		if self.next_block.id == 3:	# se o próximo bloco for um bloco "T"
			self.next_block.draw(screen, 255, 290)	# desenha o bloco "T" na tela
		elif self.next_block.id == 4:	# se o próximo bloco for um bloco "O"
			self.next_block.draw(screen, 255, 280)	# desenha o bloco "O" na tela
		else:	# para todos os outros blocos
			self.next_block.draw(screen, 270, 270)	# desenha o bloco na tela
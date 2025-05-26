from cores import Colors	#importa a classe Colors do arquivo cores.py
import pygame	#importa a biblioteca pygame
from posicao import Position	#importa a classe Position do arquivo posicao.py

class Block:	#classe que representa um bloco do jogo
	def __init__(self, id):	#construtor da classe
		self.id = id	#atributo que representa o id do bloco para que ele possa ser identificado
		self.cells = {}	#atributo que representa as células do bloco para que ele possa ser desenhado
		self.cell_size = 30	#tamanho de cada célula do bloco
		self.row_offset = 0	#deslocamento em relação à linha
		self.column_offset = 0	#deslocamento em relação à coluna
		self.rotation_state = 0	#estado de rotação do bloco
		self.colors = Colors.get_cell_colors()	#cores das células do bloco

	def move(self, rows, columns):	#função que move o bloco
		self.row_offset += rows		#desloca o bloco em relação à linha
		self.column_offset += columns	#desloca o bloco em relação à coluna

	def get_cell_positions(self):	#função que retorna as posições das células do bloco
		tiles = self.cells[self.rotation_state]	#pega as células do bloco de acordo com o estado de rotação
		moved_tiles = []	#lista que vai armazenar as células do bloco
		for position in tiles:	
			#cria uma nova posição para a célula do bloco de acordo com o deslocamento
			position = Position(position.row + self.row_offset, position.column + self.column_offset)	
			moved_tiles.append(position)
		return moved_tiles

	def rotate(self):	#função que rotaciona o bloco
		self.rotation_state += 1	#aumenta o estado de rotação do bloco
		#se o estado de rotação do bloco for maior que o número de células do bloco, volta para o estado 0
		if self.rotation_state == len(self.cells):	
			self.rotation_state = 0

	def undo_rotation(self):	#função que desfaz a rotação do bloco
		self.rotation_state -= 1
		if self.rotation_state == -1:
			self.rotation_state = len(self.cells) - 1

	def draw(self, screen, offset_x, offset_y):	#função que desenha o bloco na tela
		tiles = self.get_cell_positions()
		for tile in tiles:	
			tile_rect = pygame.Rect(offset_x + tile.column * self.cell_size, 
				offset_y + tile.row * self.cell_size, self.cell_size -1, self.cell_size -1)
			pygame.draw.rect(screen, self.colors[self.id], tile_rect)
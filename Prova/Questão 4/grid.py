import pygame	# importa a biblioteca pygame para criar jogos em python
from cores import Colors	# importa a classe Colors do arquivo cores.py

class Grid:	# classe que representa a grade do jogo
	def __init__(self):	# construtor da classe Grid
		# constrói a grade com 20 linhas e 10 colunas
		# e cada célula tem 30 pixels de tamanho
		# a grade é inicializada com 0, que representa uma célula vazia
		# e as cores das células são definidas pela classe Colors
		self.num_rows = 20	
		self.num_cols = 10
		self.cell_size = 30
		self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
		self.colors = Colors.get_cell_colors()

	def print_grid(self):	# função que imprime a grade no console
		for row in range(self.num_rows):	# percorre as linhas da grade
			for column in range(self.num_cols):	# percorre as colunas da grade
				print(self.grid[row][column], end = " ")	# imprime o valor da célula
			print()

	def is_inside(self, row, column):	# função que verifica se a célula está dentro da grade
		if row >= 0 and row < self.num_rows and column >= 0 and column < self.num_cols:	
			return True	
		return False

	def is_empty(self, row, column):	# função que verifica se a célula está vazia
		if self.grid[row][column] == 0:	# se a célula estiver vazia
			return True	
		return False

	def is_empty(self, row, column):	# função que verifica se a célula está vazia
		if self.grid[row][column] == 0:
			return True
		return False

	def is_row_full(self, row):	# função que verifica se a linha está cheia
		for column in range(self.num_cols):	# percorre as colunas da linha
			if self.grid[row][column] == 0:	# se a célula estiver vazia
				# a linha não está cheia
				return False
		return True

	def clear_row(self, row):	# limpa a linha, ou seja, coloca todas as células da linha como 0
		for column in range(self.num_cols):	# percorre as colunas da linha
			self.grid[row][column] = 0	# limpa a célula da linha

	def move_row_down(self, row, num_rows):	# move a linha para baixo, ou seja, coloca as células da linha na linha de baixo
		for column in range(self.num_cols):	
			self.grid[row+num_rows][column] = self.grid[row][column]	
			self.grid[row][column] = 0

	def clear_full_rows(self):	# percorre a grade de baixo para cima
		completed = 0	
		for row in range(self.num_rows-1, 0, -1):	# percorre as linhas da grade
			if self.is_row_full(row):	# se a linha estiver cheia
				self.clear_row(row)	# limpa a linha
				completed += 1	# aumenta o contador de linhas limpas
			elif completed > 0:	# se houver linhas limpas
				self.move_row_down(row, completed)	# move as linhas para baixo
		return completed

	def reset(self):	# reinicia a grade, ou seja, coloca todas as células como 0
		for row in range(self.num_rows):	# percorre as linhas da grade
			for column in range(self.num_cols):	# percorre as colunas da grade
				self.grid[row][column] = 0	# limpa a célula da linha

	def draw(self, screen):	# desenha a grade na tela
		for row in range(self.num_rows):# percorre as linhas da grade
			for column in range(self.num_cols):	# percorre as colunas da grade
				cell_value = self.grid[row][column]	# obtém o valor da célula
				cell_rect = pygame.Rect(column*self.cell_size + 11, row*self.cell_size + 11,
				self.cell_size -1, self.cell_size -1)	# cria um retângulo para a célula
				pygame.draw.rect(screen, self.colors[cell_value], cell_rect)# desenha a célula na tela
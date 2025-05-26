from block import Block # importa a classe Block do arquivo block.py
from posicao import Position    # importa a classe Position do arquivo posicao.py

class LBlock(Block):    # classe que representa o bloco L
	def __init__(self): # construtor da classe LBlock
		super().__init__(id = 1)   # chama o construtor da classe Block com o id 1
		self.cells = {  # dicionário que armazena as células do bloco L
			0: [Position(0, 2), Position(1, 0), Position(1, 1), Position(1, 2)],
			1: [Position(0, 1), Position(1, 1), Position(2, 1), Position(2, 2)],
			2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 0)],
			3: [Position(0, 0), Position(0, 1), Position(1, 1), Position(2, 1)]
		}
		self.move(0, 3) # move o bloco L para a posição inicial

class JBlock(Block):    # classe que representa o bloco J
    def __init__(self): # construtor da classe JBlock
        super().__init__(id = 2)  # chama o construtor da classe Block com o id 2
        self.cells = {  # dicionário que armazena as células do bloco J
            0: [Position(0, 0), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(0, 2), Position(1, 1), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 2)],
            3: [Position(0, 1), Position(1, 1), Position(2, 0), Position(2, 1)]
        }
        self.move(0, 3)

class IBlock(Block):    # classe que representa o bloco I
    def __init__(self): # construtor da classe IBlock
        super().__init__(id = 3)    # chama o construtor da classe Block com o id 3
        self.cells = {
            0: [Position(1, 0), Position(1, 1), Position(1, 2), Position(1, 3)],
            1: [Position(0, 2), Position(1, 2), Position(2, 2), Position(3, 2)],
            2: [Position(2, 0), Position(2, 1), Position(2, 2), Position(2, 3)],
            3: [Position(0, 1), Position(1, 1), Position(2, 1), Position(3, 1)]
        }
        self.move(-1, 3)

class OBlock(Block):    # classe que representa o bloco O
    def __init__(self): # construtor da classe OBlock
        super().__init__(id = 4)  # chama o construtor da classe Block com o id 4
        self.cells = {
            0: [Position(0, 0), Position(0, 1), Position(1, 0), Position(1, 1)]
        }
        self.move(0, 4)

class SBlock(Block):    # classe que representa o bloco S
    def __init__(self): # construtor da classe SBlock
        super().__init__(id = 5) # chama o construtor da classe Block com o id 5
        self.cells = {
            0: [Position(0, 1), Position(0, 2), Position(1, 0), Position(1, 1)],
            1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 2)],
            2: [Position(1, 1), Position(1, 2), Position(2, 0), Position(2, 1)],
            3: [Position(0, 0), Position(1, 0), Position(1, 1), Position(2, 1)]
        }
        self.move(0, 3)

class TBlock(Block):    # classe que representa o bloco T
    def __init__(self): # construtor da classe TBlock
        super().__init__(id = 6)  # chama o construtor da classe Block com o id 6
        self.cells = {
            0: [Position(0, 1), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 1)],
            3: [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 1)]
        }
        self.move(0, 3)

class ZBlock(Block):    # classe que representa o bloco Z
    def __init__(self): # construtor da classe ZBlock
        super().__init__(id = 7)  # chama o construtor da classe Block com o id 7
        self.cells = {
            0: [Position(0, 0), Position(0, 1), Position(1, 1), Position(1, 2)],
            1: [Position(0, 2), Position(1, 1), Position(1, 2), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(2, 1), Position(2, 2)],
            3: [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 0)]
        }
        self.move(0, 3)
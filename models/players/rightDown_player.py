class rightDownPlayer:
	def __init__(self, color):
		self.color = color


	def play(self, board):
		return self.getMostrightDown(board.valid_moves(self.color))

	def getMostrightDown(self, moves):
		maxRight = 0
		maxDown = 0
		retmove = None
		for move in moves:
			#print move
			rightMove = move.y
			downMove = move.x
			if rightMove > maxRight :
				maxRight = rightMove
				maxDown = downMove
				retmove = move
			elif rightMove == maxRight :
				if downMove > maxDown :
					maxDown = downMove
					retmove = move

		return retmove

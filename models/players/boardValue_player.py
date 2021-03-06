class BoardValuePlayer:
	def __init__(self, color):
		self.color = color

	def play(self, board):
		return self.getBestValue(board.valid_moves(self.color))

	def getBestValue(self,moves):
		retMoveValue = -50
		
		for move in moves:
			myMoveValue = self.heuristic(move)
			if myMoveValue > retMoveValue:
				retMoveValue = myMoveValue
				retMove = move		
		return retMove
		
	def heuristic(self,move):
		valueMatrix =	[[0, 0,  0,  0,  0,  0,  0,  0, 0,],\
									[0,200,-20, 20,  5,  5, 20,-20,200],\
									[0,-20,-40, -5, -5, -5, -5,-40,-20],\
									[0, 20, -5, 15,  3,  3, 15, -5, 20],\
									[0,  5, -5,  3,  3,  3,  3, -5,  5],\
									[0,  5, -5,  3,  3,  3,  3, -5,  5],\
									[0, 20, -5, 15,  3,  3, 15, -5, 20],\
									[0,-20,-40, -5, -5, -5, -5,-40,-20],\
									[0,200,-20, 20,  5,  5, 20,-20,200]]
									
		retValue = valueMatrix [move.x][move.y]
		return retValue

class MinMaxPlayer:
	BLACK, WHITE =  '@', 'o'
	def __init__(self, color):
		self.color = color

	def play(self, board):
		print 'minMax_player'
		return self.getBest(board,board.valid_moves(self.color),self.color,3)

	def getBest(self, board, moves, player_color, depthMax):
		bestMove = self.getMinMax(board, moves, player_color, depthMax, 0 )
		return bestMove[1]

	def getMinMax(self, board, moves, player_color, depthMax, currentDepth):

		if len(moves) == 0:
			if currentDepth % 2 == 0:
				retMove = [ 10000 ,None]
			else:
				retMove = [-10000 ,None]
			return retMove
			
		elif len(moves) == 1:
			retMove = [self.scoreBoard(board, player_color),moves[0]]
			return retMove

		elif currentDepth == depthMax:
			retMove = [self.scoreBoard( board, player_color), None]

			return retMove

		else:
			init = 0

			if currentDepth % 2 == 0:
				retMove = [ -10000 ,None]
			else:
				retMove = [ 10000 ,None]
				
			for move in moves:		
				
				cloneBoard = board.get_clone()
				cloneBoard.play(move,player_color)
				nextmoves =  cloneBoard.valid_moves(self._opponent(player_color))

				currentScore = self.scoreBoard( cloneBoard, player_color)
				if init == 0: 
					retMove = [currentScore,move]
					init += 1

				recursiveMove = self.getMinMax(cloneBoard,nextmoves,self._opponent(player_color),depthMax,currentDepth + 1)
			
				if currentDepth % 2 == 0: 	#Par sou eu = Max
					if recursiveMove[0] > retMove[0]:
						retMove[0] = recursiveMove[0]
						retMove[1] = move
				else:
					if recursiveMove[0] < retMove:
						retMove[0] = recursiveMove[0]
						retMove[1] = move
									
		return retMove


	def _opponent(self, color):
		if color == MinMaxPlayer.BLACK:
			retColor = MinMaxPlayer.WHITE
		else :
			retColor = MinMaxPlayer.BLACK
		
		return retColor


	def scoreBoard(self, board, player_color):
		white = 0
		black = 0
		totalScore = 0
		for i in range(1, 9):
			for j in range(1, 9):
				if board.board[i][j] == MinMaxPlayer.WHITE:
					white += self.heuristic([i,j])
				elif board.board[i][j] == MinMaxPlayer.BLACK:
					black += self.heuristic([i,j])
		if player_color == MinMaxPlayer.BLACK:
			totalScore = black
		else:
			totalScore = white
	
		return totalScore

	
	def heuristic(self,move):
		valueMatrix =	[[0, 0, 0,  0, 0, 0, 0,  0, 0,],\
									[0 ,100, 2, 8, 3, 3, 8,  2,100],\
									[0 ,  2, 1, 7, 4, 4, 7,  1,  2],\
									[0 ,  8, 7, 9, 5, 5, 9,  7,  8],\
									[0 ,  3, 4, 5, 0, 0, 5,  4,  3],\
									[0 ,  3, 4, 5, 0, 0, 5,  4,  3],\
									[0 ,  8, 7, 9, 5, 5, 9,  7,  8],\
									[0 ,  2, 1, 7, 4, 4, 7,  1,  2],\
									[0 ,100, 2, 8, 3, 3, 8,  2,100]]

		retValue = valueMatrix [move[0]][move[1]]
		return retValue		

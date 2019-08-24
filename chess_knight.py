class ChessKnight:

	def __init__(self):
		self.size = 8
		self.board = [[0 for j in range(0,self.size)] for i in range(0,self.size)]

	def get_board(self):
		return self.board

	def get_size(self):
		return self.size

	def is_position_in(self, pos):
		x, y = pos
		if x < 0 or x >= self.size:
			return False
		if y < 0 or y >= self.size:
			return False

		return True

	def get_functions(self):
		f1 = lambda x, y: (x - 2, y + 1)
		f2 = lambda x, y: (x - 2, y - 1)
		f3 = lambda x, y: (x + 2, y + 1)
		f4 = lambda x, y: (x + 2, y - 1)

		f5 = lambda x, y: (x + 1, y - 2)
		f6 = lambda x, y: (x - 1, y - 2)
		f7 = lambda x, y: (x + 1, y + 2)
		f8 = lambda x, y: (x - 1, y + 2)

		return [f1, f2, f3, f4, f5, f6, f7, f8]


	def find_path(self, c, t, board):
		if c == t:
			return 1

		cx, cy = c

		# don't follow a path is the cell is known
		if board[cx][cy] == 1:
			return 0

		fn = self.get_functions()

		# mark current cell as known
		board[cx][cy] = 1

		# compute all possible positions
		for f in fn:
			new_pos = f(cx, cy)
			if self.is_position_in(new_pos):
				print(new_pos)
				self.find_path(new_pos, t, board)
			else:
				return 0


	def is_reachable(self, curr, target):
		board = [[0 for j in range(0,self.size)] for i in range(0,self.size)]
		result = self.find_path(curr, target, board)
		print(result)

def main():
	knight = ChessKnight()
	print(knight.get_size())
	print(knight.get_board())

	knight.is_reachable((5,5), (3,6))



if __name__ == "__main__":
	main()

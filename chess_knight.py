class Queue:
	def __init__(self):
		self.size = 0
		self.queue = []

	def enqueue(self, elem):
		self.size += 1
		self.queue += [elem]

	def dequeue(self):
		first = self.queue[0]
		self.queue = self.queue[1:]
		self.size -= 1

		return first

	def isEmpty(self):
		return self.size == 0

class ChessKnight:

	def __init__(self, n, m):
		self.size = (n, m)
		self.board = [[0 for j in range(0,m)] for i in range(0,n)]

	def get_board(self):
		return self.board

	def get_size(self):
		return self.size

	def is_position_in(self, pos):
		x, y = pos
		if x < 0 or x >= self.size[0]:
			return False
		if y < 0 or y >= self.size[1]:
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


	def find_path(self, t, board, visited):

		# compute all possible positions
		fn = self.get_functions()

		while not visited.isEmpty():
			(cx, cy), dist = visited.dequeue()
			# visited = visited[1:]
			if (cx, cy) == t:
				return dist
			for f in fn:
				nx, ny = new_pos = f(cx, cy)
				if self.is_position_in(new_pos) and board[nx][ny] == 0:
					visited.enqueue((new_pos, dist + 1)) # += [(new_pos, dist + 1)]
					board[nx][ny] = 1

		return -1


	def is_reachable(self, curr, target):
		board = self.get_board()
		visited = Queue()
		visited.enqueue((curr,0))
		board[curr[0]][curr[1]] = 1
		result = self.find_path(target, board, visited)
		print(result)

def main():
	knight1 = ChessKnight(4, 7)
	# 2, 6 ; 2, 4 -> 2
	knight1.is_reachable((1,5), (1,3))

	# 0
	knight2 = ChessKnight(1, 1)
	knight2.is_reachable((0,0), (0,0))

	# 6
	knight3 = ChessKnight(8, 8)
	knight3.is_reachable((0,0),(7,7))



if __name__ == "__main__":
	main()

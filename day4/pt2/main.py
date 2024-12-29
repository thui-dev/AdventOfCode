import math

def main():

	file = open("../input.txt").read().split('\n')

	def check_for_word(word, index, direction):
		for char in word:
			if index[0] < 0 or index[1] < 0:
				return 0
			try:
				if char != file[index[0]][index[1]]:
					return 0
			except:
				return 0
			index[0] += direction[0]
			index[1] += direction[1]
		return 1

	def search(start_index):

		word = "MAS"
		middle_letter = word[len(word)//2]

		if middle_letter != file[start_index[0]][start_index[1]]:
			return 0

		diagonal_kernels = [
			[
				[-1,-1],
						[+1,+1]
			],
			[
						[-1,+1],
				[+1,-1]
			]
		]

		#backtracking from middle
		tests = 0
		for diagonals in range(2):
			for direction in range(2):
				current_index = list(start_index)
				for i in range(len(word)//2):
					current_index[0] += diagonal_kernels[diagonals][direction][0]
					current_index[1] += diagonal_kernels[diagonals][direction][1]
				tests += check_for_word(word, current_index, diagonal_kernels[diagonals][direction-1])

		return 1 if tests == 2 else 0
	
	total = 0

	for i, line in enumerate(file):
		for j, char in enumerate(line):
			total += search((i, j))
	
	print(total)
	return

main()
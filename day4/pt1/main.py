def main():

	file = open("../input.txt").read().split('\n')

	def search(word, start_index):

		#8 directions (kernel?)
		kernel = [
			[-1,-1], [-1, 0], [-1,+1],
			[ 0,-1],          [ 0,+1],
			[+1,-1], [+1, 0], [+1,+1]
		]

		final = 0

		for item in kernel:
			if word[0] != file[start_index[0]][start_index[1]]:
				break
			
			current_index = list(start_index)
			
			for char in word:
				if current_index[0] < 0 or current_index[1] < 0:
					break
				try:
					if char != file[current_index[0]][current_index[1]]:
						break
				except:
					break
				current_index[0] += item[0]
				current_index[1] += item[1]

			else:
				final += 1
				#print("position:", start_index)

		return final
	
	total = 0

	for i, line in enumerate(file):
		for j, char in enumerate(line):
			total += search('XMAS', (i, j))
	
	print(total)
	return

main()
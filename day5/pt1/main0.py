def main0():
	f = open("../input.txt").read().split('\n\n')
	rules = f[0].split('\n')
	rules = [list(int(i) for i in line.split('|')) for line in rules]
	updates = f[1].split('\n')
	updates = [[int(i) for i in line.split(',')] for line in updates]

	def check(line):
		for i, item in enumerate(line):
			if set(line[:i]) & set((i[1] for i in rules if i[0] == item)) != set():
				return False
			if set(line[i+1:]) & set((i[0] for i in rules if i[1] == item))!= set():			
				return False
		return True

	print(sum([line[len(line)//2] for line in filter(check, updates)]))

main0()
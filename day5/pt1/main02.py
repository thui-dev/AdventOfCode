def main02():
	f = open("../input.txt").read().split('\n\n')
	rules = f[0].split('\n')
	rules = [list(int(i) for i in line.split('|')) for line in rules]
	updates = f[1].split('\n')
	updates = [[int(i) for i in line.split(',')] for line in updates]
	
	map_rules = [{}, {}]
	map_seen =  [set(), set()]
	for n in range(2):
		for rule in rules:
			if rule[n] not in map_seen[n-1]:
				map_seen[n].add(rule[n])
				map_rules[n][rule[n]] = set(_[n-1] for _ in rules if _[n] == rule[n])

	def check(line):
		for i, item in enumerate(line):
			try:
				#check for contradiction: if theres an item that's BEFORE (line[:item]), and should be AFTER (after_rules[item])
				if set(line[:i]) & map_rules[0][item] != set():
					return False
			except: pass
			try:
				#the same thing, just swapped: item that AFTER and should be BEFORE
				if set(line[i+1:]) & map_rules[1][item] != set():			
					return False
			except: pass
		return True

	print(sum([line[len(line)//2] for line in filter(check, updates)]))

main02()
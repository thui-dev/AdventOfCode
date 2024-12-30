def main():
	#parsing out input
	f = open("../input.txt").read().split('\n\n')
	rules = f[0].split('\n')
	rules = [list(int(i) for i in line.split('|')) for line in rules]
	updates = f[1].split('\n')
	updates = [[int(i) for i in line.split(',')] for line in updates]

	#setting up input as useful data_struct (dict)
	bf_af_rules = [{}, {}] #[0] are after rules, [1] are before rules.
	bf_af_seen =  [set(), set()]
	for n in range(2):
		for rule in rules:
			if rule[n] not in bf_af_seen[n]:
				bf_af_seen[n].add(rule[n])
				bf_af_rules[n][rule[n]] = set(_[n-1] for _ in rules if _[n] == rule[n])

	def check(line):
		for i, item in enumerate(line):
			if set(line[:i]) & bf_af_rules[0].get(item, set()) != set():
					return False
			if set(line[i+1:]) & bf_af_rules[1].get(item, set()) != set():			
					return False
		return True
	
	def ajeitar(line):
		for index, item in enumerate(line.copy()):
			befores = bf_af_rules[1].get(item, set())
			try:
				new_index = max([line.index(_) for _ in befores if _ in line])
			except: continue
			if new_index > index:
				new_item = line[new_index]
				line[new_index] = item
				line[index] = new_item
				return ajeitar(line)
		return line
	
	errados = [line for line in updates if check(line) is False]
	print(sum([line[len(line)//2] for line in list(map(ajeitar, errados))]))

main()
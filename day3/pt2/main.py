
import re

def mul(a, b):
	return a*b

instructions = re.findall("mul\([0-9]*,[0-9]*\)|do\(\)|don't\(\)", open("../input.txt").read())

print(*l, sep='\n')

switch = True

for item in instructions:
	pass

#print(sum(list(map(eval, l))))
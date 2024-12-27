
import re

def mul(a, b):
	return a*b

instructions = re.findall("mul\([0-9]*,[0-9]*\)", open("../input.txt").read())

#print(*instructions, sep='\n')

print(sum(list(map(eval, instructions))))
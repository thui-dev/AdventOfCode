
import re

def mul(a, b):
	return a*b

instructions = re.findall("mul\(\d+,\d+\)", open("../input.txt").read())

#print(*instructions, sep='\n')

print(sum(list(map(eval, instructions))))
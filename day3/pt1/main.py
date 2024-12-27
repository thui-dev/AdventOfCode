
import re

def mul(a, b):
	return a*b

l = re.findall("mul\([0-9]*,[0-9]*\)", open("./input.txt").read())
print(sum(list(map(eval, l))))
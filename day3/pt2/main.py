
import re

switch = True

def mul(a, b):
	if switch == True:
		return a*b
	else:
		return None

def do():
	global switch
	switch = True
	return

def dont():
	global switch
	switch = False
	return

def clear_donts(a):
	if a == "don't()":
		return "dont()"
	return a

instructions = re.findall("mul\([0-9]*,[0-9]*\)|do\(\)|don't\(\)", open("../input.txt").read())

instructions = list(map(clear_donts, instructions)) #cant define function "don't()", so changing all occurances of it to "dont()"

#print(*instructions, sep='\n')
#print(*list(map(eval, instructions)), sep="\n")

instructions = list(map(eval, instructions))

print(f"total sum: {sum([_ for _ in instructions if _ is not None])}")
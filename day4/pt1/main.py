
with open("../demo.txt") as f:
	f = f.read().split('\n')

print(f[0][0])


"""
diagonal
n   0

n-1 0
n   1

n-2 0
n-1 1
n   2
"""
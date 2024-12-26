
f = open("./input.txt")

lists = [list(), list()]

for line in f:
    line = line.split('   ')
    
    lists[0].append(int(line[0]))
    lists[1].append(int(line[1]))

for l in lists:
    l.sort()

final = 0
for a, b in zip(lists[0], lists[1]):
    final += abs(a - b)

print(final)
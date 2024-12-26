
f = open("./input.txt")

lists = [list(), list()]

for line in f:
    line = line.split('   ')
    
    lists[0].append(int(line[0]))
    lists[1].append(int(line[1]))

final = []
for item in lists[0]:
    final.append(lists[1].count(item)*item)

print(sum(final))
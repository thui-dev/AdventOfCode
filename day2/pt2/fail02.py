
f = open("./input.txt")

final, report = list(), list()
for line in f:
    report.append(list(map(int, line.split())))
    final.append(1)
    
for index, level in enumerate(report):
    
    level_bckp = level.copy()
    dampener = None

    monotone = 1 if level[0] - level[1] > 0 else -1 # '1' means it's decresing, because.
    
    for n in range(len(level)-1):
        diff = level[n] - level[n+1]
        if 1 <= abs(diff) <= 3 and diff/abs(diff) == monotone:
            continue

        dampener = n
        level.pop(dampener)
        break
    else:
        continue

    monotone = 1 if level[0] - level[1] > 0 else -1
    for n in range(len(level)-1):
        diff = level[n] - level[n+1] 
        if 1 <= abs(diff) <= 3 and diff/abs(diff) == monotone:
            continue
        break
    else:
        continue
        
    level = level_bckp
    level.pop(dampener+1)
    monotone = 1 if level[0] - level[1] > 0 else -1
    for n in range(len(level)-1):
        diff = level[n] - level[n+1] 
        if 1 <= abs(diff) <= 3 and diff/abs(diff) == monotone:
            continue
        
        final[index] = 0
        break
        
    #print(final[index])

print(f"total sum: {sum(final)}")
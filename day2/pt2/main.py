
f = open("./input.txt")

final, report = [], []
for line in f:
    report.append(list(map(int, line.split())))
    final.append(0)

def monotone(a, b):
    diff = a-b
    if diff > 0:
        return 1
    elif diff < 0:
        return -1
    return 0

def evaluate_level(level):
    for n in range(len(level)-1):
        diff = level[n] - level[n+1]
        if 1 <= abs(diff) <= 3 and diff/abs(diff) == monotone(level[0], level[1]):
            continue
        return False
    return True
    
    
for index, level in enumerate(report):
    
    if evaluate_level(level):
        final[index] = 1
    else:
        for i in range(len(level)):
            level_copy = level.copy()
            level_copy.pop(i)
            if evaluate_level(level_copy):
                final[index] = 1
                break
        
    print(final[index])

print(f"total sum: {sum(final)}")
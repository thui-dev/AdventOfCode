
from main01 import main01
from main02 import main02

import timeit
import cProfile

after_rules = {}
	before_rules = {}
	after_seen = set()
	before_seen = set()
	for i in rules:
		if i[0] not in after_seen:
			after_seen.add(i[0])
			after_rules[i[0]] = set(j[1] for j in rules if j[0] == i[0])
		if i[1] not in before_rules:
			before_seen.add(i[1])
			before_rules[i[1]] = set(j[0] for j in rules if j[1] == i[1])

bf_af_rules = [{}, {}]
bf_af_seen =  [set(), set()]
for n in range(2):
	for rule in rules:
		if rule[n] not in bf_af_seen[n-1]:
			bf_af_seen[n].add(rule[n])
			bf_af_rules[n][rule[n]] = set(_[n-1] for _ in rules if _[n] == rule[n])

RUNS = 100
print(F"TESTING SCRIPT 1 for {RUNS} times...")
script1 = timeit.timeit("main01()", globals=globals(), number=RUNS)
print(f"TESTING SCRIPT 2... for {RUNS} times:")
script2 = timeit.timeit("main02()", globals=globals(), number=RUNS)

print(f"Average execution time of SCRIPT 1 with {RUNS} runs: {script1 / 100}")
print(f"Average execution time of SCRIPT 2 with {RUNS} runs: {script2 / 100}")

"""
cProfile.run("main01()")
print()
print()
cProfile.run("main02()")
"""
import re

f = open("input.txt", "rt")
pattern = r'mul\((\d+),(\d+)\)'

mul = re.findall(pattern, f.read())

results = []
for m in mul:
    num1 = int(m[0])
    num2 = int(m[1])
    results.append(num1 * num2)


print(sum(results))

from typing import Counter

from rapidfuzz.distance.Prefix import similarity

f = open("input.txt", 'rt')
numbers = f.read()
lines = numbers.strip().split('\n')

column1 = []
column2 = []

for line in lines:
    num1, num2 = map(int, line.split())
    column1.append(num1)
    column2.append(num2)

similarity_score = []
for i in column1:
    if i in column2:
        match_count = column2.count(i)
        similarity_score.append(i * match_count)

print(sum(similarity_score))
f = open("input.txt", 'rt')
numbers = f.read()
lines = numbers.strip().split('\n')

column1 = []
column2 = []

for line in lines:
    num1, num2 = map(int, line.split())
    column1.append(num1)
    column2.append(num2)

column1.sort()
column2.sort()

diff = []
for i in column1:
    index = column1.index(i)
    if column2[index] > i:
        diff.append(column2[index] - i)


    else:
        diff.append(i - column2[index])

print(sum(diff))
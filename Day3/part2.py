import re

with open("input.txt", "r") as file:
    corrupted_memory = file.read()

    mul_pattern = r'mul\(\d+,\d+\)'
    do_pattern = r"don't\(\).*?(?=do\(\)|$)"
    pattern = r'\d+'

    corrupted_memory = re.sub(do_pattern, "", corrupted_memory, flags=re.DOTALL)
    findings = re.findall(mul_pattern, corrupted_memory)

    mul = [re.findall(pattern, finding) for finding in findings]

    results = []
    for m in mul:
        num1 = int(m[0])
        num2 = int(m[1])
        results.append(num1 * num2)

    print(sum(results))
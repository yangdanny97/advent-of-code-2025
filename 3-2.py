instructions = """
987654321111111
811111111111119
234234234234278
818181911112111
"""

banks = instructions.split()
total = 0
for bank in banks:
    max_jolts = 0
    max_prev = [0] * 11
    for digit in bank:
        n = int(digit)
        if max_prev[-1]:
            max_jolts = max(max_jolts, max_prev[-1] * 10 + n)
        for i in reversed(range(len(max_prev))):
            if i == 0:
                max_prev[i] = max(max_prev[i], n)
            else:
                max_prev[i] = max(max_prev[i], max_prev[i - 1] * 10 + n)
    total += max_jolts
print(total)

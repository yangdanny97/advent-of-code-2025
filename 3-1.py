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
    max_first_digit = 0
    for digit in bank:
        n = int(digit)
        if max_first_digit:
            max_jolts = max(max_jolts, max_first_digit * 10 + n)
        if n > max_first_digit:
            max_first_digit = n
    total += max_jolts

print(total)

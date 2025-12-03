instructions = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124"""

ranges = [tuple(x.split("-")) for x in instructions.split(",")]
score = 0
for start, end in ranges:
    start_prefix_len = len(start) // 2
    end_prefix_len = len(end) // 2
    start_n = int(start)
    end_n = int(end)
    range_start = max(10 ** (start_prefix_len - 1), 1)
    range_end = max(10 ** (end_prefix_len + 1), 1)
    for i in range(range_start, range_end):
        doubled = int(str(i) + str(i))
        if doubled >= start_n and doubled <= end_n:
            score += doubled
print(score)

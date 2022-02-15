map = [['A', 'B', 'G', 'K'], ['T', 'T', 'A', 'B'], ['A', 'C', 'C', 'D']]
pattern = []

for _ in range(2):
    pattern_row = list(map(str, input()))
    pattern.append(pattern_row)

print(pattern)
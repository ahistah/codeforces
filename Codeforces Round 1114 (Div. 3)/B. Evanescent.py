t = int(input())
#using the optimization strategy for longest continuous running blocks fo chars
for _ in range(t):
    n = int(input())
    s = str(input())
    runs = []
    curr_char = s[0]
    curr_length = 1

    for i in range(1, n):
        if s[i] == curr_char:
            curr_length += 1
        else:
            runs.append([curr_char, curr_length])
            curr_char = s[i]
            curr_length = 1

    runs.append([curr_char, curr_length])
    compressed_length = len(runs)
    best_reduction = 0

    for i in range(1, len(runs) - 1):
        if runs[i][1] == 1:
            if runs[i - 1][0] == runs[i + 1][0]:
                best_reduction = 2
                break
            else:
                best_reduction = max(best_reduction, 1)

    print(compressed_length - best_reduction)
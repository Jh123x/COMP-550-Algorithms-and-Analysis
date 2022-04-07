def trace_table(backtrack_table, seq1, seq2):
    """Trace back the backtrack table to find the longest common subsequence"""
    i, j = len(seq1)-1, len(seq2)-1
    lcs = []

    while i >= 0 and j >= 0:
        dx, dy = backtrack_table[i][j]
        if dx + dy == -2:
            lcs.append(seq1[i])
            # break
        i += dx
        j += dy
    return lcs[::-1]


def longest_common_subsequence(seq1, seq2):
    """Find the longest common subsequence between 2 strings"""
    count_table = [[0] * (len(seq2)+1) for _ in range(len(seq1)+1)]
    backtrack_table = [[(0, 0)] * (len(seq2)) for _ in range(len(seq1))]
    for i in range(1, len(seq1) + 1):
        for j in range(1, len(seq2) + 1):
            if (seq1[i-1] == seq2[j-1]):
                count_table[i][j] = count_table[i-1][j-1] + 1
                backtrack_table[i-1][j-1] = (-1, -1)
            elif count_table[i-1][j] >= count_table[i][j-1]:
                count_table[i][j] = count_table[i-1][j]
                backtrack_table[i-1][j-1] = (-1, 0)
            else:
                count_table[i][j] = count_table[i][j-1]
                backtrack_table[i-1][j-1] = (0, -1)

    return count_table[-1][-1], trace_table(backtrack_table, seq1, seq2)


if __name__ == '__main__':
    X = ["A", "T", "C", "A", "C", "C", "T", "A", "T", "C", "A", "C", "C", "T"]
    Y = ["A", "T", "A", "A", "C", "T", "A", "T", "A", "A", "C", "T"]
    print(longest_common_subsequence(X, Y))

def edit_distance(word1: str, word2: str) -> int:
    """Check the edit distance between 2 words"""
    memo = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]

    for i in range(len(word1) + 1):
        memo[i][0] = i
    for j in range(len(word2) + 1):
        memo[0][j] = j

    for i in range(1, len(word1) + 1):
        for j in range(1, len(word2) + 1):
            l1 = word1[i - 1]
            l2 = word2[j - 1]

            if l1 == l2:
                memo[i][j] = memo[i-1][j-1]
                continue

            memo[i][j] = min(memo[i-1][j-1] if i > 0 and j > 0 else 0,
                             memo[i-1][j] if i > 0 else 0, memo[i][j-1] if j > 0 else 0) + 1

    return memo[-1][-1]


if __name__ == '__main__':
    word1 = "part"
    word2 = "spartan"
    r = edit_distance(word1, word2)
    print(r)

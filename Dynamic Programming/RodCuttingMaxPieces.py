from typing import List


def rod_cutting_max_pieces(pieces: List[int], length: int) -> int:
    """Optimal way to cut rods into the maximum pieces"""
    dp = [0] * (length + 1)
    for i in range(1, length + 1):
        # Check if i is in pieces size
        for j in range(len(pieces)):
            piece_size = pieces[j]
            if i == piece_size:
                dp[i] = max(dp[i], 1)
                continue
            if i > piece_size:
                dp[i] = max(dp[i], dp[i-piece_size] + dp[piece_size])

    return dp[length], dp

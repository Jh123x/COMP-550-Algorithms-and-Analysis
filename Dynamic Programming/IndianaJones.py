from typing import List


"""
Indiana Jones must climb a wall of height feet by putting ladders together
of different lengths that sum to the total of feet exactly. Indy has an
unlimited number of ladders of length 1, 5, or 10 feet. He can use any
combination of these ladders to traverse feet exactly.
If , then Indy has three possible ladder permutations: six one-foot
ladders, a five-foot ladder followed by a one-foot ladder, or a one-foot
ladder followed by a five-foot ladder.
"""


def indiana_jones(height: int, ladder_size: List[int]):
    """Indiana Jones"""
    dp = [0] * (height + 1)
    dp[0] = 0

    for i in range(1, height+1):
        dp[i] = 0
        for j in ladder_size:
            if i == j:
                dp[i] += 1

            if i > j:
                dp[i] += dp[i-j]

    return dp[-1]

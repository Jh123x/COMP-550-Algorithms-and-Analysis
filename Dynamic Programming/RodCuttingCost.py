from typing import List


def rod_cutting_cost(prices: List[int], length: int, cost: int) -> int:
    """Optimal way to cut rods"""
    dp = [0] * (length + 1)
    for i in range(1, length + 1):
        dp[i] = prices[i - 1]
        for j in range(1, i + 1):
            dp[i] = max(dp[i], prices[j - 1] + dp[i - j] - cost)
    return dp[length], dp

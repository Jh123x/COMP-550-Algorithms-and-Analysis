from typing import List


def rod_cutting(prices: List[int], length: int) -> int:
    """Optimal way to cut rods"""
    dp = [0] * (length + 1)
    for i in range(1, length + 1):
        for j in range(1, i + 1):
            dp[i] = max(dp[i], prices[j - 1] + dp[i - j])
    return dp[length], dp


if __name__ == '__main__':
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    length = 5
    for i in range(length + 1):
        print(rod_cutting(prices, i))

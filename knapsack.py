#!/usr/bin/env python3
"""knapsack - 0/1 knapsack, unbounded knapsack, and fractional knapsack."""
import sys

def knapsack_01(weights, values, capacity):
    n = len(weights)
    dp = [[0]*(capacity+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for w in range(capacity+1):
            dp[i][w] = dp[i-1][w]
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i][w], dp[i-1][w-weights[i-1]] + values[i-1])
    # Backtrack
    items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            items.append(i-1)
            w -= weights[i-1]
    return dp[n][capacity], items[::-1]

def knapsack_unbounded(weights, values, capacity):
    dp = [0] * (capacity + 1)
    for w in range(1, capacity + 1):
        for i in range(len(weights)):
            if weights[i] <= w:
                dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    return dp[capacity]

def knapsack_fractional(weights, values, capacity):
    items = sorted(range(len(weights)), key=lambda i: values[i]/weights[i], reverse=True)
    total = 0
    remaining = capacity
    fractions = [0.0] * len(weights)
    for i in items:
        if remaining <= 0: break
        take = min(weights[i], remaining)
        fractions[i] = take / weights[i]
        total += values[i] * fractions[i]
        remaining -= take
    return total, fractions

def test():
    val, items = knapsack_01([2, 3, 4, 5], [3, 4, 5, 6], 5)
    assert val == 7  # items 0,1 (w=5, v=7)
    val2 = knapsack_unbounded([2, 3, 4], [3, 4, 5], 7)
    assert val2 >= 10  # multiple copies allowed
    val3, frac = knapsack_fractional([10, 20, 30], [60, 100, 120], 50)
    assert abs(val3 - 240.0) < 1e-6  # take all of first two + 2/3 of third
    print("knapsack: all tests passed")

if __name__ == "__main__":
    test() if "--test" in sys.argv else print("Usage: knapsack.py --test")

#!/usr/bin/env python3
"""knapsack - 0/1 and fractional knapsack solvers."""
import sys

def knapsack_01(weights, values, capacity):
    n = len(weights)
    dp = [[0]*(capacity+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for w in range(capacity+1):
            dp[i][w] = dp[i-1][w]
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i][w], dp[i-1][w-weights[i-1]] + values[i-1])
    items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            items.append(i-1)
            w -= weights[i-1]
    return dp[n][capacity], list(reversed(items))

def fractional_knapsack(weights, values, capacity):
    n = len(weights)
    ratios = [(values[i]/weights[i], weights[i], values[i], i) for i in range(n)]
    ratios.sort(reverse=True)
    total = 0
    remaining = capacity
    items = []
    for ratio, w, v, i in ratios:
        if remaining <= 0:
            break
        take = min(w, remaining)
        fraction = take / w
        total += v * fraction
        remaining -= take
        items.append((i, fraction))
    return total, items

def unbounded_knapsack(weights, values, capacity):
    dp = [0] * (capacity + 1)
    for w in range(1, capacity + 1):
        for i in range(len(weights)):
            if weights[i] <= w:
                dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    return dp[capacity]

def test():
    val, items = knapsack_01([2,3,4,5], [3,4,5,6], 8)
    assert val == 10
    assert sum(2 if i==0 else 3 if i==1 else 4 if i==2 else 5 for i in items) <= 8
    fval, fitems = fractional_knapsack([10,20,30], [60,100,120], 50)
    assert abs(fval - 240) < 0.01
    uval = unbounded_knapsack([2,3], [3,4], 7)
    assert uval >= 10
    val0, items0 = knapsack_01([], [], 10)
    assert val0 == 0
    val1, items1 = knapsack_01([5], [10], 3)
    assert val1 == 0
    print("All tests passed!")

if __name__ == "__main__":
    test() if "--test" in sys.argv else print("knapsack: Knapsack solvers. Use --test")

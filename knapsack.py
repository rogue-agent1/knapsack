#!/usr/bin/env python3
"""Knapsack problem solver. Zero dependencies."""

def knapsack_01(weights, values, capacity):
    n = len(weights)
    dp = [[0]*(capacity+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for w in range(capacity+1):
            dp[i][w] = dp[i-1][w]
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i][w], dp[i-1][w-weights[i-1]] + values[i-1])
    # Reconstruct
    items = []; w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            items.append(i-1); w -= weights[i-1]
    return dp[n][capacity], list(reversed(items))

def knapsack_unbounded(weights, values, capacity):
    dp = [0] * (capacity + 1)
    choice = [-1] * (capacity + 1)
    for w in range(1, capacity + 1):
        for i in range(len(weights)):
            if weights[i] <= w and dp[w - weights[i]] + values[i] > dp[w]:
                dp[w] = dp[w - weights[i]] + values[i]
                choice[w] = i
    items = []; w = capacity
    while w > 0 and choice[w] >= 0:
        items.append(choice[w]); w -= weights[choice[w]]
    return dp[capacity], items

def fractional_knapsack(weights, values, capacity):
    items = sorted(range(len(weights)), key=lambda i: values[i]/weights[i], reverse=True)
    total = 0; taken = []
    for i in items:
        if capacity <= 0: break
        take = min(weights[i], capacity)
        total += take * values[i] / weights[i]
        taken.append((i, take / weights[i]))
        capacity -= take
    return total, taken

if __name__ == "__main__":
    w = [2,3,4,5]; v = [3,4,5,6]
    val, items = knapsack_01(w, v, 8)
    print(f"Value: {val}, Items: {items}")

from knapsack import knapsack_01, knapsack_unbounded, fractional_knapsack
val, items = knapsack_01([2,3,4,5], [3,4,5,6], 8)
assert val == 10  # items 0,2 (w=6,v=8) or 1,2 (w=7,v=9) or 0,1,2... let me check
# w=[2,3,4,5] v=[3,4,5,6] cap=8: best is items 1,2 (w=7,v=9) or 0,3 (w=7,v=9) or 0,1,2 (w=9 too big)
# Actually: 0+1+? = w=5,v=7; +nothing better. 0+2=w=6,v=8; 0+3=w=7,v=9; 1+2=w=7,v=9; 1+3=w=8,v=10
assert val == 10
uval, _ = knapsack_unbounded([2,3], [3,4], 7)
assert uval == 10  # 2+2+3=7, v=3+3+4=10
fval, _ = fractional_knapsack([10,20,30], [60,100,120], 50)
assert abs(fval - 240) < 0.01
print("knapsack tests passed")

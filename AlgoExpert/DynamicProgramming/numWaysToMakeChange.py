# Time O(dn) | Space O(n)
def numberOfWaysToMakeChange(n, denoms):
    ways = [0]*(n+1)
	ways[0] = 1
	for denom in denoms:
		for amount in range(1, n + 1):
			if denom <= amount:
				ways[amount] += ways[amount-denom]
	return ways[-1]
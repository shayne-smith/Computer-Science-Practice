# Time O(n^2) | Space O(1)
def twoNumberSum(array, targetSum):
	# i and j counter, starting at 0
	# loop through array twice, comparing not moving i to moving j
	for i in range(len(array)):
		for j in range(len(array)):
			print(i, j)
			# continue when i=j
			if i == j:
				continue
			# add numbers and compare to target sum
			if array[i] + array[j] == targetSum:
				return [array[i], array[j]]
	return []
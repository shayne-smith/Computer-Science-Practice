# Time O(n) | Space O(1)
def maxSubsetSumNoAdjacent(array):
	if len(array) == 0:
		return 0
	if len(array) == 1:
		return array[0]
	
	sums = []
	for i in range(len(array)):
		if len(sums) == 0:
			sums.append(array[0])
		elif len(sums) == 1:
			if array[1] > sums[0]:
				sums.append(array[1])
			else:
				sums.append(sums[0])
		elif sums[i-2] + array[i] > sums[i-1]:
			sums.append(sums[i-2] + array[i])
		else:
			sums.append(sums[i-1])
	return max(sums)
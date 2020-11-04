# Time O(n) | Space O(n)
def hasSingleCycle(array):
    # start at index 0
	current = 0
	
	# add current index to set
	idxSet = set()
	
	# check if length of set equals length of array
	while len(idxSet) < len(array): # 0, 2, 3, -1, 1, 4, 0
		if current in idxSet:
			return False
		else:
			idxSet.add(current)
			current = getNextIdx(current, array)
	
	return current == 0

# get next index	
def getNextIdx(current, array):
	jump = array[current]
	nextIdx = (current + jump) % len(array)
	return nextIdx if nextIdx >= 0 else nextIdx + len(array)
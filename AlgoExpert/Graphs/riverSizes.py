# Time O(wh) | Space O(wh)
def riverSizes(matrix):
	visited = set()
	sizes = []
	
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if (i, j) in visited:
				continue	   
			traverseNode(i, j, matrix, visited, sizes)
	return sizes
					   
def traverseNode(i, j, matrix, visited, sizes):
	currentRiverSize = 0
	nodesToExplore = [(i, j)]
	while len(nodesToExplore) > 0:
		currentNode = nodesToExplore.pop(0)
		i = currentNode[0]
		j = currentNode[1]
		if currentNode in visited:
			continue
		visited.add(currentNode)
		if matrix[i][j] == 0:
			continue
		currentRiverSize += 1
		unvisitedNeighbors = getUnvisitedNeighbors(i, j, matrix, visited)
		for neighbor in unvisitedNeighbors:
			nodesToExplore.append(neighbor)
	if currentRiverSize > 0:
		sizes.append(currentRiverSize)

def getUnvisitedNeighbors(i, j, matrix, visited):
	unvisitedNeighbors = []
	if i > 0 and (i - 1, j) not in visited:
		unvisitedNeighbors.append((i - 1, j))
	if i < len(matrix) - 1 and (i + 1, j) not in visited:
		unvisitedNeighbors.append((i + 1, j))
	if j > 0 and (i, j - 1) not in visited:
		unvisitedNeighbors.append((i, j - 1))
	if j < len(matrix[0]) - 1 and (i, j + 1) not in visited:
		unvisitedNeighbors.append((i, j + 1))
	return unvisitedNeighbors
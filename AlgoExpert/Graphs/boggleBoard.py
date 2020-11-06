# First Try
def boggleBoard(board, words):
	visited = set()
	words.sort(key=lengthFunc, reverse=True)
	print(words)
	
	for i in range(len(board)):
		for j in range(len(board[0])):
			if (i, j) in visited:
				continue
			visited.add((i, j))
			for word in words:
				if board[i][j] == word[0]:
					traverseWord(board, words, (i, j), visited)
					
def lengthFunc(s):
	return len(s)

def traverseWord(board, words, currentIdx, visited):
	i = currentIdx[0]
	j = currentIdx[1]
	word = board[i][j]
	filteredWords = [k for k in words if word in k]
	tempVisited = []
	foundWord = False
	
	# print("filtered: " + str(filteredWords))
	while not foundWord and len(filteredWords) != 0:
		# print("filtered: " + str(filteredWords))
		neighbors = getUnvisitedNeighbors(board, i, j, visited)
		foundPossibleWord = False
		
		for neighbor in neighbors: # ["s", "i", "h"]
			temp = word + neighbor[0]
			# print("temp " + temp)
			for k in filteredWords:
				if temp in k:
					foundPossibleWord = True
					word = temp # update word which holds the string being built
					print("word inside neighbors " + word)
					i = neighbor[1] # update i
					j = neighbor[2] # update j
					tempVisited.append((i, j))
					print("tempVisited " + str(tempVisited))
					break # stop checking neighbors after first match
			if foundPossibleWord:
				break

		print("word inside while " + word)
		filteredWords = [k for k in words if word in k] # update filteredWords

		for filtered in filteredWords:
			for word in words:
				if filtered == word:
					foundWord = True

					for visit in tempVisited: # update where pointer has visited
						visited.add(visit)
	
	# print("word " + word)
	return word
		
def checkWord(str, words):
	for word in words:
		if str == word:
			return True
	return False
				
def getUnvisitedNeighbors(board, i, j, visited):
	neighbors = [] # [(character, i, j)]
	# 8 maximum possible neighbors
	if 0 < i and 0 < j: # upper-left
		if (i-1, j-1) not in visited:
			neighbors.append((board[i-1][j-1], i-1, j-1))

	if 0 < i: # upper-middle
		if (i-1, j) not in visited:
			neighbors.append((board[i-1][j], i-1, j))

	if 0 < i and j < len(board[0]) - 1:	# upper-right
		if (i-1, j+1) not in visited:
			neighbors.append((board[i-1][j+1], i-1, j+1))

	if 0 < j: # middle-left
		if (i, j-1) not in visited:
			neighbors.append((board[i][j-1], i, j-1))

	if j < len(board[0]) - 1: # middle-right
		if (i, j+1) not in visited:
			neighbors.append((board[i][j+1], i, j+1))

	if i < len(board) - 1 and 0 < j: # lower-left
		if (i+1, j-1) not in visited:
			neighbors.append((board[i+1][j-1], i+1, j-1))

	if i < len(board) - 1: # lower-middle
		if (i+1, j) not in visited:
			neighbors.append((board[i+1][j], i+1, j))

	if i < len(board) - 1 and j < len(board[0]) - 1: # lower-right
		if (i+1, j+1) not in visited:
			neighbors.append((board[i+1][j+1], i+1, j+1))
		
	return neighbors
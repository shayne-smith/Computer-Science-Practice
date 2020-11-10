def boggleBoard(board, words):
	foundWords = []
	
	for i in range(len(board)):
		for j in range(len(board[0])):
			for word in words:
				if board[i][j] == word[0]:
					visited = set()
					newWord = traverseWord2(board, words, i, j, board[i][j], visited, foundWords)
					if newWord is not False and newWord in words and newWord not in foundWords:
						print("newWord " + str(newWord))
						foundWords.append(newWord)
	
	print("foundWords" + str(foundWords))
	return foundWords
					
def stringLengthFunc(s):
	return len(s)

def traverseWord(board, words, i, j): # [(character, i, j)]
	word = board[i][j]
	filteredWords = [k for k in words if word in k]
	foundWord = False
	
	# print("filtered: " + str(filteredWords))
	while not foundWord and len(filteredWords) != 0:
		# print("filtered: " + str(filteredWords))
		neighbors = getNeighbors(board, i, j)
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
	
def numWordsContainingString(testStr, words):
	count = 0
	for word in words:
		if testStr in word:
			count += 1
	return count
	
def traverseWord2(board, words, i, j, testStr, visited, foundWords):
	# print("pre-testStr " + testStr)
	if testStr in words and numWordsContainingString(testStr, words) is 1:
		print("success2! -- " + testStr)
		return testStr
	visited.add((i, j))
	neighbors = getNeighbors(board, i, j, visited)
	# print(str(neighbors))
	for neighbor in neighbors:
		if testStr not in words:
			testStr = testStr + neighbor[0]
		# if testStr in words and numWordsContainingString(testStr, words) is not 1:
		# 	testStr = testStr + neighbor[0]
		print("post-testStr " + testStr)
		if testStr in words and testStr not in foundWords:
			print("success! -- " + testStr)
			return testStr
		elif testStr in foundWords:
			print("already found! -- " + testStr)
			numPossibleWords = numWordsContainingString(testStr, words)
			print("number of possible words: " + str(numPossibleWords))
			if numPossibleWords == 1:
				return False
			else:
				testStr = testStr + neighbor[0]
				print(testStr)
				for word in words:
					if testStr in word[:len(testStr)]:
						print(testStr)
						return traverseWord2(board, words, neighbor[1], neighbor[2], testStr, visited, foundWords)
				testStr = testStr[:-1]
				print("post: " + testStr)
		else:
			for word in words:
				if testStr in word[:len(testStr)]:
					# print(testStr)
					return traverseWord2(board, words, neighbor[1], neighbor[2], testStr, visited, foundWords)
			testStr = testStr[:-1]
	
def checkWord(str, words):
	for word in words:
		if str == word:
			return True
	return False
				
def getNeighbors(board, i, j, visited):
	neighbors = [] # of the form: [(character, i, j)]
	# 8 maximum possible neighbors
	if 0 < i and 0 < j and (i-1, j-1) not in visited: # upper-left
		neighbors.append((board[i-1][j-1], i-1, j-1))

	if 0 < i and (i-1, j) not in visited: # upper-middle
		neighbors.append((board[i-1][j], i-1, j))

	if 0 < i and j < len(board[0]) - 1 and (i-1, j+1) not in visited:	# upper-right
		neighbors.append((board[i-1][j+1], i-1, j+1))

	if 0 < j and (i, j-1) not in visited: # middle-left
		neighbors.append((board[i][j-1], i, j-1))

	if j < len(board[0]) - 1 and (i, j+1) not in visited: # middle-right
		neighbors.append((board[i][j+1], i, j+1))

	if i < len(board) - 1 and 0 < j and (i+1, j-1) not in visited: # lower-left
		neighbors.append((board[i+1][j-1], i+1, j-1))

	if i < len(board) - 1 and (i+1, j) not in visited: # lower-middle
		neighbors.append((board[i+1][j], i+1, j))

	if i < len(board) - 1 and j < len(board[0]) - 1 and (i+1, j+1) not in visited: # lower-right
		neighbors.append((board[i+1][j+1], i+1, j+1))
		
	return neighbors
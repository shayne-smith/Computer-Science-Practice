# Time O(n + m) | Space O(1)  --- where n is the length of the matrix's rows
# and m is the length of the matrix's columns
def searchInSortedMatrix(matrix, target):
	top = 0
	right = len(matrix[0]) - 1
	
	while top < len(matrix) and right >= 0:
		if matrix[top][right] == target:
			return [top, right]
		elif target < matrix[top][right]:
			right -= 1
		else:
			top += 1
	return [-1, -1]
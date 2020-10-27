# Time O(n) | Space O(1) - where n is the length of the array
def isValidSubsequence(array, sequence):

	while len(sequence) != 0 and len(array) != 0:
		if sequence[0] == array[0]:
			sequence.pop(0)
			array.pop(0)
		else:
			array.pop(0)
	
	if len(sequence) == 0:
		return True
	else:
		return False
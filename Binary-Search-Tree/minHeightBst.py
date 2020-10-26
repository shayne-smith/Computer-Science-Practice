# Time O(nlog(n)) | Space O(n)
# Recursive, naive solution that uses BST insert method
def minHeightBst(array):
	return constructMinHeightBst(array, None, 0, len(array) - 1)

def constructMinHeightBst(array, bst, startIdx, endIdx):
	# base case
	if endIdx < startIdx:
		return

    # calculate middle index and value
	midIdx = (startIdx + endIdx) // 2
	valueToAdd = array[midIdx]

    # check if bst is None
	if bst is None:

        # establish root node if so
		bst = BST(valueToAdd)
	else:

        # otherwise add value to existing bst 
		bst.insert(valueToAdd)

    # recursively call constructMinHeightBst with updated start and stop indices
	constructMinHeightBst(array, bst, startIdx, midIdx - 1)
	constructMinHeightBst(array, bst, midIdx + 1, endIdx)
    
	return bst

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

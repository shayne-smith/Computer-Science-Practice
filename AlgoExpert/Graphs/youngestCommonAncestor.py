# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

# Time O(d) | Space O(d) -> d is depth of graph (ancestral tree)
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
	ancestorList1 = getAncestors(topAncestor, descendantOne)
	ancestorList2 = getAncestors(topAncestor, descendantTwo)
	
	for i in range(len(ancestorList1)):
		if ancestorList1[i] in ancestorList2:
			return ancestorList1[i]

def getAncestors(topAncestor, descendant):
	if topAncestor.name is descendant.name:
		return [topAncestor]
	ancestorList = []
	current = descendant
	ancestorList.append(current)
	while current.ancestor.name is not topAncestor.name:
		ancestorList.append(current.ancestor)
		current = current.ancestor
	ancestorList.append(current.ancestor)
	return ancestorList
	

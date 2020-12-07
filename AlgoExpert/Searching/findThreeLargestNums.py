# Time O(n) | Space O(1)
def findThreeLargestNumbers(array):
	# initialize output array with None values
	largest = [None] * 3
	# loop through input array
	for num in array:
		# check if None value in largest array
		if None in largest:
			for count, ele in enumerate(largest): # loop through output array
				# swap None for current integer and break innermost loop
				if ele is None:
					largest[count] = num
					break
		else:
			# find smallest integer in largest array
			smallest = min(largest)
			# if current integer is larger than smallest value in largest array
			if smallest < num:
				for count, ele in enumerate(largest): # loop through output array
					# swap smallest value for current integer and break innermost loop
					if ele == smallest:
						largest[count] = num
						break
	largest.sort() # sort output array before returning
	return largest
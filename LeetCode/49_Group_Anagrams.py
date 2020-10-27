# Time O(n^2)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dictList = []
        groupedList = []
        
        # O(n) -> n is length of strs
        for str in strs:
            s = {}
            
            if str != "":
                
                # create a dictionary of characters for each string in strs
                # O(c) -> c is number of characters in each str
                for char in str:
                    if char not in s:
                        s[char] = 1
                    else:
                        s[char] = s[char] + 1
                if s not in dictList:
                    dictList.append(s)
                    groupedList.append([str])
                else:

                    # O(g) -> g is number of lists in groupedList, which converges on n in worst case
                    for group in groupedList:
                        t = {}

                        # O(t) -> t is number of characters in each group in groupedList
                        for char in group[0]:
                            if char not in t:
                                t[char] = 1
                            else:
                                t[char] = t[char] + 1
                        if s == t:
                            group.append(str)
            else:
                if len(groupedList) != 0:
                    found = False
                    # O(g) -> g is number of lists in groupedList
                    for group in groupedList:
                        if group[0] == "":
                            found = True
                            group.append("")
                    if found == False:
                        groupedList.append([""])
                        
                else:
                    groupedList.append([""])
                    
        return groupedList
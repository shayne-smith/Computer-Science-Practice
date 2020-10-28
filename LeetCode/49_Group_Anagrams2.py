# Time O(NKlogK), N is length of strs, K is maximum length of a string in strs
# Space O(NK), the total information content stored in ans
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)

        # Time O(N)
        for s in strs:

            # Time O(KlogK)
            ans[tuple(sorted(s))].append(s)
        return ans.values()

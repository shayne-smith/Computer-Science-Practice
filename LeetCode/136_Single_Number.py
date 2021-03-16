class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cache = {}
        for num in nums:
            if num not in cache:
                cache[num] = '#'
            else:
                cache[num] = num
        for key, value in cache.items():
            if value == '#':
                return key
        return False

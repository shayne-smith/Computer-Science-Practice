"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        memo = {}
        def deepCopy(n):
            # Trivial Returns
            if not n:
                return
            if n in memo:
                return memo[n]
            #
            # Create node and register it immediately (to break cycles)
            memo[n] = new = Node( n.val )
            # 
            # Fix Node Properties
            new.next = deepcopy( n.next )
            new.random = deepcopy( n.random )
            return new
        return deepcopy(head)
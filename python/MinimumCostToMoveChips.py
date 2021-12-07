# Question No. 1217
# Minimum cost to Move Chips to the same position
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        even = 0
        for num in position:
            if num % 2 == 0:
                even += 1
        return min(even, len(position) - even)
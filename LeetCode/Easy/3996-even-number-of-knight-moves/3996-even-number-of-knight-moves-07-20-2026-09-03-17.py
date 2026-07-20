class Solution:
    # Optimal Approach
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    # here we have used manhattan distance, suppose on every odd number of move
    # the color of changes, and on even number of move, the color becomes same
    # even -> odd -> even -> odd and so on. so if manhattan distance is even,
    # it means it will take even moves to reach to target cell, otherwise odd
    def canReach(self, start: list[int], target: list[int]) -> bool:
        dx = abs(start[0] - start[1])
        dy = abs(target[0] - target[1])
        totalDistance = dx + dy
        if totalDistance % 2 == 0:
            return True
        return False      
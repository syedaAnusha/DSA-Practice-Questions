class Solution:
    # Brute Force Approach
    # Time Complexity : O(3n)
    # Space Complexity: O(2n)
    def findMaxCandiesSum(self, left, right):
        Sum = 0
        for i in range(len(left)):
            Sum += max(left[i], right[i])
        return Sum

    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        left = [1] * n
        right = [1] * n
        i = 1
        j = n-2
        # Left neighbors
        while i < n:
            if ratings[i] > ratings[i-1]:
                left[i] = left[i-1] + 1
            i += 1
        # Right neighbors
        while j >= 0:
            if ratings[j] > ratings[j+1]:
                right[j] = right[j+1] + 1
            j -= 1
        return self.findMaxCandiesSum(left, right)
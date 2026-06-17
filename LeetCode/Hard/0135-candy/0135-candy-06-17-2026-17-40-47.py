class Solution:
    # Better Approach
    # Time Complexity : O(2n)
    # Space Complexity: O(n)
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        left = [1] * n
        right = 1
        i = 1
        j = n-2
        # Left neighbors
        while i < n:
            if ratings[i] > ratings[i-1]:
                left[i] = left[i-1] + 1
            i += 1
        # Right neighbors
        minNumOfCandiesRequired = max(right, left[n-1])
        while j >= 0:
            current = 1
            if ratings[j] > ratings[j+1]:
                current = right + 1
                right = current
            else:
                right = 1
            minNumOfCandiesRequired += max(left[j], current)
            j -= 1
        return minNumOfCandiesRequired
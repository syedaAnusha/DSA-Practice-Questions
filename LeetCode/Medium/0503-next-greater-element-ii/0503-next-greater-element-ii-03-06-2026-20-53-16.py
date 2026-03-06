class Solution:
    # Brute Force Approach
    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        arrOfnextGreaterElements = [];
        isGreaterElemFound = False;
        N = len(nums);
        for i in range(N):
            for j in range(i+1, i+N+1):
                ind = j % N;
                if nums[ind] > nums[i]:
                    arrOfnextGreaterElements.append(nums[ind]);
                    isGreaterElemFound = True;
                    break;
            if not isGreaterElemFound:
                arrOfnextGreaterElements.append(-1);
            isGreaterElemFound = False;
        return arrOfnextGreaterElements;       
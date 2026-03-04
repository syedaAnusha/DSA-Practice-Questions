class Solution:
    # Optimal Approach
    # Time Complexity: O(2n) + O(n)
    # Space Complexity: O(n) + O(n) + O(2n)
    def findNextGreaterElement(self, nums):
        stack = [];
        mapOfNextGreaterElement = {};

        for i in range(len(nums)-1, -1, -1):
            while stack and nums[i] >= stack[-1]:
                stack.pop();
            if not stack:
                mapOfNextGreaterElement[nums[i]] = -1;
            else:
                mapOfNextGreaterElement[nums[i]] = stack[-1];
            stack.append(nums[i]);
        return mapOfNextGreaterElement;

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [];
        mapOfNextGreaterElement =  self.findNextGreaterElement(nums2);

        for i in range(len(nums1)):
            ans.append(mapOfNextGreaterElement[nums1[i]]);
        return ans;
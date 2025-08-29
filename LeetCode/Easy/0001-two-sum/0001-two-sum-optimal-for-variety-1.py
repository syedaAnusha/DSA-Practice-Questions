class Solution(object):
    # Slightly Better Approach for variety 1
    # Time Complexity: O(n) + O(nlogn) = O(nlogn)
    # Space Complexity: O(1) or O(n) if we are not allowed to distort an array
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums = sorted(nums); 
        left = 0;
        right =  len(nums)-1;
        while left < right:
            Sum = nums[left] + nums[right];
            if Sum > target:
                right -= 1;
            elif Sum < target:
                left += 1;
            else:
                return [left, right]; # return 'Yes'
        # return 'No'


        

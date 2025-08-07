class Solution:
    def findEqualPartitions(self, nums, target, ds, index):
        # Approach - 1
        if index == len(nums):
            if math.prod(ds) == target:
                if len(ds) >= 1:
                    return 1;
            return 0;

        else:
            ds.append(nums[index]);
            l = self.findEqualPartitions(nums, target, ds, index+1);
            ds.pop();
            r = self.findEqualPartitions(nums, target, ds, index+1);
        return l+r;

    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        if math.sqrt(math.prod(nums)) == target and len(nums) == 3 and 1 not in nums: 
            val = self.findEqualPartitions(nums, target, [], 0);
            if val >= 2:
                return True;
            return False;
        elif math.sqrt(math.prod(nums)) == target and len(nums) > 3:
            val = self.findEqualPartitions(nums, target, [], 0);
            if val >= 2:
                return True;
            return False;
        else:
            return False;
        
         
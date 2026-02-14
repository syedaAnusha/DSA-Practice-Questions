class Solution:
    # Brute Force Approach
    # Time Complexity: O(4^n) // for three operators and with no operator when index = 0;
    # Space Complexity: O(n)
    def generateAllValidExpressions(self, index, nums, target, curRes, lastOperand, exp, resArr):
        if index == len(nums):
            if curRes == target:
                resArr.append(exp);
            return;

        for i in range(index, len(nums)):
            if i > index and nums[index] == "0":
                return;
            
            curNum = nums[index:i+1];
            curNumVal = int(curNum);
            if index == 0:
                self.generateAllValidExpressions(i+1, nums, target, curNumVal, curNumVal, curNum, resArr);
            else:
                self.generateAllValidExpressions(i+1, nums, target, curRes + curNumVal, curNumVal, exp+"+"+curNum, resArr);
                self.generateAllValidExpressions(i+1, nums, target, curRes - curNumVal, -curNumVal, exp+"-"+curNum, resArr);
                self.generateAllValidExpressions(i+1, nums, target, (curRes - lastOperand) + (lastOperand * curNumVal), (lastOperand * curNumVal), exp+"*"+curNum, resArr);

    def addOperators(self, num: str, target: int) -> List[str]:
        index = 0;
        curRes = 0;
        exp = "";
        lastOperand = 0;
        resArr = [];
        self.generateAllValidExpressions(index, num, target, curRes, lastOperand, exp, resArr);
        return resArr;
class Solution:
    # Better Approach
    # Time Complexity:O(n) + O(n) = O(2n)
    # Space Complexity: O(n)
    def moveValuesFromStackToArray(self, stack):
        array = [];
        while stack:
            array.append(stack.pop());
        return array;
    
    def storeValuesInReverseOrder(self, fromArray, toStack):
        i = 0;
        while i < len(fromArray):
            toStack.append(fromArray[i]);
            i += 1;
        return toStack; 
        
    def reverseStack(self, st):
        # code here
        tempArr = self.moveValuesFromStackToArray(st);
        return self.storeValuesInReverseOrder(tempArr, st);

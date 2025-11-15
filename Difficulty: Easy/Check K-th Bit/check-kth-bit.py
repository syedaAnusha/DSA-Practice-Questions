class Solution:
    # Brute Force Approach
    # Time Complexity: O(log n)
    # Space Complexity: O(log n)
    def convertToBinary(self, n):
        binary = "";
        while n > 0:
            if n % 2 != 0:
                binary += "1";
            else:
                binary += "0";
            n = n // 2;
            
        return binary;
        
    def checkKthBit(self, n, k):
        # code here
        binary = self.convertToBinary(n); 
        if len(binary) > k:
            if binary[k] == "1":
                return True;
            else:
                return False;
        return False;
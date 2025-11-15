#User function Template for python3
class Solution:
    # Optimal Approach
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def bitManipulation(self, num, i):
        # Code here
        i = i-1; # for (1-based) indexing
        bitMask = 1 << i;
        getIthBit = "0";
        # Get the ith bit
        if (num & bitMask):
            getIthBit = "1";
        
        # Set the ith bit
        setIthBit = num | bitMask;
        
        # clear the ith bit
        clearIthBit = num & (~(bitMask));
        
        print(getIthBit,setIthBit,clearIthBit);
        
        
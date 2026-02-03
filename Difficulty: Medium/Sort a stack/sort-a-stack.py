class Solution:
    # Brute Approach - 01
    # Time Complexity:O(n^2)
    # Space Complexity:O(n)
    def insertVal(self, st, curVal):
        if not st or curVal > st[-1]:
            st.append(curVal);
            return st;
        val = st.pop();
        self.insertVal(st, curVal);
        st.append(val);
        return st;
        
    def sortStack(self, st):
        # code here 
        if st:
            curVal = st.pop();
            self.sortStack(st);
            self.insertVal(st, curVal); 
            return st;
        
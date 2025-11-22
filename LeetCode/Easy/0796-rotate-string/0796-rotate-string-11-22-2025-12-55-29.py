class Solution:
    # Brute Force Approach
    # Time Complexity: O(n*n*n) = O(n^3)
    # Space Complexity: O(1)
    def rotateStr(self, lst, char):
        temp = [];
        n = len(lst);
        for i in range(1,n):
            temp.append(lst[i]);
        temp.append(char);
        return temp;

    def rotateString(self, s: str, goal: str) -> bool:
        lst = list(s);
        n = len(lst);
        for i in range(n):
            rotatedLst = self.rotateStr(lst, lst[0]);
            rotatedStr = "".join(rotatedLst);
            if rotatedStr == goal:
                return True;
            lst = rotatedLst;
        return False;
        
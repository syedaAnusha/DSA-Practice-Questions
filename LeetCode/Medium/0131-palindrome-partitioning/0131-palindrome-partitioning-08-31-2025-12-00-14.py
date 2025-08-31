class Solution(object):
    def checkIsPalindrome(self, s, i, j):
        while i <= j:
            if s[i] != s[j]:
                return False;
            i += 1;
            j -= 1;
        return True;

    def findPartition(self, s, ans, ds, index):
        if index == len(s):
            ans.append(list(ds));
            return;

        for i in range(index, len(s)):
            if self.checkIsPalindrome(s, index, i):
                ds.append(s[index:i+1]);
                self.findPartition(s, ans, ds, i+1);
                ds.pop();

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        ans = [];
        index = 0;
        ds = [];
        self.findPartition(s, ans, ds, index);
        return ans;

        
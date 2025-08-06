class Solution(object):
    def isValidPalindrome(self, start, end, s):
        while(start <= end):
            if s[start] != s[end]:
                return False;
            start += 1;
            end -= 1;
        return True;

    def findPalindromPartitions(self, ds, ans, s, N, index):
        if index == N:
            ans.append(list(ds));
            return;

        for i in range(index, N):
            if self.isValidPalindrome(index, i, s):
                ds.append(s[index:i+1]);
                self.findPalindromPartitions(ds, ans, s, N, i+1);
                ds.pop();      

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        ans = [];
        ds = [];
        index = 0;
        N = len(s);
        self.findPalindromPartitions(ds, ans, s, N, index);
        return ans;
class Solution:
    # Time Complexity ≈ O(n+T) ≈ O(T)
    # Space Complexity ≈ O(n) + O(T)
    def findDecodedStr(self, s, i):
        res = '';
        num = 0;
        while i < len(s):
            if s[i].isdigit():
                num = num * 10 + int(s[i]);
            elif s[i] == '[':
                substr, i = self.findDecodedStr(s, i+1);
                res += num * substr;
                num = 0;
            elif s[i] == ']':
                return res, i;
            else:
                res += s[i];
            i += 1;
        return res;

    def decodeString(self, s: str) -> str:
        return self.findDecodedStr(s, 0);
        
      


       
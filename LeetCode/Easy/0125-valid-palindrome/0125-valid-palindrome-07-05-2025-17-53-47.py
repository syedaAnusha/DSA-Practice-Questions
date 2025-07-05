class Solution(object):
    def checkPalindrome(self, i, arr, n):
        if i >= n/2:
            return True;
        if arr[i] != arr[n-i-1]:
            return False;
        else:
            return self.checkPalindrome(i+1, arr, n);


    def removeAllNonAlphaNum(self, s):
        filteredText = "";
        for i in s:
            if i.isalnum():
                filteredText += i.lower();
        return list(filteredText);

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_str_arr = self.removeAllNonAlphaNum(s);
        len_new_str_arr = len(new_str_arr);
        return self.checkPalindrome(0, new_str_arr, len_new_str_arr);
        
        
class Solution:
    # Optimal Approach
    # Time Complexity: O(n) 
    # Space Complexity: O(1)
    def reverseWords(self, s: str) -> str:
        left = 0
        right = len(s) - 1

        temp = ""
        ans = ""

        # Step 1: Trim leading and trailing spaces manually
        while left <= right and s[left] == ' ':
            left += 1
        while right >= 0 and s[right] == ' ':
            right -= 1

        # Step 2: Iterate and build reversed sentence
        while left <= right:
            ch = s[left]

            if ch != ' ':
                temp += ch
            else:
                # Skip multiple spaces
                if temp != "":
                    if ans != "":
                        ans = temp + " " + ans
                    else:
                        ans = temp
                    temp = ""

            left += 1

        # Step 3: Add the last word
        if temp != "":
            if ans != "":
                ans = temp + " " + ans
            else:
                ans = temp

        return ans
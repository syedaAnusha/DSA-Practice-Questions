class Solution:
    # Better Approach
    # Time Complexity: O(n * m)
    # Space Complexity: O(1)

    def minWindow(self, s1, s2):
        # Code here
        if not s1 or not s2:
            return ""

        min_len = float('inf')
        res = ""
        i, j = 0, 0

        while i < len(s1):
            # Forward pass: Check if s2 is a subsequence of s1
            if s1[i] == s2[j]:
                j += 1

                # If the entire s2 is found in s1
                if j == len(s2):
                    end = i
                    j -= 1

                    # Backward pass: Minimize the window
                    while j >= 0:
                        if s1[i] == s2[j]:
                            j -= 1
                        i -= 1

                    start = i + 1
                    length = end - start + 1

                    # Update the absolute minimum window
                    if length < min_len:
                        min_len = length
                        res = s1[start:start + length]

                    # Reset pointers for the next search
                    i = start
                    j = 0

            i += 1

        return res
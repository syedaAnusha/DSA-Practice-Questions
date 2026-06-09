class Solution:
    # Optimal Approach
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def lemonadeChange(self, bills: List[int]) -> bool:
        fiveDollars = tenDollars = 0;
        for amount in bills:
            if amount == 5:
                fiveDollars += 1;
            elif amount == 10:
                tenDollars += 1;
                if fiveDollars:
                    fiveDollars -= 1;
                else:
                    return False;
            elif amount == 20:
                if fiveDollars and tenDollars:
                    fiveDollars -= 1;
                    tenDollars -= 1;
                elif fiveDollars >= 3:
                    fiveDollars -= 3;
                else:
                    return False;

        return True;        
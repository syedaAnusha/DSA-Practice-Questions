class Solution:
    # Optimal Approach
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def lemonadeChange(self, bills: List[int]) -> bool:
        fiveDollars = tenDollars = twentyDollars = 0;
        for amount in bills:
            if amount == 5:
                fiveDollars += 1;
            elif amount == 10:
                tenDollars += 1;
                if fiveDollars > 0:
                    fiveDollars -= 1;
                else:
                    return False;
            elif amount == 20:
                twentyDollars += 1;
                if fiveDollars > 0 and tenDollars > 0:
                    fiveDollars -= 1;
                    tenDollars -= 1;
                elif fiveDollars > 0 and tenDollars == 0:
                    fiveDollars -= 3;
                    if fiveDollars < 0:
                        return False;
                else:
                    return False;

        return True;        
class Solution:
    # Brute Force Approach
    # Time Complexity: O(n^3)
    # Space Complexity: O(n)
    def findMaxAndMinFreqCount(self, mapFreq):
        maxFreq = max(mapFreq.values());
        minFreq = min(mapFreq.values());
        return (maxFreq, minFreq);
        
    def beautySum(self, s: str) -> int:
        sumOfSubStrs = 0;
        n = len(s);
        maxFreq = float('-inf');
        minFreq = float('inf'); 

        for i in range(n):
            mapCharFreq = {s[i]:1};
            for j in range(i+1,n):
                if s[j] in mapCharFreq:
                    mapCharFreq[s[j]] += 1;
                else:
                    mapCharFreq[s[j]] = 1;

                freqCountTple = self.findMaxAndMinFreqCount(mapCharFreq);
                mostFreq = max(freqCountTple[0], maxFreq);
                leastFreq = min(freqCountTple[1], minFreq);
                beautyOfSubStr = mostFreq - leastFreq;
                if beautyOfSubStr > 0:
                    sumOfSubStrs += beautyOfSubStr; 

        return sumOfSubStrs;

        
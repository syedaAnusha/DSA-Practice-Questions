#User function Template for python3

class Solution:
    # Optimal Solution
    # Time Complexity: O(n log log n) + O(n * log n )
    # Space Complexity: O(n)
    def __init__(self):
        self.primeSet = self.sieve()
        
    def sieve(self):
        n = 1000000;
        primeSet = [i for i in range(n+1)];
        i = 2;
        
        while i*i <= n:
            if primeSet[i] == i:
                j = i*i;
                while j <= n:
                    if primeSet[j] == j:
                        primeSet[j] = i;
                    j += i;
            i += 1;
        return primeSet;
        
    def findPrimeFactors(self, N):
        # Code here
        #primeSet = self.sieve();
        ans = [];
        while N != 1:
            ans.append(self.primeSet[N]);
            #print('factor', primeSet[N]);
            N = N // self.primeSet[N];
        return ans;
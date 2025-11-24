class Solution:
    def primeFac(self, n):
        # code here
        i = 2;
        primeSet = [];
        while i*i <= n:
            if i*i <= n and n % i == 0:
                n = n // i;
                if len(primeSet) == 0 or primeSet[-1] != i:
                    primeSet.append(i);
            elif i*i <= n and n % i != 0:
                i += 1;
        if len(primeSet) == 0:
            return [n];
        else:
            if primeSet[-1] != n:
                primeSet.append(n);
            return primeSet;
            
        
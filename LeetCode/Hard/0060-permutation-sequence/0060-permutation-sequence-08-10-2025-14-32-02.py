class Solution:
    # Time Complexity : O(n)*O(n)
    # Space Complexity: O(n)
    def findPermutations(self, n, k):
        fact = 1;
        numbers = [];
        for i in range(1, n):
            fact = fact * i;
            numbers.append(i); 
        numbers.append(i+1);

        ans = '';
        k = k-1;
        while True:
            index = k // fact;
            ans = ans + str(numbers[index]);
            numbers.remove(numbers[index]);
            if len(numbers) == 0:
                break;

            k = k % fact;
            fact = fact // len(numbers);
        return ans;

    def getPermutation(self, n: int, k: int) -> str:
        if n == 1 and k == 1:
            return '1';
        else:
            return self.findPermutations(n, k);
        
            
        

        
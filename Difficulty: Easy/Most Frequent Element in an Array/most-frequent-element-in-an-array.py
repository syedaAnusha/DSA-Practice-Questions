class Solution:
    def mostFreqEle(self, arr):
        # code here
        hashTable = {};
        maxFreq = 0;
        highestElem = float('-inf');
        
        for i in range(len(arr)):
            if arr[i] in hashTable:
                hashTable[arr[i]] += 1;
            else:
                hashTable[arr[i]] = 1;
            maxFreq = max(maxFreq, hashTable[arr[i]]);
           
        for key, value in hashTable.items():
            if value == maxFreq:
                highestElem = max(highestElem, key);
                
        return highestElem;
                
        
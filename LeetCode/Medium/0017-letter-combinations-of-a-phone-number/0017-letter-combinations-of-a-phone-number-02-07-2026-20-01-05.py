class Solution:
    # Brute Force Approach
    # Time Complexity:O(4^n*n)
    # Space Complexity:O(n)
    def generateAllLetterCombinations(self, digits, index, resArr, digitStr, digitLettersMap):
        if index == len(digits):
            resArr.append(digitStr);
            return resArr;
        curDigitLetters = digitLettersMap[digits[index]];
        for i in range(len(curDigitLetters)):
            digitStr += curDigitLetters[i];
            self.generateAllLetterCombinations(digits, index+1, resArr, digitStr, digitLettersMap);
            digitStr = digitStr[:-1];
                
    def letterCombinations(self, digits: str) -> List[str]:
        digitLettersMap = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno",
                            "7":"pqrs", "8":"tuv", "9":"wxyz"};
        resArr = [];
        index = 0;
        digitStr = "";
        self.generateAllLetterCombinations(digits, index, resArr, digitStr, digitLettersMap);
        print('len', len(resArr));
        return resArr; 
class Solution(object):
    def findCombinations(self, candidates, target, finalList, index, templist):
        if index == len(candidates):
            if target == 0:
                finalList.append(list(templist))
            return;
        else:
            if (candidates[index] <= target):
                # pick an element again
                templist.append(candidates[index]);
                self.findCombinations(candidates, target-candidates[index], finalList, index, templist);
                # remove an element from templist while backtrack
                templist.remove(candidates[index])
            # not pick an element
            self.findCombinations(candidates, target, finalList, index+1, templist);


    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        finalList = [];
        self.findCombinations(candidates, target, finalList, 0, []);
        return finalList;
        
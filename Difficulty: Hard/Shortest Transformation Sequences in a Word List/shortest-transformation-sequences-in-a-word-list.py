from collections import deque
class Solution:
    # Brute Force Approach
    # Time Complexity: O(N × L × 26 + S × L), where N is the length of wordList, 
    # L = length of the word in wordList
    # S = number of shortest sequences
    # Space Complexity: O(N × L + S × L) 
    def bfs(self, wordSet, beginWord, endWord, que, usedOnLevel, level, ans): 
        while que:
            path = que.popleft()
            if len(path) > level:
                level += 1
                for word in usedOnLevel:
                    wordSet.discard(word)
                usedOnLevel = set()

            word = path[-1]
            if word == endWord:
                if not ans:
                    ans.append(path[:])
                elif len(ans[-1]) == len(path): # we need all shortest paths sequences only
                    ans.append(path[:])
            
            for i in range(len(word)):
                for letter in 'abcdefghijklmnopqrstuvwxyz':
                    newWord = word[:i] + letter + word[i+1:]
                    if newWord in wordSet:
                        path.append(newWord)
                        que.append(path[:]) # created new shallow copy
                        usedOnLevel.add(newWord)
                        path.pop()

        return ans
        
    def findSequences(self, words, s, e):
        # code here
        wordSet = set(words)
        que = deque([[s]])
        usedOnLevel = {s}
        level = 0
        ans = []
        self.bfs(wordSet, s, e, que, usedOnLevel, level, ans)
        return ans  
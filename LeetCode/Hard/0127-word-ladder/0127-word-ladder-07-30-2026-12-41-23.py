from collections import deque
class Solution:
    # Brute Force Approach
    # Time Complexity: O(N * M * 26), where N is the length of wordList, M = length of the word in wordList
    # Space Complexity: O(N) + O(N) 
    def bfs(self, que, wordSet, alphabets, endWord):
        while que:
            word, step = que.popleft()
            if word == endWord:
                return step

            for i in range(len(word)):
                for letter in alphabets:
                    newWord = word[:i] + letter + word[i+1:]
                    if newWord in wordSet:
                        wordSet.remove(newWord)
                        que.append((newWord, step+1))
        return 0

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        que = deque([(beginWord, 1)])
        wordSet = set(wordList)
        if beginWord in wordSet:
            wordSet.remove(beginWord)

        alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                    's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        
        return self.bfs(que, wordSet, alphabets, endWord)        
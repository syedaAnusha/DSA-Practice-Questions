from collections import deque
class Solution:
    # Optimal Approach
    # Time Complexity: O(1000 * N)
    # Space Complexity: O(1000)
    def bfs(self, q, end, arr, distance):
        while q:
            steps, num = q.popleft()
            for i in range(len(arr)):
                newNum = (num * arr[i]) % 1000
                if steps+1 < distance[newNum]:
                    if newNum == end:
                        return steps+1
                    distance[newNum] = steps+1
                    q.append((steps+1, newNum))
                
        return -1
                
    def minSteps(self, arr, start, end):
        # code here
        # edge case: if start and end are equal
        if start == end:
            return 0
        q = deque([])
        q.append((0, start))
        distance = [float('inf')] * 1000
        distance[start] = 0 
        return self.bfs(q, end, arr, distance)
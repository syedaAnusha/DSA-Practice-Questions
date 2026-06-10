class Solution:
    # Optimal Approach
    # Time Complexity: O(n log n) + O(n)
    # Space Complexity: O(1)
    def solve(self, bt):
        # code here
        waitingTime = 0;
        time = 0;
        bt.sort();
        for process in bt:
            time += waitingTime;
            waitingTime += process
            
        avgWaitingTime = time // len(bt);
        return avgWaitingTime;
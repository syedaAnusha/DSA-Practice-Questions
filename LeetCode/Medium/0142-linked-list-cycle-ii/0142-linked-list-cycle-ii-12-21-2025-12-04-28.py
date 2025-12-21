# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Brute Force Approach
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return None;

        nodeMap = {};
        temp = head;
        nodeCnt = -1;

        while temp != None:
            if temp in nodeMap:
                return temp;
            nodeCnt += 1;
            nodeMap[temp] = nodeCnt; 
            temp = temp.next;
        return temp;
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Brute Force Approach
    # Time Complexity: O(n) + O(m)
    # Space Complexity: O(n)
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        tempA = headA;
        tempB = headB;
        tempAMap = {};
        if tempA == None or tempB == None:
            return None;
        while tempA != None:
            tempAMap[tempA] = 1;
            tempA = tempA.next;

        while tempB != None:
            if tempB in tempAMap:
                return tempB;
            tempB = tempB.next;
        
        return None;
        
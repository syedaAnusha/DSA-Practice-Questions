# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Optimal Approach
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None:
            return False;
        
        slowPtr = head;
        fastPtr = head;
        while fastPtr != None and fastPtr.next != None:
            slowPtr = slowPtr.next;
            fastPtr = fastPtr.next.next;
            if slowPtr == fastPtr:
                return True;
        return False;
        
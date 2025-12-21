# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Optimal Approach
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return None;
        
        slowPtr = head;
        fastPtr = head;

        while fastPtr != None and fastPtr.next != None:
            slowPtr = slowPtr.next;
            fastPtr = fastPtr.next.next;
            if slowPtr == fastPtr:
                slowPtr = head;
                while slowPtr != fastPtr:
                    slowPtr = slowPtr.next;
                    fastPtr = fastPtr.next;
                return slowPtr;
        return None; 

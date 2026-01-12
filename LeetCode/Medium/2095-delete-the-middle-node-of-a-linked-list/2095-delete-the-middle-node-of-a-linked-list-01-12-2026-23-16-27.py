# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Brute Force Approach
    # Time Complexity: O(n/2)
    # Space Complexity: O(1)
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return None;
 
        slowPtr = head;
        fastPtr = head.next.next;

        while fastPtr != None and fastPtr.next != None:
            slowPtr = slowPtr.next;
            fastPtr = fastPtr.next.next;
        
        slowPtr.next = slowPtr.next.next;
        return head;
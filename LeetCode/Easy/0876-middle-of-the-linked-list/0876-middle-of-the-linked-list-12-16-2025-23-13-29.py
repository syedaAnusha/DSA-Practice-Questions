# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Optimal Approach
    # Time Compexity: O(n)
    # Space Compexity: O(1)
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fastPtr = head;
        slowPtr = head;

        while fastPtr != None and fastPtr.next != None:
            slowPtr = slowPtr.next;
            fastPtr = fastPtr.next.next;
        
        return slowPtr;
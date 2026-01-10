# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Optimal Approach
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head;
        evenTempNode = head.next;
        temp = head;
        while temp.next != None and temp.next.next != None:
            evenNode = temp.next;
            temp.next = temp.next.next;
            temp = temp.next;
            evenNode.next = temp.next;
        
        temp.next = evenTempNode;
        return head;


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Optimal Approach - 2
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head;

        evenHead = head.next;
        oddNode = head;
        evenNode = head.next;
        while evenNode != None and evenNode.next != None:
            oddNode.next = oddNode.next.next;
            evenNode.next = evenNode.next.next;

            oddNode = oddNode.next;
            evenNode = evenNode.next;
        
        oddNode.next = evenHead;
        return head;
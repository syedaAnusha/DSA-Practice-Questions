# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Brute Force Approach
    # Time Complexity: O(n) + O(n/2) = O(3n / 2)
    # Space Complexity: O(1)
    def getLengthOfLinkedList(self, head):
        temp = head;
        cnt = 0;
        while temp != None:
            cnt += 1;
            temp = temp.next;
        return cnt;

    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return None;

        lengthOfLinkedList = self.getLengthOfLinkedList(head);
        midNodeIndex = math.floor(lengthOfLinkedList / 2);
        temp = head;

        while temp != None:
            if midNodeIndex == 1:
                delNode = temp.next;
                temp.next = delNode.next;
                delNode.next = None;
                return head;
            temp = temp.next;
            midNodeIndex -= 1;
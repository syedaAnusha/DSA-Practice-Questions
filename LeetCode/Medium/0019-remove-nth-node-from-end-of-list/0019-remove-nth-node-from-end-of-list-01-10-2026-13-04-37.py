# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Brute Force Approach - 2
    # Time Complexity: O(n) + O(n) = O(2n)
    # Space Complexity: O(1)
    def getTotalNodes(self,head):
        cnt = 0;
        temp = head;
        while temp != None:
            cnt += 1;
            temp = temp.next;
        return cnt;

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Edge cases
        if head == None or (head.next == None and n == 1):
            return None;
        
        temp = head;
        totalNodes = self.getTotalNodes(temp);
        targetNodeIndex = totalNodes - n;

        if targetNodeIndex == 0:
            head = head.next;
            return head;

        while temp != None:
            if targetNodeIndex == 1:
                delNode = temp.next;
                temp.next = temp.next.next;
                return head;
            targetNodeIndex -= 1;
            temp = temp.next; 
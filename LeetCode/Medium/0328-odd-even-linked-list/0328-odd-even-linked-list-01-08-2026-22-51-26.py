# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Brute Force Approach
    # Time Complexity: O(n) + O(n) = O(2n)
    # Space Complexity: O(n)
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head;

        cnt = 1;
        temp = head;
        oddArr = [];
        evenArr = [];
        while temp != None:
            if cnt % 2 == 0:
                evenArr.append(temp.val);
            else:
                oddArr.append(temp.val);
            cnt += 1;
            temp = temp.next;
       
        temp = head;
        i = 0;
        while i < len(oddArr):
            temp.val = oddArr[i];
            i += 1;
            temp = temp.next;
        i = 0;
        while i < len(evenArr):
            temp.val = evenArr[i];
            i += 1;
            temp = temp.next;
        return head;
            




        
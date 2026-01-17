# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Optimal Approach
    # Time Complexity: O(max (l1, l2)) 
    # Space Complexity: O(max(l1, l2))
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 == None and l2 == None:
            return None;
        temp1 = l1;
        temp2 = l2;
        dummyNode = ListNode(-1);
        mover = dummyNode;
        carry = 0;
        while temp1 != None or temp2 != None:
            Sum = carry;
            if temp1:
                Sum += temp1.val;
            if temp2:
                Sum += temp2.val;
            node = ListNode(Sum  % 10);
            mover.next = node;
            mover = node;
            carry = Sum // 10;
            if temp1:
                temp1 = temp1.next;
            if temp2:
                temp2 = temp2.next;
        if carry:
            node = ListNode(carry);
            mover.next = node;
            mover = node;
        return dummyNode.next;
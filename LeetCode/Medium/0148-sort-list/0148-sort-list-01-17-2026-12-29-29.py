# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Optimal Approach
    # Time Complexity: O(log N) * O(N + N/2) = O(log N) * O(N)
    # Space Complexity: O(1)
    # Aux space: O(log N) for recursion call
    def findMidNode(self, head):
        slow = head;
        fast = head.next;

        while fast != None and fast.next != None:
            slow = slow.next;
            fast = fast.next.next;
        return slow;
    
    def mergeLinkedLists(self, leftHead, rightHead):
        dummyNode = ListNode(-1);
        temp = dummyNode;
        while leftHead != None and rightHead != None:
            if leftHead.val < rightHead.val:
                temp.next = leftHead;
                temp = leftHead;
                leftHead = leftHead.next;
            else:
                temp.next = rightHead;
                temp = rightHead;
                rightHead = rightHead.next;
        if leftHead:
            temp.next = leftHead;
        else:
            temp.next = rightHead;
        return dummyNode.next;

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head;
        middleNode = self.findMidNode(head);
        leftHead = head;
        rightHead = middleNode.next;
        middleNode.next = None;
        leftLinkedListHead = self.sortList(leftHead);
        rightLinkedListHead = self.sortList(rightHead);
        return self.mergeLinkedLists(leftLinkedListHead, rightLinkedListHead);
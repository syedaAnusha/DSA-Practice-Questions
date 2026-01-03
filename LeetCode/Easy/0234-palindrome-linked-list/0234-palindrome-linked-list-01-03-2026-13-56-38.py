# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Optimal Approach
    # Time Complexity: O(n/2) + O(n/2) = O(2n)
    # Space Complexity: O(1)
    def findMidNode(self, temp):
        slowPtr = temp;
        fastPtr = temp;

        while fastPtr.next != None and fastPtr.next.next != None:
            slowPtr = slowPtr.next;
            fastPtr = fastPtr.next.next;
        return slowPtr;
    
    def reverseLinkedList(self, node):
        if node == None or node.next == None:
            return node;
        newHead = self.reverseLinkedList(node.next);
        front = node.next;
        front.next = node;
        node.next = None;
        return newHead;
      
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None:
            return True;
        
        temp = head;
      
        # find middle node
        midNode = self.findMidNode(temp);
        newHead = self.reverseLinkedList(midNode.next);

        first = head;
        last = newHead;

        while last != None:
            if first.val != last.val:
                self.reverseLinkedList(newHead);
                return False
            first = first.next;
            last = last.next;
        self.reverseLinkedList(newHead);
        return True;


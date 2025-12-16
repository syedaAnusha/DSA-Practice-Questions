# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Brute Force Approach
    # Time Compexity: O(n) + O(n/2)
    # Space Compexity: O(1)
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        currNode = head;
        cntNodes = 0;

        if head == None or head.next == None:
            return head;

        while currNode != None:
            cntNodes += 1;
            currNode = currNode.next;
        
        temp = head;
        middleNode = (cntNodes // 2) + 1;
        while temp != None:
            middleNode -= 1;
            if middleNode == 0:
                break;
            temp = temp.next;
        
        return temp;
        
            
        
        
        
        
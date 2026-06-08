import heapq;
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Optimal Approach
# Time Complexity: O(k log k) + O(n*k log k)
# Space Complexity: O(k) + O(k*n) for output 
class Solution:
    def getSortedList(self, lists):
        minHeap = [];
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(minHeap, (node.val, i, node));
        dummyNode = ListNode(0);
        temp = dummyNode;
        while minHeap:
            nodeValue, i, node = heapq.heappop(minHeap);
            temp.next = node;
            temp = temp.next;

            if node.next:
                heapq.heappush(minHeap, (node.next.val, i, node.next));

        return dummyNode.next;

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return self.getSortedList(lists);     
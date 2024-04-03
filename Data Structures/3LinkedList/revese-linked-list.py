# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# LinkedList(val: 1, next: LinkedList(val: 1, next: None)), 1, tahan = 2, 2 = None, None = 1, 1 = 2, tampung None, None = 1, 1, None 
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            temp = curr.next # 2
            curr.next = prev #  None
            prev = curr # 1
            curr = temp # 
        print("prev.next: ", prev.next)
        return prev

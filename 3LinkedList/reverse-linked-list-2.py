# Problem link: leetcode.com/problems/reverse-linked-list-ii
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
		prev, curr = None, head

		temp1 = curr
		curr = curr.next
		temp = None
		if left <= right:
			while curr and curr.next != None:
				temp = curr.next
				curr.next = prev
				prev = curr
				curr = temp

		temp1.next = prev
		data = prev

		while data:
			if data.next == None:
				data.next = curr

			data = data.next
		print('nilai curr: ', curr)
		print('nilai temp: ', temp)
		return temp1

testObj = Solution()

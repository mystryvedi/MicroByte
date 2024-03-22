# 234. Palindrome Linked List

# Given the head of a singly linked list, return true if it is a 
# palindrome
#  or false otherwise.
   
# Example 1:

# Input: head = [1,2,2,1]
# Output: true
# Example 2:

# Input: head = [1,2]
# Output: false

# Constraints:

# The number of nodes in the list is in the range [1, 105].
# 0 <= Node.val <= 9

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        slow = head
        fast = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        if fast:
            slow = slow.next
        while prev and slow:
            if prev.val != slow.val:
                return False
            prev = prev.next
            slow = slow.next

        return True

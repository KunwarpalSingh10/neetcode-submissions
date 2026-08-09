# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        
        while fast and fast.next: # to break the list into two halfs
            slow = slow.next
            fast = fast.next.next
        
        # reverse the second half
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        #now we are going to merge the two linked lists
        first = head
        second = prev

        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            first = tmp1
            second.next = first
            second = tmp2


        


            
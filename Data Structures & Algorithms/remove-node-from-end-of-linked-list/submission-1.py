# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 1
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        head = prev
        
        if n == 1:
            head = head.next
        else:
            while prev:
                curr = prev
                prev = prev.next
                count += 1
                if count == n and prev:
                    curr.next = prev.next
                    prev = None
                    break
        
        curr = head
        prev = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        return prev
                

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current = head
        prev = None
        if head == None:
            return head
        while True:
            if current.next == None:
                return head
            if current.val != (current.next).val:
                prev = current
                current = current.next
            else:
                duplicate_val = current.val
                while current.next.val == duplicate_val:
                    current.next = current.next.next
                    if current.next == None:
                        if prev == None:
                            return None
                        prev.next = None
                        return head
                current.val = current.next.val
                current.next = current.next.next

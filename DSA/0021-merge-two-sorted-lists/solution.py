# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None or list2 is None:
            if list1 is None:
                return list2
            elif list2 is None:
                return list1
        if list1.val <= list2.val:
            head = list1
            prev = list1
            curr1 = list1.next
            curr2 = list2
        else:
            head = list2
            prev = list2
            curr1 = list1
            curr2 = list2.next
        while curr1 is not None and curr2 is not None:
            if curr1.val <= curr2.val:
                prev.next = curr1
                prev = curr1
                curr1 = curr1.next
            elif curr1.val > curr2.val:
                prev.next = curr2
                prev = curr2
                curr2 = curr2.next
        if curr1 is None:
            prev.next = curr2
        elif curr2 is None:
            prev.next = curr1
        return head

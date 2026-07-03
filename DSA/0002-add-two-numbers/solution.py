# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        place = 0
        num1 = l1.val
        num2 = l2.val

        curr = l1

        while (curr.next != None):
            place += 1
            curr = curr.next
            num1 += curr.val * (10 ** place)
        
        place = 0
        curr = l2

        while (curr.next != None):
            place += 1
            curr = curr.next
            num2 += curr.val * (10 ** place)
        
        total = num1 + num2

        result = ListNode(total % 10, None)
        total = total // 10

        curr = result

        while (total != 0):
            temp = ListNode(total % 10, None)
            total = total // 10
            curr.next = temp
            curr = temp
        
        return result

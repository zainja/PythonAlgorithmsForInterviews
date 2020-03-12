class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        main_return = l3 = ListNode(0)
        carry = 0
        while l1 or l2 or carry != 0:
            sum = l1.val + l2.val + carry
            carry = 0
            if sum >= 10:
                carry = sum - 9
                sum = 0
            l3.next = ListNode(sum)
            l3 = l3.next
            l1 = l1.next
            l2 = l2.next
        return main_return.next
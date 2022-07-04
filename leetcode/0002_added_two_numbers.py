# https://leetcode.com/problems/add-two-numbers/


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode],
                      l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return None
        head_node, cur_node = None, None
        reminder = 0
        while l1 or l2:
            cur_number = reminder
            if l1:
                cur_number += l1.val
                l1 = l1.next
            if l2:
                cur_number += l2.val
                l2 = l2.next
            reminder = cur_number // 10
            cur_val = cur_number % 10
            if not head_node:
                head_node = ListNode(cur_val, None)
                cur_node = head_node
            else:
                cur_node.next = ListNode(cur_val, None)
                cur_node = cur_node.next
        if reminder:
            cur_node.next = ListNode(reminder, None)
        return head_node

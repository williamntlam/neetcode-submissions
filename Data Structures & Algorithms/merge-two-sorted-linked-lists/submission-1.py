# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # merge the two lists in O(n) time
        # have a pointer for each linked list and always append the one with the 
        # lower value and then increment the pointer.
        # runtime: O(n)
        # spacetime: O(1)

        current_one = list1
        current_two = list2

        head_new = ListNode()
        current_new = head_new

        while current_one is not None and current_two is not None:
            if current_one.val <= current_two.val:
                new_node = ListNode(current_one.val)
                current_new.next = new_node
                current_new = new_node
                current_one = current_one.next
            else:
                new_node = ListNode(current_two.val)
                current_new.next = new_node
                current_new = new_node
                current_two = current_two.next

        # if current_one is not None:
        #     current_new.next = current_one
        # else:
        #     current_new.next = current_two

        current_new.next = current_one or current_two

        return head_new.next

'''
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseList(head):
    curNode = head
    prevNode = None

    while curNode:
        prevNode, curNode.next, curNode = curNode, prevNode, curNode.next

    return prevNode


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

node1.next = node2
node2.next = node3
print("node1 value", node1.val)

linkedList2 = reverseList(node1)
print(linkedList2.val)

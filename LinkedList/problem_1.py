'''

10. Reverse Linked List (Logic) 
Note: In competitive coding, you often receive the head of the list, but for TCS NQT, you 
might have to build it from an array first. 
Problem: Reverse a singly linked list. 
• Input Format: 
1. An integer n. 
2. n integers representing the nodes. 
• Output Format: The reversed list. 
• Example: 
o Input: 
5 
1 2 3 4 5 
o Output: 5 4 3 2 1

'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def build_linked_list(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for value in values[1:]:
        current.next = Node(value)
        current = current.next
    return head


def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev


def print_linked_list(head):
    values = []
    current = head
    while current:
        values.append(str(current.data))
        current = current.next
    print(' '.join(values))


if __name__ == '__main__':
    n = int(input().strip())
    values = list(map(int, input().split())) if n > 0 else []
    head = build_linked_list(values)
    reversed_head = reverse_linked_list(head)
    print_linked_list(reversed_head)



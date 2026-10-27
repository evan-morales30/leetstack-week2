from typing import Iterable, Optional

class ListNode:
    def __init__(self, val: int, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, values: Iterable[int] = ()) -> None:
        self.head: Optional[ListNode] = None
        for value in values:
            self.append(value)

    def append(self, value: int) -> None:
        node = ListNode(value)
        if self.head is None:
            self.head = node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = node

    def to_list(self) -> list[int]:
        values = []
        current = self.head
        while current is not None:
            values.append(current.val)
            current = current.next
        return values

    def reverse(self) -> None:
        self.head = reverseList(self.head)



def reverseList(head):
    prev = None
    while head is not None:
        temp = head.next
        head.next = prev
        prev = head
        head = temp
    return prev



linked_list = LinkedList([1, 2, 3, 4, 5])
linked_list.reverse()
print("Lista invertida:", linked_list.to_list())
if linked_list.to_list() == [5, 4, 3, 2, 1]:
    print("Correcto!")
else:
    print("Incorrecto!")


empty_list = LinkedList()
empty_list.reverse()
print("Lista vacia:", empty_list.to_list())
if empty_list.to_list() == []:
    print("Correcto!")
else:
    print("Incorrecto!")


single_node_list = LinkedList([1])
single_node_list.reverse()
print("Lista de un solo nodo:", single_node_list.to_list())
if single_node_list.to_list() == [1]:
    print("Correcto!")
else:
    print("Incorrecto!")





class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    # Create a dummy node to act as the start of the merged list
    dummy = ListNode()
    tail = dummy

    # Traverse both lists while neither is empty
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    # Attach any remaining elements from either list
    tail.next = list1 if list1 else list2

    return dummy.next


def list_to_linked_list(values):
    dummy = ListNode()
    tail = dummy
    for value in values:
        tail.next = ListNode(value)
        tail = tail.next
    return dummy.next


def linked_list_to_list(node):
    values = []
    while node:
        values.append(node.val)
        node = node.next
    return values


def test_case(name, list1, list2, expected):
    result = mergeTwoLists(list_to_linked_list(list1), list_to_linked_list(list2))
    actual = linked_list_to_list(result)
    status = "correct" if actual == expected else "incorrect"
    print(f"{name}: {status}")


test_case("Case 1", [1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4])
test_case("Case 2", [], [0], [0])
test_case("Case 3", [5, 6, 7], [1, 2, 3], [1, 2, 3, 5, 6, 7])


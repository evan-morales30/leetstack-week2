class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorderList(head):
    if not head or not head.next:
        return

    # Step 1: Find the middle of the linked list
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse the second half of the list
    previous = None
    current = slow.next
    slow.next = None  # Cut the connection between first and second halves
    while current:
        nxt = current.next
        current.next = previous
        previous = current
        current = nxt

    # Step 3: Merge the two halves alternately
    first = head
    second = previous
    while second:
        temp1 = first.next
        temp2 = second.next
        first.next = second
        second.next = temp1
        first, second = temp1, temp2


def list_to_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


def linked_list_to_list(head):
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    return values


def test_case(name, values, expected):
    head = list_to_linked_list(values)
    reorderList(head)
    actual = linked_list_to_list(head)
    status = "correct" if actual == expected else "incorrect"
    print(f"{name}: {status}")


test_case("Case 1", [1, 2, 3, 4, 5, 6], [1, 6, 2, 5, 3, 4])
test_case("Case 2", [1, 2, 3, 4, 5], [1, 5, 2, 4, 3])
test_case("Case 3", [1], [1])
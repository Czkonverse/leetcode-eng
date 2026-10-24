"""
Test program for 2_add_two_numbers.py

Run with:  python LinkedList/test_2_add_two_numbers.py
"""

from importlib import util
from pathlib import Path

# Import the solution module by file path (filename starts with a digit,
# so a normal import statement won't work).
_module_path = Path(__file__).with_name("2_add_two_numbers.py")
_spec = util.spec_from_file_location("add_two_numbers", _module_path)
solution_module = util.module_from_spec(_spec)
_spec.loader.exec_module(solution_module)
ListNode = solution_module.ListNode
Solution = solution_module.Solution


def build_linked_list(values: list[int]) -> ListNode | None:
    """Build a linked list from a Python list (digits already reversed)."""
    dummy = ListNode(0)
    curr = dummy

    for value in values:
        curr.next = ListNode(value)
        curr = curr.next

    return dummy.next


def linked_list_to_list(head: ListNode | None) -> list[int]:
    """Convert a linked list back to a Python list."""
    values = []
    curr = head
    while curr:
        values.append(curr.val)
        curr = curr.next
    return values


def run_test(
    name: str, l1_vals: list[int], l2_vals: list[int], expected: list[int]
) -> bool:
    l1 = build_linked_list(l1_vals)
    l2 = build_linked_list(l2_vals)

    actual = linked_list_to_list(Solution().addTwoNumbers(l1, l2))

    ok = actual == expected
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] {name}")
    print(f"       l1       = {l1_vals}")
    print(f"       l2       = {l2_vals}")
    print(f"       expected = {expected}")
    print(f"       actual   = {actual}")
    print()
    return ok


def main() -> None:
    # Each case: (name, l1 digits reversed, l2 digits reversed, expected digits reversed)
    cases = [
        # 342 + 465 = 807
        ("Basic example", [2, 4, 3], [5, 6, 4], [7, 0, 8]),
        # 0 + 0 = 0
        ("Both zero", [0], [0], [0]),
        # 99 + 1 = 100  (tests carrying across digits)
        ("Carry to new digit", [9, 9], [1], [0, 0, 1]),
        # 5 + 5 = 10
        ("Single digit carry", [5], [5], [0, 1]),
        # Different lengths: 1 + 999 = 1000
        ("Different lengths", [1], [9, 9, 9], [0, 0, 0, 1]),
        # 9999999 + 9999 = 10009998
        ("Long numbers", [9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
        # 123 + 456 = 579 (no carries)
        ("No carry", [3, 2, 1], [6, 5, 4], [9, 7, 5]),
        # 0 + 123 = 123
        ("One zero operand", [0], [3, 2, 1], [3, 2, 1]),
    ]

    passed = 0
    for name, l1_vals, l2_vals, expected in cases:
        if run_test(name, l1_vals, l2_vals, expected):
            passed += 1

    total = len(cases)
    print("=" * 40)
    print(f"Result: {passed}/{total} tests passed")
    if passed != total:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

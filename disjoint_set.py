from collections import defaultdict

""" 
 Represent every node that belongs to a determinated set
 """
class Node:
    def __init__(self, element, memory_part):
        self.element = element
        self.memory_part = memory_part
        self.next = None

    
class Element:
    def __init__(headVal, tailVal):
        self.headVal = headVal
        self.tailVal = tailVal

    
class ListSet:
    def __init__(self):
        self.node_address = defaultdict(lambda: None)

    def make_set(self, elem):
        new_set = Element(Node(elem, None), None)
        new_set.headVal.memory_part = new_set
        new_set.tailVal = new_set.headVal
        self.node_address[elem] = new_set.headVal

    def find_element(elem, key):
        node = self.node_address[key]
        return node.memory_part

    def union_set(self, set_one, set_two):
        new_tail = set_two.headVal
        while new_tail:
            new_tail.memory_part = set_one
            new_tail = new_tail.next
        set_one.tailVal.next = set_two.headVal
        set_one.tailVal = set_two.tailVal
        del set_two


# https://www.geeksforgeeks.org/linked-list-representation-disjoint-set-data-structures/
def main():
    first_test = ListSet()
    first_test.make_set(12)
    first_test.make_set(4)
    first_test.make_set(22)

    print(f"find(13): {first_test.find_element(12)}")


if __name__ == "__main__":
    main()
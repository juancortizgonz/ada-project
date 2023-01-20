'''
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

    '''


from collections import defaultdict

class Node:
    def __init__(self, val, item_ptr):
        self.val = val
        self.item_ptr = item_ptr
        self.next = None

class Item:
    def __init__(self, hd, tl):
        self.hd = hd
        self.tl = tl

class ListSet:
    def __init__(self):
        self.node_address = defaultdict(lambda: None)

    def makeset(self, a):
        new_set = Item(Node(a, None), None)
        new_set.hd.item_ptr = new_set
        new_set.tl = new_set.hd
        self.node_address[a] = new_set.hd

    def find(self, key):
        node = self.node_address[key]
        return node.item_ptr

    def union(self, i1, i2):
        cur = i2.hd
        while cur:
            cur.item_ptr = i1
            cur = cur.next
        i1.tl.next = i2.hd
        i1.tl = i2.tl
        del i2

def execOperation(queryOpt, x, y=''):
    if y == '':
        return queryOpt == x
    else:
        if queryOpt == 1:
            print("Query 1")
        elif queryOpt == 2:
            print("Query 2")
        elif queryOpt == 3:
            print("Query 3")
        else:
            print("Query not defined")

def main():
    execOperation(3, 3)
    a = ListSet()
    a.makeset(13)
    a.makeset(25)
    a.makeset(45)
    a.makeset(65)

    print(f"find(13): {a.find(13)}")
    print(f"find(25): {a.find(25)}")
    print(f"find(65): {a.find(65)}")
    print(f"find(45): {a.find(45)}")
    print()
    print("Union(find(65), find(45))")
    a.union(a.find(65), a.find(45))
    print(f"find(65): {a.find(65)}")
    print(f"find(45): {a.find(45)}")

if __name__ == "__main__":
    main()

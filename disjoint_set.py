'''
 This is the first point project for ADA course from Universidad del Valle.
 @authors: Juan Camilo Ortiz Gonzalez - 2023921
           Paul Rojas - 
           Nicolas - 
 https://campusvirtual.univalle.edu.co/moodle/pluginfile.php/3959645/mod_resource/content/3/enunciado_proyecto_ada.pdf
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

    def execOperation(self, queryOpt, x, y="NoN"):
        if y != "NoN":
            if queryOpt == 1:
                if x <= y:
                    self.makeset(x)
                    self.makeset(y)
                    self.union(self.find(x), self.find(y))
                else:
                    print("Can't execute, invalid values for X and Y")
            elif queryOpt == 2:
                if x <= y:
                    self.makeset(x)
                    self.makeset(y)
                    for i in range(x+1, y):
                        self.makeset(i)
                        if i >= x+1:
                            self.union(self.find(i-1), self.find(i))
                else:
                    print("Can't execute, invalid values for X and Y")
            elif queryOpt == 3:
                self.makeset(x)
                self.makeset(y)
                first_elem = self.find(x)
                second_elem = self.find(y)
                return first_elem == second_elem
            else:
                print("Query not defined")
        else:
            return queryOpt == x

def main():
    path_input = input("Ingrese la ruta del archivo de entrada:")
    input_file = open(path_input, "r")
    output_file = open("output.txt", "w") # Change the name for creating a new file for each output, otherwise will be over-written
    
    total_input = input_file.readlines()
    print(total_input)
    converted_input = []
    output_list = []
    for i in range(0, len(total_input)):
        if i == 0:
            converted_input.append(total_input[i].replace("\n", "").split(" ", 1))
            print(converted_input[i])
        else:
            converted_input.append(total_input[i].replace("\n", "").split(" "))
            print(converted_input[i])
    print(converted_input)
    # print(converted_input)

    input_file.close() # Free up memory

    a = ListSet() # Initialize data structure

    # print(a.execOperation(3, 4, 5))
    for i in range(0, len(converted_input)):
        if i != 0:
            first_param = int(converted_input[i][0])
            second_param = int(converted_input[i][1])
            third_param = int(converted_input[i][2])
            result = a.execOperation(first_param, second_param, third_param)
            if type(result) == bool:
                output_list.append(str(result)+"\n")
            print(output_list)
    if len(output_list) > 0:
                output_file.writelines(output_list)

    # execOperation(3, 3)
    # a = ListSet()
    # a.makeset(5)
    # a.makeset(7)
    # a.union(a.find(1), a.find(5))
    # a.execOperation(2, 5, 7)
    # a.makeset(13)
    # a.makeset(25)
    # a.makeset(45)
    # a.makeset(65)

    """ print(f"find(13): {a.find(13)}")
    print(f"find(25): {a.find(25)}")
    print(f"find(65): {a.find(65)}")
    print(f"find(45): {a.find(45)}")
    print()
    print("Union(find(65), find(45))")
    a.union(a.find(65), a.find(45))
    print(f"find(65): {a.find(65)}")
    print(f"find(45): {a.find(45)}") """

if __name__ == "__main__":
    main()

import time
start = time.time()
'''
 Represents a Disjoint Set Union data structure
 @authors: Juan Camilo Ortiz
           Paul Rojas
           Nicolas Huertas
'''
class DisjointSet:
    parent = {}
 
    # Represents the depth of each tree
    rank = {}
 
    '''
    Generate a new set for each integer in the list (n sets, single element each one)
    Arguments:
        list_elements: list of integers
    Returns:
        None
    '''
    def makeset(self, list_elements):
        for i in list_elements:
            self.parent[i] = i
            self.rank[i] = 0 # Default depth
 
    '''
    Find the set where the keyVal belongs to
    Arguments:
        keyVal: integer
    Returns:
        integer (representative element of the set: <integer>)
    '''
    def find(self, keyVal):
        if self.parent[keyVal] != keyVal:
            # Using path compression (explained in Google Docs)
            self.parent[keyVal] = self.find(self.parent[keyVal])
        return self.parent[keyVal]
 
    '''
    Union from two subsets (all the set where a and b belongs) into a new one set
    Arguments:
        a: an integer
        b: an integer
    Returns:
        None
    '''
    def union(self, a, b):
        firstElem = self.find(a)
        secondElem = self.find(b)
        if firstElem == secondElem:
            print("Already in the same set")
            return
        
        # Attach the smaller depth tree within the another tree
        if self.rank[firstElem] > self.rank[secondElem]:
            self.parent[secondElem] = firstElem
        elif self.rank[firstElem] < self.rank[secondElem]:
            self.parent[firstElem] = secondElem
        else:
            self.parent[firstElem] = secondElem
            self.rank[secondElem] = self.rank[secondElem] + 1

    def checkExist(self, elem):
        try:
            return self.find(elem) != ''
        except:
            return False

    '''
    Executes the corresponding operation based on the query option. Operation handler.
    Arguments:
        queryOpt: an integer
        x: an integer
        y: an integer
    Returns:
        bool: if queryOpt == 3
        None: else
    '''
    def execOperation(self, queryOpt, x, y="NoN"):
        if y != "NoN":
            if queryOpt == 1:
                self.makeset([x, y])
                self.union(x, y)
            elif queryOpt == 2:
                list_of_elems = [elem for elem in range(x, y+1)]
                list_to_remove = []
                # depurar la lista para quitar los que ya existen
                for val in list_of_elems:
                    if self.checkExist(val):
                        list_of_elems.pop(list_of_elems.index(val))
                # print(list_of_elems)
                self.makeset(list_of_elems)
                for i in range(x, y):
                    self.union(i, i+1)
            elif queryOpt == 3:
                try:
                    result = self.find(x) == self.find(y)
                    return result
                except:
                    return False
            else:
                print("Invalid query option")
        else:
            return queryOpt == x
 
'''
Prints all the sets that exists actually - Aux function for testing purposes
Arguments:
    universe: an integer
    actual_set: an integer
Returns:
    None
'''
def printSets(universe, actual_set):
    print([actual_set.find(i) for i in universe])

time.sleep(1)
end = time.time()
print("Total execution time: ", end-start)
 
 
if __name__ == '__main__':

    path_input = input("Ingrese la ruta del archivo de entrada:")
    try:
        input_file = open(path_input, "r")
    except:
        print("No existe el archivo")
        exit()
    output_file = open("output.txt", "w") # Change the name for creating a new file for each output, otherwise will be over-written
    
    total_input = input_file.readlines()
    # print("Archivo inicial leido:", total_input)
    converted_input = []
    output_list = []
    for i in range(0, len(total_input)):
        if i == 0:
            converted_input.append(total_input[i].replace("\n", "").split(" ", 1))
            # print(converted_input[i])
        else:
            converted_input.append(total_input[i].replace("\n", "").split(" "))
            # print(converted_input[i])
    # print(converted_input)

    input_file.close() # Free up memory

    ds = DisjointSet() # Create new instance of the data structure
    '''
    for i in range(0, len(converted_input)):
        if i != 0:
            first_param = int(converted_input[i][0])
            second_param = int(converted_input[i][1])
            third_param = int(converted_input[i][2])
            print(converted_input[i][0], converted_input[i][1], converted_input[i][2])
            resultQuery = ds.execOperation(first_param, second_param, third_param)
            if first_param == 3:
                output_list.append(str(resultQuery)+"\n")
    if len(output_list) > 0:
        print(output_list)
        output_file.writelines(output_list)
    '''

    '''
    another = DisjointSet()
    print(another.execOperation(3, 2, 5))
    another.execOperation(1, 2, 5)
    print(another.execOperation(3, 2, 5))
    another.execOperation(2, 4, 7)
    another.execOperation(2, 1, 2)
    print(another.execOperation(3, 1, 7))
    print("--------------------------")
    '''



    # print(converted_input)
    for i in range (1, len(converted_input)):
        if int(converted_input[i][0]) == 3:
            resultOperation = ds.execOperation(int(converted_input[i][0]), int(converted_input[i][1]), int(converted_input[i][2]))
            output_list.append(str(resultOperation)+"\n")
        else:
            ds.execOperation(int(converted_input[i][0]), int(converted_input[i][1]), int(converted_input[i][2]))
    # print(output_list)
    output_file.writelines(output_list)

    '''
    ds = DisjointSet()
    ds.execOperation(1, 2, 3)
    print(ds.execOperation(3, 2, 4))
    '''

    # list_nueva = [elem for elem in range(0, 5)]
 
    '''
    # universe of items
    universe = [1, 2, 3, 4, 5]
 
    # initialize `DisjointSet` class
    ds = DisjointSet()
 
    # create a singleton set for each element of the universe
    ds.makeset(universe)
    print(ds.find(2))
    print(ds.find(3))
    ds.union(2, 3)
    printSets(universe, ds)
 
    ds.Union(4, 3)        # 4 and 3 are in the same set
    printSets(universe, ds)
 
    ds.Union(2, 1)        # 1 and 2 are in the same set
    printSets(universe, ds)
 
    ds.Union(1, 3)        # 1, 2, 3, 4 are in the same set
    printSets(universe, ds)
    '''
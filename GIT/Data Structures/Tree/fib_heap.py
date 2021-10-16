import math

class Node:
    
    def __init__(self, new_key, new_left=None, new_right=None, new_parent = None, new_child = None):
        self.key = new_key
        self.degree = 0
        self.parent = new_parent
        self.child = new_child
        self.left = new_left
        self.right = new_right
        self.mark = False

    def set_parent(self, new_parent):
        self.parent = new_parent
    
    def get_parent(self):
        return self.parent
    
    def add_child (self, new_child):
        
        if self.degree == 0:
            self.child = new_child
            

        elif self.degree == 1:
            self.child.set_right(new_child)
            self.child.set_left(new_child)
            new_child.set_right(self.child)
            new_child.set_left(self.child)
        else:
            self.child.right.set_left(new_child)
            new_child.set_right(self.child.right)

            self.child.set_right(new_child)
            new_child.set_left(self.child)
        
        new_child.set_parent(self)
        self.degree += 1
    
    def get_child(self):
        return self.child
    
    def set_left(self, new_left):
        self.left = new_left
    
    def get_left(self):
        return self.left
    
    def set_right(self, new_right):
        self.right = new_right
    
    def get_right(self):
        return self.right
    
    def set_degree(self, new_degree):
        self.degree = new_degree
    
    def get_degree(self):
        return self.degree

    def __str__(self):
        return str(self.key)
    
    def __lt__ (self, other):
        return self.key < other.key
    
class fib_heap:
    def __init__(self):
        self.node_count = 0
        self.root_count = 0
        self.min_heap = None
    
    def insert(self, new_node):
        if (self.min_heap == None):
            self.min_heap = new_node
        elif self.root_count == 1:
            self.min_heap.set_left(new_node)
            new_node.set_right(self.min_heap)
            
            self.min_heap.set_right(new_node)
            new_node.set_left(self.min_heap)

            if(new_node < self.min_heap):
                self.min_heap = new_node
        else:
            self.min_heap.right.set_left(new_node)
            new_node.set_right(self.min_heap.right)

            self.min_heap.set_right(new_node)
            new_node.set_left(self.min_heap)

            if(new_node < self.min_heap):
                self.min_heap = new_node

        self.root_count += 1
        self.node_count += 1



    def extract_min(self):
        min = self.min_heap
        
        
        if min.get_degree()== 0:
            self.min_heap.left.set_right(self.min_heap.get_right())
            self.min_heap.right.set_left(self.min_heap.get_left())
            self.min_heap = self.min_heap.get_left()
        elif min.get_degree() == 1:
            self.min_heap.child.set_parent(None)

            self.min_heap.left.set_right(self.min_heap.child)
            self.min_heap.child.set_left(self.min_heap.left)
            
            self.min_heap.right.set_left(self.min_heap.child)
            self.min_heap.child.set_right(self.min_heap.right)
        else:
            '''get child to root'''
            current = min.child
            for k in range (min.get_degree()):
                current.set_parent(None)
                current = current.left 
            self.min_heap.left.set_right(self.min_heap.child.right)
            self.min_heap.child.right.set_left(self.min_heap.left)

            self.min_heap.child.set_right(self.min_heap.right)
            self.min_heap.right.set_left(self.min_heap.child)
            
        self.min_heap = self.min_heap.left
        self.consolidate()

        self.node_count -= 1
        

        return min
    
    def consolidate(self):
        # create array 
        array = [None] * (math.ceil(math.log(self.node_count,2)) + 1)

        current, first = self.min_heap, self.min_heap
        done = False

        while not done:
            next = current.right
            while array[current.get_degree()] != None:
                node_1 = array[current.get_degree()]
                print("join", node_1, "and", current)
                if node_1 < current:
                    # current jadi anak node
                    self.remove_from_root(current)
                    node_1.add_child(current)
                    current = node_1
                else:
                    self.remove_from_root(node_1)
                    current.add_child(node_1)

                array[current.get_degree()] = None

            array[current.get_degree()] = current

            if next == first:
                done = True
            
            current = next
        
        self.root_count = 0
        done = False
        current, min = array[0], array[0]
        print(array[0], array[1])
        for i in range(len(array)):
            current = array[i]
            if current != None:
                if(current < min):
                    min = current
                self.root_count += 1
        
        self.min_heap = min



    def remove_from_root(self, node):
        node.left.right = node.right
        node.right.left = node.left

    def decrease_key(self, key):
        pass

a = fib_heap()
a.insert(Node(1))
a.insert(Node(2))
a.insert(Node(3))

current = a.min_heap
for j in range(a.root_count + 1):
    print(current, end= "->")
    current = current.right
print("\n-----")

a.min_heap.add_child(Node(9))
a.min_heap.add_child(Node(8))
a.min_heap.add_child(Node(7))

print("min:", a.extract_min())
print(a.root_count)


current = a.min_heap
for j in range(a.root_count+ 1):
    print(current, end= "->")
    current = current.right
print(current.child)
    
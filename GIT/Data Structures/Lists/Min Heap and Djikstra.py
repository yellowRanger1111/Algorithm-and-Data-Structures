'''
By : Owen 30039096
'''

from fib_heap import *


class MinHeap:
    '''
    class meanheap
    by: owen
    monash id : 30039096
    '''
    def __init__(self, size):
        '''
        this function initiates the class
        param           int
        return          None
        pre             None
        post            class mean heap have been created
        complexity      O(1)
        '''
        self.length = 0
        self.array = [0]*(size + 1)
        self.first = 1
        self.array[0] = [-10, -10]
        self.position = [0] * (size)

    def parent(self, pos):
        '''
        this function find the position of the parent
        param           int
        return          int
        pre             None
        post            None
        complexity      O(1)
        '''
        return pos//2
    
    def left_child(self, pos):
        '''
        this function find the left child position
        param           int
        return          int
        pre             None
        post            None
        complexity      O(1)
        '''
        return 2 * pos

    def right_child(self, pos):
        '''
        this function find the right child position
        param           int
        return          int
        pre             None
        post            None
        complexity      O(1)
        '''
        return (2 * pos) + 1
    
    def swap(self, pos1, pos2):
        '''
        this function will swap the element of 2 indexes
        param           int, int
        return          none
        pre             None
        post            position of the 2 item swaped
        complexity      O(1)
        '''
        self.array[pos1], self.array[pos2] = self.array[pos2], self.array[pos1]
        self.position[self.array[pos1][1]], self.position[self.array[pos2][1]] = self.position[self.array[pos2][1]], self.position[self.array[pos1][1]]
    

    def insert(self, thing):
        '''
        this function insert a thing into the mean heap and instantly sort them
        param           tuple
        return          none
        pre             None
        post            item inserted
        complexity      log n, where n is the length of the list
        '''
        #thing = (dist, vertex id)
        if(self.position[thing[1]] == 0):    
            if(self.length == len(self.array)):
                self.length += 1
                self.array.append(thing)
                self.position[thing[1]] = self.length
            else:
                self.length += 1
                self.array[self.length] = thing
                current = self.length
                self.position[thing[1]] = self.length
        
        else :
            self.array[self.position[thing[1]]] = thing
            current = self.position[thing[1]]


        
        while self.array[current][0] < self.array[self.parent(current)][0]:
            self.swap(current, self.parent(current)) 
            current = self.parent(current)


    def is_last(self, pos): 
        '''
        this function find if the node have a child
        param           int
        return          boolean
        pre             None
        post            None
        complexity      O(1)
        '''
        if pos >= (self.length//2) + 1 and pos <= self.length: 
            return True
        return False


    def pop_front(self):
        '''
        this function will delete the minimum item from the array then re sorted it
        param           none
        return          an element
        pre             None
        post            one item deleted
        complexity      log(n) where n is the total number of element in the array
        '''
        to_pop = self.array[self.first]
        self.array[self.first] = self.array[self.length]
        self.length -= 1
        if self.length> 0:
            self.heapify(self.first)
        self.position[to_pop[1]] = 0
        return to_pop


    def heapify(self, pos):
        '''
        this recursive function will sort the heap top down
        param           int
        return          None
        pre             None
        post            array sorted
        complexity      O(1)
        '''
        if not self.is_last(pos): 
            if (self.array[pos][0] > self.array[self.left_child(pos)][0]) or (self.array[pos][0] > self.array[self.right_child(pos)][0]): 
  
                if self.array[self.left_child(pos)][0] < self.array[self.right_child(pos)][0]: 
                    self.swap(pos, self.left_child(pos)) 
                    self.heapify(self.left_child(pos)) 
                else: 
                    self.swap(pos, self.right_child(pos)) 
                    self.heapify(self.right_child(pos)) 


    def __len__(self):
        '''
        this function return the length 
        param           none
        return          int
        pre             None
        post            None
        complexity      O(1)
        '''
        return self.length

def djikstra(start, gfile):
    '''
    this function find the distance from start to end using djikstra's algorithm
    '''
    now = read_file(gfile)
    
    graph = []
    for i in range(int(now[0][0])):
        graph.append([])

    #putting every egde in the grpah in the class
    for i in range(1, len(now)):
        graph[int(now[i][0])].append([int(now[i][1]), int(now[i][2])])
    
    #initiation
    pred = [None] * len(graph)
    dist = [9999] * len(graph)
    final = [0] * len(graph)
    
    #initiate staring points
    pred[start] = start
    dist[start] = 0
    final[start] = 1

    #pushing to the min heap
    priority_queue = MinHeap(len(graph))
    priority_queue.insert([0, start])

    while(len(priority_queue) != 0):
        next = priority_queue.pop_front()[1]
        for edges in graph[next]:
            if (edges[1] + dist[next]) < dist[edges[0]]:
                dist[edges[0]] = edges[1] + dist[next]
                pred[edges[0]] = next
                priority_queue.insert([edges[1] + dist[next], edges[0]])
    
    return dist, pred


def read_file(gfile):
    
    '''
    this function read a file and return the file in a list accordingly by rows
    '''
    file = open(gfile, "r")
    graph = []
    for row in file:
        graph.append((row.strip().split()))
    
    return graph


if __name__ == "__main__":
    file = open('output_adventure.txt', 'w+')
    file.write("I have done the fib heap implementation only\nHave an amazing day!")
    file.close
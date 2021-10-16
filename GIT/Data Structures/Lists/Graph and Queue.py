class Graph:
    '''
    class of Graph, using Adjencency List
    By : Owen Austin 
    Monash ID : 30039096
    '''
    def __init__(self, gfile):
        '''
        this function initiates the graph class from the file
        param           file name
        return          None
        pre             None
        post            a graph class have been made
        best cmplxity   O(e + v), where v is the total vertices in the graph and e is the number of edges in the graph   
        worst cmplxty   O(e + v), where v is the total vertices in the graph and e is the number of edges in the graph  
        '''
        #read file and put in the list
        now = self.read_file(gfile)
        # print(now)
             
        #initiate graph
        self.graph = []
        for i in range(int(now[0][0])):
            self.graph.append([])

        #putting every egde in the grpah in the class
        for i in range(1, len(now)):
            #int() = casting so all is saved in int not str
            #useful for next functions
            self.graph[int(now[i][0])].append([int(now[i][1]), int(now[i][2])])
        
        # print (self.graph)
        
    def read_file(self, gfile):
        '''
        this function read a file and return the file in a list accordingly by rows
        param           file name
        return          a list
        pre             None
        post            None
        best cmplxity   O(r), where r is the total row in the file 
        worst cmplxty   O(r), where r is the total row in the file
        '''
        file = open(gfile, "r")
        graph = []
        for row in file:
            graph.append((row.strip().split()))
        
        return graph

    def shallowest_spanning_tree(self):
        '''
        this function find the lowest spanning tree
        param           None
        return          Int, int 
        pre             None
        post            None
        best cmplxity   O(v3), where v is the number of vertices in the graph
        worst cmplxty   O(v3), where v is the number of vertices in the graph
        '''
        min, vertex = 9999, 0

        for vertices in range(len(self.graph)):
            result = self.bfs(vertices)
            if ( result < min):
                min = result
                vertex = vertices
        
        return(vertex, min)

    def bfs(self, vertex):
        '''
        this function find the max depth from the vertex
        param           int
        return          int
        pre             None
        post            None
        best cmplxity   O(v2), where v is the number of vertices in the graph
        worst cmplxty   O(v2), where v is the number of vertices in the graph
        '''  
        #create visiting classes
        visited = [0] * len(self.graph)
        visited[vertex] = 1

        #queue = [vertex]
        # print('visited = ', visited)
        queue = Queue(len(self.graph))
        queue.append(vertex)
        # print(queue.array)
        
        while len(queue) != 0:
            for edges in self.graph[queue[0]]:
                if visited[edges[0]] == 0:
                    visited[edges[0]] = visited[queue[0]] + 1
                    queue.append(edges[0])    
            
            queue.pop_front()
            # print("queue = ", queue)
            # print("visited = ", visited)

        # print (visited)
        return (max(visited)-1)

    def shortest_errand(self, home, destination, ice_locs, ice_cream_locs):
        '''
        this function find the shortest route from home to destination through ice locs and ice cream locs
        param           int, int, list, list
        return          Int, list 
        pre             None
        post            None
        best cmplxity   O(ve log v), where v is the number of vertices in the graph and e is the number of edges in the graph
        worst cmplxty   O(ve log v), where v is the number of vertices in the graph and e is the number of edges in the graph
        '''
        home_to_ices, pred_home_to_ice = self.djikstra(home)
        des_to_ice_cream, pred_des_to_i_cream = self.djikstra(destination)

        min = 9999
        walk = []

        for ices in ice_locs:
            #djikstra for ices
            ices_dist, ices_pred = self.djikstra(ices)
            for ice_creams in ice_cream_locs:
                if( (home_to_ices[ices] + ices_dist[ice_creams] + des_to_ice_cream[ice_creams]) < min):
                    min = (home_to_ices[ices] + ices_dist[ice_creams] + des_to_ice_cream[ice_creams])
                    walk = [ice_creams]
                    
                    #find walks
                    while walk[-1] != destination:
                        walk.append(pred_des_to_i_cream[walk[-1]])
                    walk = walk[::-1]
                    while walk[-1] != ices:
                        walk.append(ices_pred[walk[-1]])
                    while walk[-1] != home:
                        walk.append(pred_home_to_ice[walk[-1]])
                    walk = walk[::-1]
        
        return (min, walk)

    def djikstra(self, start):
        '''
        this function find the distance from start to end using djikstra's algorithm
        param           int, int
        return          Int, list 
        pre             None
        post            None
        best cmplxity   O(e log v), where v is the number of vertices in the graph and e is the number of edges in the graph
        worst cmplxty   O(e log v), where v is the number of vertices in the graph and e is the number of edges in the graph
        '''
        #initiation
        pred = [None] * len(self.graph)
        dist = [9999] * len(self.graph)
        final = [0] * len(self.graph)
        
        #initiate staring points
        pred[start] = start
        dist[start] = 0
        final[start] = 1

        #pushing to the min heap
        priority_queue = MinHeap(len(self.graph))
        priority_queue.insert([0, start])

        while(len(priority_queue) != 0):
            next = priority_queue.pop_front()[1]
            for edges in self.graph[next]:
                if (edges[1] + dist[next]) < dist[edges[0]]:
                    dist[edges[0]] = edges[1] + dist[next]
                    pred[edges[0]] = next
                    priority_queue.insert([edges[1] + dist[next], edges[0]])
        
        return dist, pred
            
    def pretty_print(self):
        '''
        this function print the graph neatly
        param           none
        return          none 
        pre             None
        post            None
        best cmplxity   O(e), where e is the number of edges in the graph
        worst cmplxty   O(e), where e is the number of edges in the graph
        '''
        for vertex in range(len(self.graph)):
            print(vertex ,end= " : ")
            for edges in self.graph[vertex]:
                print(edges, end= " ")
            print ('')



class Queue:
    '''
    class queue
    by : Owen Austin
    monash id : 30039096
    '''
    def __init__(self, size):
        '''
        this function initiates the class
        param           int
        return          None
        pre             None
        post            class queue have been created
        complexity      O(1)
        '''
        self.array = [None] * size
        self.length = 0
        self.start = 0 
    
    def __len__ (self):
        '''
        this function will return the length of the queue
        param           None
        return          int
        pre             None
        post            None
        best cmplxity   O(1)
        worst cmplxty   O(1)
        '''
        return self.length
    
    def append(self, thing):
        '''
        this function will add an item to the back of the queue
        param           Item
        return          none
        pre             None
        post            Queue len added by 1
        best cmplxity   O(1)
        worst cmplxty   O(1)
        '''
        if(self.is_full()):
            self.array.append(thing)
        
        else:
            self.array[self.start + self.length] = thing
            self.length += 1
            
    
    def pop_front (self):
        '''
        this function will pop the first item in the queu
        param           None
        return          none
        pre             None
        post            an item in the front of the queue deleted
        best cmplxity   O(1)
        worst cmplxty   O(1)
        '''
        if not self.is_empty():
            self.length -= 1
            self.start += 1
        else :
            print("nothing to pop")

    def __getitem__ (self, index):
        '''
        this function will get an item of a certain index
        param           None
        return          Item in that index
        pre             None
        post            None
        best cmplxity   O(1)
        worst cmplxty   O(1)
        '''
        if not self.is_empty():
            try:
                return self.array[index + self.start]
            except IndexError:
                print("out of range")
        else:
            print("Queue is empty") 

    def is_full(self):
        '''
        this function will tell wether the list is full or not
        param           None
        return          Boolean
        pre             None
        post            None
        best cmplxity   O(1)
        worst cmplxty   O(1)
        '''
        return self.length + self.start == len(self.array)
    
    def is_empty(self):
        '''
        this function will tell wether the list is empty or not
        param           None
        return          Boolean
        pre             None
        post            None
        best cmplxity   O(1)
        worst cmplxty   O(1)
        '''
        return self.length == 0


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



now = Graph("test3.txt")
print(now.shallowest_spanning_tree())
print(now.shortest_errand(0, 8, [1,5,8], [4,6]))

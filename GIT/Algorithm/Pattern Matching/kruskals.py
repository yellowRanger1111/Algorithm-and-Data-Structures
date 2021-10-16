'''
By : Owen 30039096
'''

import sys

class Node:
    def __init__(self, new_id):
        self.size = 1
        self.point = None
        self.id = new_id
    
    def get_id(self):
        return self.id
    
    def set_id(self, new_id):
        self.id = new_id
    
    def inc_size(self, a:int):
        self.size += a
    
    def get_size(self):
        return -self.size

    def set_point(self, new_point):
        self.point = new_point
    
    def get_point(self):
        if self.point == None:
            return self.id
        else:
            #self.point.get_point()
            return self.point.get_point()

def take_weight(k):
    return k[2]

def sort (edge_array):
    # u v weight
    return sorted(edge_array, key=take_weight)

def kruskal (verti, edge_array):
    #create vertices nodes
    vertices = []
    for i in range(verti):
        vertices.append(Node(i))

    edges_used = []
    total_weight = 0

    # for vertex in vertices:
    #     print(vertex.get_point(), end= ",")
    # print("")

    for u,v,w in edge_array:
        #contains id
        root_a = vertices[u].get_point()
        root_b = vertices[v].get_point()

        # print("-----")
        # print(u,v, w)
        # print(root_a)
        # print(root_b)
        

        if(root_a != root_b):
            #join u and v
            if(vertices[root_a].get_size() < vertices[root_b].get_size()):
                # join u to v
                vertices[root_a].set_point(vertices[root_b])
                vertices[root_b].inc_size(vertices[root_a].get_size())
                edges_used.append((u,v,w))
                total_weight+= w
            else:
                #join v to u
                vertices[root_b].set_point(vertices[root_a])
                vertices[root_a].inc_size(vertices[root_b].get_size())
                edges_used.append((u,v,w))
                total_weight+= w
        '''
        for vertex in vertices:
            print(vertex.get_point(), end= ",")
        print("")
        '''
    return total_weight, edges_used


def readFiles(pfn):
    patFile = open(pfn, "r")
    graph = []
    for row in patFile:
        graph.append((row.strip().split()))
    
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            graph[i][j] = int(graph[i][j])
    return graph

def writeFile (max, data, fn):
    file = open(fn, 'w+')
    file.write(max)
    file.write("\n")
    for lines in data:
        file.write(str(lines[0]))
        file.write(" ")
        file.write(str(lines[1]))
        file.write(" ")
        file.write(str(lines[2]))
        file.write("\n")        
    file.close()
    


if __name__ == "__main__":
    vert = sys.argv[1]
    file2Name = sys.argv[2]

    string2 = readFiles(file2Name)
    #print(string2)
    
    max, data = kruskal(int(vert), sort(string2))
    
    writeFile(str(max), data,'output_kruskals.txt')


# g = [[0,1,5],
#     [1, 2 ,4],
#     [2, 3 ,2],
#     [3, 4 ,10],
#     [4, 5 ,6],
#     [5, 0 ,1],
#     [0, 6 ,8],
#     [1, 6 ,2],
#     [2, 6 ,1],
#     [3, 6 ,3],
#     [4, 6 ,7],
#     [5, 6 ,4]]

# w, eu = kruskal(7, sort(g))
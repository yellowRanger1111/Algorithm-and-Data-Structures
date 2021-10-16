def change_letter(letter):
    '''changes letter to index to put in suffix tree'''
    if(letter == "$"):
        return 0
    return ord(letter)-96

class Node:
    '''includes start, end, link, child, is_leaf'''
    string = ""

    def __init__(self, new_start, new_end):
        self.start = new_start
        self.end = new_end
        self.child = [None]*27
        self.link = None
        self.leaf = True

    def set_string(self, new_string):
        Node.string = new_string
    
    def split(self, split_at):
        new_child = Node(split_at + self.start, self.end)
        self.end = Ending(self.start + split_at)

        #transfer child 
        new_child.child = self.child
        self.child = [None] * 26

        #transfer link
        new_child.link = self.link
        self.link = None

        #add new child to self
        self.add_child(new_child)
    
    def __str__(self):
        return Node.string[self.start: self.end.get_num()]
    
    def get_first_letter(self):
        return Node.string[self.start]
    
    def add_child(self, new_node):
        self.child[change_letter(str(new_node)[0])] = new_node
        self.leaf = False
    
    def is_leaf(self):
        if self.leaf :
            """re check once and for all"""
            for child in self.child:
                if child != None:
                    self.leaf = False
        return self.leaf
    
    def create_link (self, new_link):
        self.link = new_link

    def get_link(self):
        return self.link
    
    def find_child(self, first_letter):
        return self.child[change_letter(first_letter)]

    def print_labels (self, depth=0):
        print("-"*depth , self)
        #print("-"*depth , self, "l:", self.link)
        for child in self.child:
            if(child != None):
                child.print_labels(depth+1)
    
    def get_elem_in_order(self):
        return_array = []
        for child in self.child:
            if child != None:
                child._get_elem_in_order_aux("", return_array)
        return return_array
        
    def _get_elem_in_order_aux(self, prefix, return_array):
        if self.is_leaf():
            return_array.append(prefix + str(self))
        else:
            for child in self.child:
                if child != None:
                    child._get_elem_in_order_aux(prefix + str(self), return_array)


class Ending:
    def __init__(self, new_num):
        self.num = new_num
    
    def inc(self):
        self.num += 1
    
    def get_num(self):
        return self.num

    def __str__(self):
        return str(self.num)


def ukkonnen (string):
    #initialize tree
    root = Node(0, Ending(0))
    root.create_link(root)
    root.set_string(string)

    #initial global variables
    global_end = Ending(1)
    remainder = ""
    last_j = 0

    #creating the first child
    if(string != ""):
        root.add_child(Node(0, global_end))

    active_node = root

    for i in range(1, len(string)):
        #case 1
    
        global_end.inc()
        j = last_j + 1

        last_node = None
        done_2 = False

        

        while j < i+1 and not done_2:
            #code under is for debugging purposes 
            '''
            print("= = = = = = = = =")
            print(string)
            print("an:", active_node)
            print('s now:', string[j:i+1])
            print("r:",remainder)
            '''
            #keeping track for the actual place in string
            k = j + len(remainder) + len(str(active_node))
            l = len(remainder)

            
                
            if len(remainder)== 0 and active_node.find_child(string[j]) == None:
                '''
                base case 2
                print("c2b")
                '''

                active_node.add_child(Node(k, global_end))
                
                if(last_node != None):
                    last_node.create_link(active_node)

                last_node = None
                active_node = active_node.get_link()
                done_2 = True
                last_j += 1
                remainder = ""
        
            else:
                # finding the first label
                if(len(remainder)> 0):
                    current_node = active_node.find_child(remainder[0])
                    p = len(str(current_node))
                    
                    while p < len(remainder) :

                        active_node = current_node
                        current_node = active_node.find_child(remainder[p])
                        p += len(str(current_node))
                        l -= len(str(active_node))

                        remainder = remainder[len(str(active_node)):]
                        
                else:
                    current_node = active_node.find_child(string[k])
                
                done = False

                while not done:
                    if (k > i):
                        '''
                        case 3
                        code below is for debugging only
                        print("c3")
                        '''

                        remainder += string[i]
                        done = True
                        done_2 = True

                        if(last_node != None):
                            last_node.create_link(active_node)
                            last_node = None

                    elif (l >= len(str(current_node))):
                        #not enough get node again
                        if(current_node.find_child(string[k]) == None):
                            '''
                            rule 2 end
                            code under is for debugging purposes
                            print("c2e")
                            '''
                            
                            current_node.add_child(Node(k, global_end))
                            last_j += 1
                            done = True

                            if(last_node != None):
                                last_node.create_link(current_node)
                                
                            if(active_node == root):
                                remainder = remainder[1:]
                            
                            last_node = None
                            active_node = active_node.get_link()


                        else:
                            #getting code
                            new_child = current_node.find_child(string[k])
                            
                            active_node = current_node
                            current_node = new_child
                            remainder = ''
                            l = 0
                    
                    elif string[k] != str(current_node)[l]:
                        '''
                        splitting the branch
                        code under is debugging purposes
                        print("c2s")
                        '''
                        current_node.split(l)
                        current_node.add_child(Node(k, global_end))
                        
                        if(last_node != None):
                            last_node.create_link(current_node)

                        if(active_node == root):
                            remainder = remainder[1:]

                        last_node = current_node
                        active_node = active_node.get_link()
                        last_j += 1
                        done = True
                    
                    else:
                        k+=1
                        l+=1

            # root.print_labels()
            j += 1

    return root



                





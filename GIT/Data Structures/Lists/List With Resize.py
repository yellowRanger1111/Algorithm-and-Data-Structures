import math
class ListADT:
    def __init__(self, size = 40):
        """
        this function initialize the class List Adt
        param          the new class defined and size of the list
        return         none
        pre            none
        post           a list class have been created
        complexity     best and worst case: O(1)
        """
        if (size < 40):
            size = 40
        
        self.the_array = [None]*size
        self.length = 0

    def __str__(self):
        """
        this function returns string of the array
        param          the list class
        return         string of the list
        pre            none
        post           the string of the list will be forwarded
        complexity     best and worst case: O(n), where n = size of list
        """
        string_return = ""
        for index in range(self.length):
            string_return += str(self.the_array[index])
            string_return +="\n"
    
        return string_return

    def __len__ (self):
        """
        this function returns the length of the array
        param          the list class
        return         length
        pre            none
        post           the length returned
        complexity     best and worst case: O(1)
        """
        return self.length
    
    def __getitem__ (self, index):
        """
        this function will return the item 
        param          the list class, index of item wanted to be returned
        return         the item in the index of index
        pre            none
        post           item returned
        complexity     best and worst case: O(1)
        """
        if (index < 0):
            index = self.length + index
            if (index < 0):
                raise IndexError ("Index Out Of Range")
            else:
                return self.the_array[index]
        elif(index > self.length):
            raise IndexError ("Index over than length")
        else:
            return self.the_array[index]
            
    def __setitem__ (self, index, item):
        """
        this function will put an item into the list 
        param          the list class, index and the item to be placed
        return         none
        pre            none
        post           item is initialize
        complexity     best and worst case: O(1)
        """
        if (index < 0):
            index = self.length + index
            if(index < 0):
                raise IndexError ("Index Out Of Range")
            else:
                self.the_array[index] = item
    
        elif(index > self.length):
            raise IndexError ("Index over than length")
        else:
            self.the_array[index] = item



    def __eq__(self, other):
        """
        this function will test if the two list is equivalent
        param          the list class, the thing wanted to be compared with
        return         true or false (equivalent or not)
        pre            none
        post           none
        complexity     best and worst case: O(mn), where m is the length of self list 
                       and n is the length of other
        """
        return str(self)==str(other)


    def insert(self, index, item):
        """
        this function will insert item into the list 
        param          the list class, index and the item to be placed
        return         none
        pre            none
        post           item is initialize into the array
        complexity     best and worst case: O(n), n is equal to the length of the array 
                        minus the index required
        """
        if self.is_empty():
            self.append(item)
        elif self.is_full():
            print("List is full")
        elif(index < 0):
            index = self.length + index + 1
            if (index < 0):
                raise IndexError("Index Out Of Range")
            else:
                for i in range(self.length - index):
                    self.the_array[self.length - i] = self.the_array[self.length - i -1]
                self.the_array[index] = item
                self.length += 1
                
        elif(index > self.length):
            raise IndexError ("Index over than length")
        else:
            for i in range(self.length - index):
                self.the_array[self.length - i] = self.the_array[self.length - i -1]
            self.the_array[index] = item
            self.length += 1
        
        self.resize()
            
    
    def delete(self, index):
        """
        this function will delete an item 
        param          the list class, index where the item wanted to be deleted
        return         none
        pre            none
        post           item is deletd in the array
        complexity     best and worst case: O(n), n is equal to the length of the array 
                        minus the index required
        """
        if self.is_empty():
            print("List is empty")
        elif(index < 0):
            index = self.length + index
            if (index < 0):
                raise IndexError ("Index out of range")
            else:
                for i in range(self.length - index - 1):
                    self.the_array[index + i] = self.the_array[index + i + 1]
                self.length -= 1
                self.the_array[self.length] = None        
        elif(index > self.length):
            raise IndexError ("Index over than length")
        else:
            for i in range(self.length - index - 1):
                self.the_array[index + i] = self.the_array[index + i + 1]
            self.length -= 1
            self.the_array[self.length] = None
        
        self.resize()


    def resize(self):
        """
        this function will resize the list
        param          the list class
        return         none
        pre            none
        post           the array resize
        complexity     best case: O(1) where list is not 1/4 and not full
                       worst case: O(n), n is equal to the length of the array 
        """
        if (self.length <= len(self.the_array)//4 ):
            #resize smaller
            size = len(self.the_array)//2
            if not (size < 40):
            
                temp = []
                for i in range( self.length):
                    temp.append(self.the_array[i])
      
                #re initialize
                self.the_array = [None] * size
                self.length = 0

                for i in range(len(temp)):
                    self.append(temp[i])

        elif(self.is_full()):
            #resize bigger
            temp = []
            for i in range( self.length):
                temp.append(self.the_array[i])

            size = math.ceil(len(self.the_array)*1.9) 
            #re initialize
            self.the_array = [None] * size
            self.length = 0

            for i in range(len(temp)):
                self.append(temp[i])        

    def is_empty(self):
        return self.length == 0

    def is_full(self):
        return self.length == len(self.the_array)

    def __contains__(self, item):
        for i in range(self.length):
            if item == self.the_array[i]:
                return True
        return False
 
    def append(self, item):
        if not self.is_full():
            self.the_array[self.length] = item
            self.length +=1
        else:
            raise Exception('List if Full')

    def unsafe_set_array(self,array,length):
        """
        UNSAFE: only to be used during testing to facilitate it!! DO NOT USE FOR ANYTHING ELSE
        """
        if 'test' not in __name__:
            raise Exception('Not runnable')
			
        self.the_array = array
        self.length = length

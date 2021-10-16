class HashTable:
    def __init__(self, table_capacity = 10, hash_base = 7): 
        '''
        this function initialize the class
        param           table capacity and hash base
        return          none
        pre             none
        post            a new hash table have been created
        best cmplxity   O(1)
        worst cmplxty   O(1)   
        '''
        self.table = [None] * table_capacity
        self.base = hash_base
        self.count = 0
  
    def __getitem__(self, key):
        '''
        this function will return the item if there is any
        param           the key
        return          item if there is
        pre             none
        post            item returned or KeyError raised
        best cmplxity   O(1)
        worst cmplxty   O(n), where n is equal to the len of the list
        '''
        #linear probing
        i = 0

        while(self.table[self.hash(key) + i] != None):
            
            if(self.table[self.hash(key) + i][0] == key):
                return self.table[self.hash(key) + i][1]
            i += 1

            if((self.hash(key) + i) >= len(self.table)):
                i -= len(self.table)
            elif(i == 0):
                raise KeyError
            
        raise KeyError

    def __setitem__(self, key, item):
        '''
        this function will set the item with a certain key to the hash table
        param           the key and item wanted to be saved
        return          none
        pre             none
        post            item saved
        best cmplxity   O(1)
        worst cmplxty   O(nm), where n is equal to the number of collision and m is the length of rehash function if called
        '''
        #linear probing
        i = 0
        while(self.table[self.hash(key) + i ] != None):
            
            
            if(self.table[self.hash(key) + i ][0] == key):
                self.table[self.hash(key) + i][1] = item
                break
            
            i+=1
            if((self.hash(key) + i) >= len(self.table)):
                i -= len(self.table)
            elif(i == 0):
                self.rehash()
                         
        if (self.table[self.hash(key) + i ] == None):
            self.table[self.hash(key) + i] = [key, item]
            self.count += 1

    def __contains__(self, key):
        '''
        this function will return true if there exist such item and key
        param           the key and item wanted to be found
        return          true or false
        pre             none
        post            none
        best cmplxity   O(1)
        worst cmplxty   O(n), where n is equal to the length of the list
        '''
        #linear probing
        i = 0
        while(self.table[self.hash(key) + i] != None):
            if(self.table[self.hash(key) + i][0] == key):
                return True
            i += 1
        return False

    def hash(self, key):
        '''
        this function will return the hashing index of the key
        param           the key
        return          a number
        pre             none
        post            none
        best cmplxity   O(n), where n is equal to the length of the key
        worst cmplxty   O(n), where n is equal to the length of the key
        '''
        key = str(key)
        value = 0
        for i in range(len(key)):
            value = (value * self.base + ord(key[i])) % len(self.table)
        return value


    def rehash(self):
        '''
        this function will rehash the table
        param           the class
        return          none
        pre             none
        post            table is rehashed
        best cmplxity   O(mn), where m is the number of primes number skipped
                        n is equal to the number of item in hash table
        worst cmplxty   O(mn), where m is the number of primes number skipped
                        n is equal to the number of item in hash table   
        '''
        length_now = len(self.table)
        Primes = [ 3, 7, 11, 17, 23, 29, 37, 47, 59, 71, 89, 107, 131, 
        163, 197, 239, 293, 353, 431, 521, 631, 761, 919, 1103, 1327, 
        1597, 1931, 2333, 2801, 3371, 4049, 4861, 5839, 7013, 8419, 10103, 
        12143, 14591, 17519, 21023, 25229, 30313, 36353, 43627, 52361, 62851, 
        75521, 90523, 108631, 130363, 156437, 187751, 225307, 270371, 324449,
        389357, 467237, 560689, 672827, 807403, 968897, 1162687, 1395263, 1674319, 
        2009191, 2411033, 2893249, 3471899, 4166287, 4999559, 5999471, 7199369] 

        for i in Primes:
            if i > (length_now*2):
                new_table = [None] * i
                break
        
        for tupl in self.table:
            if tupl != None:
                i = 0
                while(new_table[self.hash(tupl[0]) + i ] != None):
            
                    if(new_table[self.hash(tupl[0]) + i ][0] == tupl[0]):
                        new_table[self.hash(tupl[0]) + i ][1] = tupl[1]
                        break
                    
                    i+=1
                    if((self.hash(tupl[0]) + i) >= len(new_table)):
                        i -= len(new_table)
                    elif(i == 0):
                        self.rehash()
                                
                if (new_table[self.hash(tupl[0]) + i ] == None):
                    new_table[self.hash(tupl[0]) + i ] = tupl
        

        self.table = []
        for tupl in new_table:
            self.table.append(tupl)

if __name__ == '__main__':
    a = HashTable(5,3)
    a["word"] = 1
    a["word"] = 2
    a['a'] = 1
    a['b'] = 2
    a['c'] =3
    a['d'] = 4
    a['f'] = 5
    print(a.table)

        
          

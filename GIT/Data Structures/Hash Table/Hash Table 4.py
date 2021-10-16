import timeit
import bst

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
        self.rehash_count = 0
        self.probe_total = 0
        self.probe_max = 0
        self.collision_count = 0
  
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

        if (self.table[self.hash(key)] ==None ):
            raise KeyError

        return self.table[self.hash(key)][key]

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
        if self.table[self.hash(key)] == None:
            self.table[self.hash(key)] = bst.BinarySearchTree()
        
        self.table[self.hash(key)][key] = item

        self.probe_total += len(self.table[self.hash(key)]) - 1
        if(len(self.table[self.hash(key)]) - 1 > self.probe_max):
            self.probe_max = len(self.table[self.hash(key)]) - 1
        if(len(self.table[self.hash(key)])> 1):
            self.collision_count += 1
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
        if (self.table[self.hash(key)] == None ):
            return False

        if(key in self.table[self.hash(key)]):
            return True
        else:
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

    def statistics(self):
        '''
        this function will return the statistic of the class
        param           the class
        return          collision count, probe total, probe max, rehash count
        pre             none
        post            none
        best cmplxity   O(1)
        worst cmplxty   O(1)
        '''
        return(self.collision_count, self.probe_total, self.probe_max, self.rehash_count)

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
                if(new_table[self.hash(tupl[0])] == None):
                    new_table[self.hash(tupl[0])] = bst.BinarySearchTree()
                                
                new_table[self.hash(tupl[0])][tupl[0]] = tupl
        

        self.table = []
        for tupl in new_table:
            self.table.append(tupl)

        self.rehash_count += 1

    def load_dictionary_statistics(self, hash_base, table_size, filename, max_time=None):
        '''
        this function will insert the words in the text to the table until the time limit
        param           hash_base, table sixe, filename and max time
        return          word inserted, time used, collision count, probe total, probe max, rehash count
        pre             none
        post            table is filled with words
        best cmplxity   O(mn), where m is the number of words in the file and n is the max time 
        worst cmplxty   O(mn), where m is the number of words in the file and n is the max time
        '''
        try:
            self.table = [None] * table_size
            self.base = hash_base
            self.count = 0
            self.rehash_count = 0
            self.probe_total = 0
            self.probe_max = 0
            self.collision_count = 0
            
            timer = timeit.default_timer()
            
            file_now = open(filename, 'r')
            
            for line in file_now:
                self[line] = 1
                
                if not (max_time == None):
                    time_now = timeit.default_timer()
                    if (time_now - timer)  > max_time:
                        raise TimeoutError

            end_timer = timeit.default_timer()

        except TimeoutError:
            file_now.close()
            return[self.count, None, self.collision_count, self.probe_total, self.probe_max, self.rehash_count]
        else:
            file_now.close()
            return [self.count, (end_timer-timer) , self.collision_count, self.probe_total, self.probe_max, self.rehash_count]

def table_load_dictionary_statistics(max_time):
    output = open('output5.csv', 'w')
    hash_table = HashTable()
    for word_lines in ['english_small.txt', 'english_large.txt', 'french.txt']:
        for b in [1, 27183, 250726]:
            for table_size in [250727, 402221, 1000081]:
                result = hash_table.load_dictionary_statistics(b,table_size, word_lines, max_time)
                if(result[1]== None):
                    result[1] = 'TIMEOUT'
                output.write(f'{word_lines},{table_size},{b},{result[0]},{result[1]},{result[2]},{result[3]},{result[4]},{result[5]}\n')
                print(result)
    output.close()
        
if __name__ == '__main__':
    table_load_dictionary_statistics(15)
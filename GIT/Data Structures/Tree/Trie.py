'''
Author = Owen Austin Oei
17/05/2020
'''
# ENABLE_COMPLEXITY_TEST = True
class Trie:
    '''
    class of trie 
    function = store words
    '''
    #ord a = 97
    def __init__(self, text):
        '''
        this function will initiaize the class and fill with all word in text
        param           list of words
        return          none
        pre             none
        post            a trie class have been made
        best cmplxity   O(n), where n is the total letters in the list 
        worst cmplxty   O(n), where n is the total letters in the list  
        '''
        self.trie_array = [0] * 28
        for i in text:
            self.insert(i)
        
    
    def insert(self, string):
        '''
        this function will insert a word to the object
        param           a word
        return          none
        pre             none
        post            a word added
        best cmplxity   O(n), where n is the total letters in the word
        worst cmplxty   O(n), where n is the total letters in the word  
        '''
        now = self.trie_array
        for l in range(len(string)):
            now[1] += 1
            if (now[ord(string[l])-95] == 0):
                now[ord(string[l])-95] = [0]*28
            now = now[ord(string[l])-95]
        now[1] += 1
        now[0] += 1

    def string_freq(self, query_str):
        '''
        this function will return how many times is that string inserted
        param           a word
        return          an int
        pre             none
        post            none
        best cmplxity   O(n), where n is the total letters in class peceding the query, 
                        for ex : the class is empty (or whenever n < total length of query str)
        worst cmplxty   O(t), where t is the total letters in the query str 
        '''
        now = self.trie_array
        for l in range(len(query_str)):
            if (now[ord(query_str[l])-95] == 0):
                return 0
            now = now[ord(query_str[l])-95] 
        return now[0]

    def prefix_freq(self, query_str):
        '''
        this function will return how many times the string with that prefix inserted
        param           a word
        return          an int
        pre             none
        post            none
        best cmplxity   O(n), where n is the total letters in class peceding the query, 
                        for ex : the class is empty (or whenever n < total length of query str)
        worst cmplxty   O(t), where t is the total letters in the query str 
        '''
        now = self.trie_array
        for l in range(len(query_str)):
            if (now[ord(query_str[l])-95] == 0):
                return 0
            now = now[ord(query_str[l])-95] 
        return now[1]


    def wildcard_prefix_freq(self, query_str):
        '''
        this function will return how many times the string with that prefix inserted
        param           a word
        return          an int
        pre             none
        post            none
        best cmplxity   O(n), where n is the total letters in class peceding the query, 
                        for ex : the class is empty (or whenever n < total length of query str)
        worst cmplxty   O(t + f), where t is the total letters in the query str, 
                        f is the number of letters that needed to be return 
        '''
        result = []
        self.wildcard_check(self.trie_array, query_str, result, "")
        return result

    def wildcard_check(self, now, query_str, result, pref):
        '''
        this recursive function will keep going until the query is fulfilled. 
        when the list is empty to that part o fthe query, break immediately.
        param           a word
        return          an int
        pre             none
        post            none
        best cmplxity   O(n), where n is the total letters in class peceding the query, 
                        for ex : the class is empty (or whenever n < total length of query str)
        worst cmplxty   O(t), where t is the total letters in the query str
        '''
        # print (result)
        # print(now)
        # print(pref)
        if (now != 0):
            if(now[1] != 0):
                if(len (pref) == len(query_str)):
                    self.wildcard_return(now, result, pref)
                
                elif (query_str[len(pref)] == "?"):
                    for i in range(97,123):
                        self.wildcard_check(now[i-95], query_str, result, pref+chr(i))
                
                else:
                    self.wildcard_check(now[ord(query_str[len(pref)])-95], query_str, result, pref+query_str[len(pref)])


    def wildcard_return(self, now, result, pref):
        '''
        this recursive function will keep calling itself when there are more words in front(meaning str frq & prf freq is not equal)
        param           a word
        return          an int
        pre             none
        post            none
        best cmplxity   O(f), f is the number of letters that needed to be return 
        worst cmplxty   O(f), f is the number of letters that needed to be return 
        '''
        if (now != 0):
            if(now[1] != 0):
                for i in range(now[0]):
                    result.append(pref)
                if (now[1] > now[0]):
                    for i in range(97,123):
                        self.wildcard_return(now[i-95], result, pref+chr(i))

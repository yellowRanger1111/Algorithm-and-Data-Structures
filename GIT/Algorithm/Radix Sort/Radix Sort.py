import random
import timeit

def count_sort_radix(array, index_to_sort, base):
    '''
    this function will sort a certain digit(index to sort) in base 10 or at the same logic in any base but might not be a certain digit
    param           array, the power number, base
    return          stable sorted array on that power
    pre             table not sorted
    post            table sorted unsing count sort
    best cmplxity   O(m + b), where m is the length of the array and b is the base 
    worst cmplxty   O(m + b), where m is the length of the array and b is the base   
    '''
    #initiates position and count array
    count = [0] * base
    position = [0] * base

    #count sorting
    for i in range (len (array)):
        count[array[i]//(base**index_to_sort)% base] += 1


    #make posisions
    for i in range(1,base):
        position[i] = position [i - 1] + count [i - 1]


    #creating new array
    new_array = [None] * len(array)

    #inserting the vaiable into the new array in increasing order
    for i in range(len(array)):
        new_array [position[array[i]//(base**index_to_sort)% base]] = array[i]
        position[array[i]//(base**index_to_sort)% base] += 1

    return new_array
    
def radix_sort(array, base):
    '''
    this function will sort the array using radix sort stably
    param           array, base
    return          stable sorted array
    pre             table not sorted
    post            table sorted unsing count sort
    best cmplxity   O(m + b)n, where m is the length of the array and b is the base, n is the largest number in the array 
    worst cmplxty   O(m + b)n, where m is the length of the array and b is the base, n is the largest number of the array
    '''
    #finding the largest item
    max = find_max(array)

    #sorting algorithm
    i = 0
    #when the biggest item is already zero, we know every other number is also covered
    #incrementing iteration = increasing power, which means moving to left item to sort when base 10, other base, same but different represntaion
    while ((max//(base**i)) != 0):
        array = count_sort_radix(array, i, base)
        i +=1
    
    return array


def find_max(array):
    '''
    this function will retrun the largest item on the list
    param           array
    return          largest number
    pre             none
    post            none
    best cmplxity   O(m), where m is the length of the array  
    worst cmplxty   O(m), where m is the length of the array    
    '''
    #finding the maximum item
    max = array[0]
    for i in range(1, len(array)):
        if array [i] > max:
            max = array[i]
    return max


def time_radix_sort():
    '''
    this function will time how long will radix sort take with different bases
    param           none
    return          an array with the tuples are [base, time taken]
    pre             none
    post            none
    best cmplxity   O(k(m + b)n), where m is the length of the array and b is the base, 
                    n is the largest number in the array and k is the number of base we want to test
    worst cmplxty   O(k(m + b)n), where m is the length of the array and b is the base, 
                    n is the largest number in the array and k is the number of base we want to test
    '''
    #making the list with random number
    test_data = [random.randint(1,(2**64)-1) for _ in range(100000)]
    #initiates an array for the time to be saved
    time_list = []

    #how many base we want to try
    for i in range (11, 1, -1):
        #time start
        timer_start = timeit.default_timer()
        
        #radix sort
        a = radix_sort(test_data, i)
        
        #end timer
        end_timer = timeit.default_timer()

        #append (base and time taken (end - start))
        time_list.append([i, end_timer - timer_start])
    
    #return the list of times and base
    return time_list

def find_rotation (string_list, rotation):
    '''
    this function will return words that has the rotation in the original list
    param           list, and the number of rotation
    return          an array words that have the rotation
    pre             none
    post            none
    best cmplxity   O(n)2, where n is the lenght of the string list
    worst cmplxty   O(n)2, where n is the lenght of the string list
    '''
    #initializing array for return
    result = []
    #running a loop for every word in stringlist
    for i in string_list:
        # finding real rotation, meaning if word len = 3
        # then rotating 4 times = to 1 times 
        real_rot = rotation % len(i)
        #find rotation
        rot_word = i[real_rot:] + i[:real_rot]
        #check if the rotation exist in the orignal list
        for l in string_list:
            #if exist, put it in the new list
            if (l == rot_word):
                result.append(i)
                
    return result
        

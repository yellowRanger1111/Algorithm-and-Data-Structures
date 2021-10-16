'''
By : Owen 30039096
'''

from ukkonen import *
import sys


def find_longest_substring (stringa, stringb):
    a = ukkonnen(stringa + "$")
    s_a = a.get_elem_in_order()

    b = ukkonnen(stringb + "$")
    s_b = b.get_elem_in_order()

    max = 0
    
    pointer_a = 0
    pointer_b = 0
    return_array = []

    c = ukkonnen(stringa+"$"+stringb)
    # c.print_labels()

    for current_s_a in s_a:
        for current_s_b in s_b:
            
            k = 0

            while True:
                
                if current_s_a[k] != current_s_b[k]:
                    break
                k += 1
                if k >= len(current_s_a) or k >= len(current_s_b):
                    break

            #finding start point
            pos_a , pos_b = len(stringa) - len(current_s_a) + 1, len(stringb) -len(current_s_b) + 1

            if k == max:
                # if the same, take the smaller one
                insert = False            
                
                for tuple in range(len(return_array)):
                    # print(tuple, pos_a, pos_b)
                    if return_array[tuple][0] == pos_a or return_array[tuple][1] == pos_b:
                        #take the smallest
                        if pos_a < return_array[tuple][0] or pos_b < return_array[tuple][1]:
                            return_array[tuple] = (pos_a, pos_b)
                            insert = True
                            break
                        else:
                            insert = True
                            break
                
                if not insert:
                    return_array.append((pos_a, pos_b))

            elif k > max:
                max = k
                return_array = [(pos_a, pos_b)]

            if current_s_a < current_s_b:
                pointer_a += 1
            else:
                pointer_b +=1

    return max, return_array


def readFiles(pfn):
    patFile = open(pfn, "r")
    pat = patFile.read()
    patFile.close
    return pat

def writeFile (max, data, fn):
    file = open(fn, 'w+')
    file.write(max)
    file.write("\n")
    for lines in data:
        file.write(str(lines[0]))
        file.write(" ")
        file.write(str(lines[1]))
        file.write("\n")        
    file.close()
    


if __name__ == "__main__":
    fileName = sys.argv[1]
    file2Name = sys.argv[2]

    string1 = readFiles(fileName)
    string2 = readFiles(file2Name)
    max, data = find_longest_substring(string1, string2)
    
    writeFile(str(max), data,'output_lcs.txt')
            
    
import sys

class Node:
    def __init__(self, value, new_left=None, new_right=None):
        self.set_left(new_left)
        self.set_right(new_right)
        self.set_value(value)

    def is_leaf(self):
        return self.left == None and self.right == None

    def set_left(self, new_left):
        self.left = new_left
    
    def set_right(self, new_right):
        self.right = new_right
    
    def get_left(self):
        return self.left
    
    def get_right(self):
        return self.right
    
    def set_value(self, nValue):
        self.value = nValue

    def __str__(self):
        return self.value


def huffman (line:str):
    #processing the data
    #array to store the number of character found
    ''' max = 128 formal ascii '''
    array = [0]*128
 
    for char in line:

        array[ord(char)] += 1
    
    new_array = []
    for i in range(len(array)):
        if array[i]!= 0:
            new_array.append((chr(i), array[i], Node(chr(i))))

    new_array = sort(new_array, take_key)

    while len(new_array) > 1:
        a, b = new_array[0], new_array[1]
        new_array = new_array[2:]
        new_array.append((a[0]+ b[0], a[1] + b[1], Node(a[0]+ b[0], a[2], b[2])))
        new_array = sort(new_array, take_key)
        # print("------") 
        # print_array (new_array)
    
    tree = new_array[0][2]
    
    result = []
    make_encrypt(tree, result)
    
    result = sort(result, take_len)
    # print_array(result)

    encryp = to_elias(len(result))

    for item in result:
        # str, encrypt
        encryp += to_binary(ord(item[0])) # ascii
        encryp += to_elias(len(item[1]))
        encryp += item[1]
    
    # print(encryp)
    return encryp
    


def make_encrypt(tree:Node, result, pre = ''):
    if tree.is_leaf():
        if(pre == ""):
            result.append((str(tree), "1"))
        else:
            result.append((str(tree), pre))
    else:
        make_encrypt(tree.left, result, pre+'0')
        make_encrypt(tree.right, result, pre+"1")

    
def print_tree (fruit:Node, indent= 10):
    '''
    very not useful
    '''
    print (" " * indent, fruit)
    if not fruit.is_leaf():
        print_tree (fruit.right, indent+len(str(fruit)))
        print_tree(fruit.left, indent-1)
        
def take_len(k):
    return len(k[1])

def take_key(k):
    return k[1]

def sort(array, f):
    return sorted(array, key= f)

def to_binary(x: int):
    '''
    @return binary form of x
    '''
    return bin(x)[2:]

def print_array(array):
    for row in array:
        for item in row:
            print(item, end=" ")
        print("\n")

def to_elias (num: int):
    '''
    @return elias of a num
    '''
    if num == 1:
        return "1"
    else:
        result = to_binary(num)
        x = len(result) - 1
        temp = to_binary(x)
        temp = "0" + temp[1:]

        result = temp + result
        x = len(temp) -1

        while x > 0:
            temp = to_binary(x)
            temp = "0" + temp[1:]
            result = temp + result
            x = len(temp) -1
        
        return result


def read_file (filename):
    filen = open(filename, "r")
    string = filen.read()
    filen.close()
    return string

def write_file(filename, string):
    filen = open(filename, "w")
    filen.write(string)
    filen.close()


# huffman("A_DEAD_DAD_CEDED_A_BAD_BABE_A_BEADED_ABACA_BED")
# huffman("aacaacabcaba")
# print("011110000111110001001000110001101001")
# to_elias(10)

if __name__ == "__main__":
    file_name = sys.argv[1]
    s = huffman(read_file(file_name))
    write_file("output_header.txt", s)

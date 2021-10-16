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

def print_tree (fruit:Node, indent= 10):
    '''
    very not useful
    debugging purposes only
    '''
    print (" " * indent, fruit)
    if not fruit.is_leaf():
        print_tree (fruit.right, indent+len(str(fruit)))
        print_tree(fruit.left, indent-1)


def decode_lszz(string):
    # read first elias
    num, iter = decode_elias(string)
    string = string[iter:]

    enc = []

    #taking the coded word
    for _ in range(num):
        ascii = string[:7]
        string = string[7:]

        a, s = decode_elias(string)
        string = string[s:]

        code = string[:a]
        string = string[a:]

        enc.append(( chr(int(ascii, 2)), code))

    # print(enc)
    # print(string)
    
    """
    MAKE TREE
    """

    root = Node("-")

    for char,code in enc:
        # char, code
        current = root
        for i in code:
            if i == "1":
                if current.right == None:
                    current.right = Node("-")
                current = current.right
            else:
                if current.left == None:
                    current.left = Node("-")
                current = current.left
        current.set_value(char)

    # print_tree(root)


    num, iter = decode_elias(string)
    string = string[iter:]
    result_str = ""


    for _ in range(num):
        if string[0] == "1":
            #bit 1
            #take the 1 out
            string = string[1:]
            
            iter = 0
            done = False
            current = root
            while not done:
                if string[iter] == "0":
                    current = current.left
                elif string[iter] == "1":
                    current = current.right
                else:
                    #sanity testing
                    raise Exception("invalid syntax in: " + string[iter] + "-" + iter)
                
                if current.is_leaf():
                    done = True
                    result_str += str(current)
                    string = string[iter+1:]
                else:
                    iter += 1
                
        else:
            # bit 0
            # take the 0 out
            string = string[1:]

            
            """num 1"""
            num1, iter = decode_elias(string)
            string = string[iter:]

            '''num 2'''
            num2, iter = decode_elias(string)
            string = string[iter:]

            for i in range(num2):
                result_str += result_str[-num1]
        
        # print (result_str)
    
    print(result_str)
    return result_str

def decode_elias (string):
    start = 0
    stop = 1
    done = 0
    while not done:
        if string[start] == "1":
            # print("&")
            return int( string[start:stop], 2), stop
        else:
            # print("*")
            temp = "1" + string[start+1:stop]
            num = int( temp, 2) + 1
            # print(num)
            start = stop 
            stop = start + num 

def read_file (filename):
    filen = open(filename, "r")
    string = filen.read()
    filen.close()
    return string

def write_file(filename, string):
    filen = open(filename, "w")
    filen.write(string)
    filen.close()

# string = "01111000011111000100100011000110100100011111111010011000100100001101111"
#         # 01111000011111000100100011000110100100011111111010011000100100001101111
# decode_lszz(string)


files = ["encoder_output7_L6_B3.txt", "encoder_output8_L50_B15.txt"]
out_file = ["output_lzss_decoder7.txt", "output_lzss_decoder8.txt"]

for i in range(len(files)):
    decode_lszz(read_file(files[i]))
    print(read_file(out_file[i]))

if __name__ == "__main__":
    file_name = sys.argv[1]
    s = decode_lszz(read_file(file_name))
    write_file("output_decoder_lzss.txt", s)
import Task3
import Task2 as ListADT

class StackADT:
    def __init__(self):
        self.history = ListADT.ListADT(40)
    
    def last_item(self):
        return self.history[-1]

    def is_empty(self):
        return self.history.is_empty()
    
    def push(self, thing):
        self.history.append(thing)
    
    def pop(self):
        if (self.is_empty()):
            raise Exception("Empty")
        else:
            self.history.delete(-1) 


class Editor:
    def __init__(self):
        """
        this function initialize the class Editor
        param          the new class defined
        return         none
        pre            none
        post           a editor class have been created
        complexity     best and worst case: O(1)
        """
        self.text_lines = ListADT.ListADT(40)
        self.history = StackADT()


    def read_filename(self, file_name):
        """
        this function will read a file and return to txt line
        param          file name
        return         none
        pre            none
        post           text line filled
        complexity     best and worst case: O(n) where n is the row in file
                        
        """
        self.text_lines = Task3.read_text_file(file_name)
        self.history = StackADT()

        
    def print_num(self, line_num):           
        """
        this function will print an item in index line_num -1 
        param          the list class, index of item wanted to be returned
        return         none
        pre            none
        post           item printed
        complexity     best and worst case: O(1)
        """
        line_num = int(line_num)
        if line_num < 0:
            print(self.text_lines[line_num])
        elif line_num == 0:
            raise IndexError
        else:
            print(self.text_lines[line_num - 1])


    def delete_num(self, line_num):
        """
        this function will delete an item 
        param          the list class, index where the item wanted to be deleted
        return         none
        pre            none
        post           item is deletd in text lines
        complexity     best and worst case: O(n), n is equal to the length of the array 
                        minus the index required
        """
        if(line_num == ""):
            all = []
            for i in range (len(self.text_lines)):
                all.append(self.text_lines[0])
                self.text_lines.delete(0)
            self.save(["delete all", all])
        
        else:    
            line_num = int(line_num)
            
            if line_num < 0:
                self.save(["delete", line_num, self.text_lines[line_num]])
                self.text_lines.delete(line_num)
                
            elif line_num == 0:
                raise IndexError
            else:
                self.save(["delete", line_num, self.text_lines[line_num -1]])
                self.text_lines.delete(line_num - 1)

    def insert_num_strings(self, line_num, lines):
        """
        this function will insert item into the list 
        param          the list class, index and the item to be placed
        return         none
        pre            none
        post           item is initialize into text line
        complexity     best and worst case: O(nm), n is equal to the length of the array 
                        minus the index required, m is equael to the line inserted
        """
        line_num = int(line_num)

        if line_num < 0:
            for i in range(len(lines)):
                self.text_lines.insert(line_num, lines[i])
            self.save(["insert", line_num, len(lines)])
        elif line_num == 0:
            raise IndexError
        else:
            for i in range(len(lines)):
                self.text_lines.insert(line_num - 1 + i, lines[i])
            self.save(["insert", line_num, len(lines)])

    def search_string(self, query):
        """
        this function will find where can we get the query
        param          the list class, the query
        return         a list where the query is found
        pre            none
        post           none
        complexity     best and worst case : (O)mnl, where m = length of text in the class,
                       n :  length of the list[m], l : is the length of the query 
        """
        save = ListADT.ListADT()
        
        for i in range(len(self.text_lines)):
            for j in range((len(self.text_lines[i]) - len(query))+ 1):
                string_now = ""
                for l in range(len(query)):
                    string_now += self.text_lines[i][j+l]
                if (string_now == query):
                    save.append(i + 1)
                    break
        return save
    
   
                    
    def menu(self):
        """
        this function will run the menu and do the input
        param          the class
        return         none
        pre            none
        post           none
        complexity     best and worst case : ?
        """
        input_string = [""]
        while (input_string[0].lower() != "quit"):
            input_string = input("> ").split()
            print(input_string)

            
            if (len(input_string) > 2):
                print("error command")

            elif input_string[0].lower() == "print":
                if (len(input_string)==1):
                    for i in range(len(self.text_lines)):
                        self.print_num(i+1)
                
                else:
                    try:
                        self.print_num(input_string[1])
                    except ValueError:
                        print("? Index must be a number")
                    except IndexError:
                        print("? Index out Of Range")                    
            
            elif input_string[0].lower() == "read":
                try:
                    self.read_filename(input_string[1])
                except FileNotFoundError:
                    print("? file does not exist")
                except IndexError:
                    print ("? wrong command")
            
            elif input_string[0].lower() == "insert":
                insert_strings = []
                add = ''
                while (add != "."):
                    add = input("+ ")
                    if not (add == "."):
                        insert_strings.append(add)
                
                try:
                    self.insert_num_strings(input_string[1], insert_strings)
                except ValueError:
                    print("? Index must be a number")
                except IndexError:
                    print("? Index Error")

            elif input_string[0].lower() == "delete":
                try:
                    self.delete_num(input_string[1])
                except ValueError:
                    print("? Index must be a number")
                except IndexError:
                    print("? Index out Of Range")
            
            elif input_string[0].lower() == "search":
                print(self.search_string(input_string[1]))

            elif input_string[0].lower() == "quit":
                pass
            
            elif input_string[0].lower() == "undo":
                if (len(input_string)==1):
                    try:
                        self.undo()
                    except Exception:
                        print("? nothing to undo")
                
                else:
                    print("? error command")

            else:
                print ("error command")
                


    def undo(self):
        """
        this function will undo the last move
        param          the list class
        return         none
        pre            none
        post           none
        complexity     best and worst case : (O)n where n is equal to last_item()[2] 
                       where n is number of item deleted or inserted
        """
        if not (self.history.is_empty()):
            if (self.history.last_item()[0] == "delete"):
                self.insert_num_strings(self.history.last_item()[1], [self.history.last_item()[2]])
                self.history.pop()
            
            elif(self.history.last_item()[0] == "insert"):
                for i in range(self.history.last_item()[2]):
                    self.delete_num(self.history.last_item()[1])
                    self.history.pop()
            
            elif (self.history.last_item()[0] == "delete all"):
                for i in range(len(self.history.last_item()[1])):
                    self.insert_num_strings(-1, [self.history.last_item()[1][i]])
                    self.history.pop()
            
            self.history.pop()
        else:
            raise Exception("Nothing to undo")
    
    def save(self, thing):
        """
        this function will save the last thing done
        param          the list class, the thing
        return         none
        pre            none
        post           none
        complexity     best and worst case : (O)1
        """
        self.history.push(thing)


ed = Editor()
ed.menu()
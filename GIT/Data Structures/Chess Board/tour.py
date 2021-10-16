from unsorted_list import List

class Tour:
    
    board_rows = 8
    board_cols = 8
    board_size = board_rows * board_cols
    
    def __init__(self):
        """
        this function initialize the class tour
        param          the new class defined
        return         none
        post           a new class with the position of 1, 1 is created
        complexity     best and worst case: O(1)
        """
        # You may wish to add additional attributes to the object.
        self.moves = List(Tour.board_size)
        self.moves.add_last( (1, 1) ) # Set a starting position
        self.saved_list = None

    def move_knight(self, row, col):
        """
        this function is to moves the knight 
        param          the knight(obj) that want to be move, moved where (row, col)
        return         none
        post           the knight move place to the new row and col and saved the last move
        complexity     best and worst case: O(1)
        """
        try:
            assert self.moves.length() < Tour.board_size
        except AssertionError as err:
            print ("list is full")
        else:
            self.moves.add_last( (row, col) )

    def show_tour(self):
        """
        this function shows all moves done by the knight
        param          the knight(obj) that wanted to be shown
        return         none
        post           the places where the knights position (past and now) is printed
        complexity     best and worst case: O(n*m) where n : tour.board_rows and m : tour.board_col
        """
        for r in range(1, Tour.board_rows+1):
            for c in range(1, Tour.board_cols+1):
                pos = self.moves.index( (r, c) )
                cell_char = '.'
                if pos is not None:
                    if pos == self.moves.length()-1:
                        cell_char = 'K'
                    else:
                        cell_char = '*'

                print(cell_char, end=' ')
            print('')

    def delete_pos(self, delete_item):
        '''
        this function deletes a single position as requested
        param          the knight(obj) that the moves want to be deleted, and the moves that want to be deleted
        return         none
        post           the places where the knights position deleted
        complexity     best and worst case: O(n) where n : tour.board_size
        '''
        try:
            assert self.moves.length() > 0
        except AssertionError as err:
            print ("not found")
        else:
            self.moves.delete_item( delete_item )

    def undo_moves(self):
        """
        this function deletes the last move of the knight
        param          the knight(obj) that the moves want to be deleted, and the moves that want to be deleted
        return         none
        post           the last knights position is deleted
        complexity     best and worst case: O(1) 
        """
        try:
            assert self.moves.length() > 1
        except AssertionError:
            print("Knight have not been moved")
        else:
           self.delete_pos(self.moves.last_item())

    def reset_board(self, row, col):
        """
        this function clears the board and reinitiate the starting position
        param          the knight(obj), the new starting row and col
        return         none
        post           the board claers and the knight starts a new
        complexity     best and worst case: O(1) 
        """
        self.moves = List(Tour.board_size)
        self.moves.add_last( (row, col) ) # Set a starting position

    def copy_list (self):
        """
        this function save the partial tour for reagained later
        param          the knight(obj)
        return         none
        post           saving the partial list to a private variable
        complexity     best and worst case: O(n) n is length of variable saved
        """
        self.saved_list = List(Tour.board_size)
        for i in range (self.moves.length()):
            self.saved_list.add_last(self.moves.the_array[i])

    def set_list(self):
        """
        this function retore the saved list to the current list
        param          the knight(obj)
        return         none
        post           list retored from the private variable
        complexity     best and worst case: O(n) n is length of variable saved 
        """
        if self.saved_list == None:
            print ("No Saved List")
        else:
            self.moves = List(Tour.board_size)
            for i in range (self.saved_list.length()):
                self.moves.add_last(self.saved_list.the_array[i])

    def next_move(self):
        """
        this function show where can the knight move next
        param           the knight that want to move
        return          list containing all possible moves
        post            none
        complexity      best and worst case: O(1)
        """
        row , col  = self.moves.last_item()
        
        possible_moves = []
        
        #possibilty 1
        row_try = row + 1
        col_try = col + 2

        if (row_try <= self.board_rows and col_try <= self.board_cols):
            if self.moves.index((row_try,col_try))== None:
                possible_moves.append((row_try, col_try))

        #possibility 2
        row_try = row + 1
        col_try = col - 2

        if (row_try <= self.board_rows and col_try > 0):
            if self.moves.index((row_try,col_try))== None:
                possible_moves.append((row_try, col_try))

        #possibilty 3
        row_try = row - 1
        col_try = col + 2

        if (row_try >0 and col_try <= self.board_cols):
            if self.moves.index((row_try,col_try))== None:
                possible_moves.append((row_try, col_try))

        #possibility 4
        row_try = row - 1
        col_try = col - 2

        if (row_try > 0 and col_try > 0):
            if self.moves.index((row_try,col_try))== None:
                possible_moves.append((row_try, col_try))
        
        #possibilty 5
        row_try = row + 2
        col_try = col + 1

        if (row_try <= self.board_rows and col_try <= self.board_cols):
            if self.moves.index((row_try,col_try))== None:
               possible_moves.append((row_try, col_try))

        #possibility 6
        row_try = row + 2
        col_try = col - 1

        if (row_try <= self.board_rows and col_try > 0):
            if self.moves.index((row_try,col_try))== None:
                possible_moves.append((row_try, col_try))

        #possibilty 7
        row_try = row - 2
        col_try = col + 1

        if (row_try >0 and col_try <= self.board_cols):
            if self.moves.index((row_try,col_try))== None:
                possible_moves.append((row_try, col_try))

        #possibility 8
        row_try = row - 2
        col_try = col - 1

        if (row_try > 0 and col_try > 0):
            if self.moves.index((row_try,col_try))== None:
                possible_moves.append((row_try, col_try))

        return possible_moves
    
    def valid_move(self, list_possible, row, col):
        """
        this function will check is the user input and validate it
        param           the knight that want to move, the location requested and the position want to be moved to
        return          true or false
        post            none
        complexity      best and worst case: O(n) where n is length of list_possible

        """
        position_now = (row, col)
        for item in list_possible:
            if item == position_now:
                return True
        return False

def test_move():
    test = Tour ()
    test_array = [None]*64
    test.move_knight(2,2)
    test_array[0] = (1,1)
    test_array[1] = (2,2)
    assert test.moves.the_array == test_array
    test.move_knight(3,3)
    test_array[2] = (3,3)
    assert test.moves.the_array == test_array
    test = Tour ()

    for i in range(64):
        test.move_knight(1,1)
    
    test_array = [(1,1)]*64

    assert test.moves.the_array == test_array
    assert not test.move_knight(1,1)

def test_delete():
    test1 = Tour()
    test1.move_knight(2,2)
    test1.move_knight(3,3)
    test1_array = [None]*64
    test1_array[0] = (1,1) #starting position
    test1_array[1] = (2,2)
    test1_array[2] = (3,3)
    assert test1.moves.the_array == test1_array
    test1.delete_pos((3,3))
    assert test1.moves.length() == 2

def test_undo_move():
    test = Tour()
    test.move_knight(2,2)
    test.undo_moves()
    assert test.moves.length() == 1
    assert test.moves.last_item() == (1,1)

def test_save_and_restore ():
    test = Tour ()
    test.move_knight(2,2)
    test.move_knight(3,3)
    test.copy_list()
    test_array = [None]*64
    test_array[0] = (1,1)
    test_array[1] = (2,2)
    test_array[2] = (3,3)
    assert test.saved_list.the_array == test_array
    test.move_knight(4,4)
    test.set_list()
    assert test.moves.the_array == test_array

def test_valid_move_and_next_move():
    test = Tour()
    test_array_possible_move = [(2,3), (3,2)]
    assert test.next_move() == test_array_possible_move
    assert test.valid_move(test_array_possible_move, 2,3)
    assert not test.valid_move(test_array_possible_move, 8,3)








if __name__ == '__main__':
    test_move()
    test_delete()
    test_undo_move()
    test_save_and_restore()
    test_valid_move_and_next_move()
    print ("all test passed")
    

    

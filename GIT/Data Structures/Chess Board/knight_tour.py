#getting the tour class
from tour import Tour

#creating the knight object
knight = Tour()
#initialize the loop
quitted = False

# knight.move_knight(2,1)
# knight.move_knight(2,5)
# knight.show_tour()

# knight.delete_pos((2,5))
# knight.show_tour()

while not quitted:
    #what the user want to do?
    user_input = input("1 : Move Knight \n2 : Undo\n3 : Reset Board\n4 : Save List\n5 : Restore List\n6 : Quit\n--> ")

    if (user_input == "1"):
        #printing next move
        possible_moves = knight.next_move()
        print("possibe moves", possible_moves)

        quit_inner_loop = False
        #if no more possible moves, player automatically quit
        if (len(possible_moves) == 0):
            print ("LOL U LOSE")
            quitted = True
            quit_inner_loop = False
        
        while not quit_inner_loop:
            #user input
            row_new = input("Move knight to which row ? ")
            col_new = input("Move knight to which col ? ")

            #making sure is the input is a number
            try: 
                row_new, col_new = int(row_new), int(col_new)
            
            #if err
            except ValueError as err:
                print ("err : ", err) 

            #if true, do this code
            else:
                
                #if valid do it
                if (knight.valid_move(possible_moves, row_new, col_new)):
                    quit_inner_loop= True
                #not valid, cannot move
                else:
                    print("not possible! Knight can only move in L\n")
            
        
        #move the knight to designated space
        knight.move_knight(row_new, col_new)
        #show the tour
        knight.show_tour()
     
    
    elif (user_input == "2"):
        #delete the last move
        knight.undo_moves()
        #show the tour
        knight.show_tour()

    elif (user_input == "3"):
        #ask for the new starting position
        row_new = int(input("Move knight to which row ? "))
        col_new = int(input("Move knight to which col ? "))
        
        try: 
            row_new, col_new = int(row_new), int(col_new)
        except ValueError as err:
            print ("err : ", err) 
        else:
            #reset
            knight.reset_board(row_new, col_new)
            #show tour
            knight.show_tour()

    elif user_input == "4":
        #ask to save
        knight.copy_list()
        print("List have been saved")
        
    elif user_input == "5":
        #restore list
        knight.set_list()
        print("List have been Restored")
        knight.show_tour()

    elif (user_input == "6"):
        #means user want to quit
        quitted = True
    
    print ("")
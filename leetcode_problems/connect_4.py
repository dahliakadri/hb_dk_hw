#connect 4

Design Connect 4 with stubs (global variables, functions, objects, etc.).

Global Variables:

Objects:
Board
2D array
[O,O,O,O,O,O,O]
[O,O,O,O,O,O,O]
[O,O,O,O,O,O,O]
[O,O,O,O,O,O,O]
[O,O,O,O,O,O,O]
[O,O,O,O,O,O,O]

Functions:
build_board():
instantiates the board

start_game():  
Calls add_piece, check_connection, end_game, will only call play_game_again if end_game = TRUE

add_piece(color, coordinates):
Mark space as red or black
Check_if_legal_move 
If space is already taken or not AND
If the space directly under is already taken OR
We’re on the bottom of the board

update_board()

check_connection(board, new_piece): 
 check the 8 spaces around it for like color. If connected, increment red or black count

end_game():
If red or black count = 4
End in a draw:
All pieces are covered, even if red or black count < 4

change_turn()

play_game_again()
Resets the board
Reset red and black counts

What to keep track of?
Where reds/blacks are placed on the board
Number of connected reds/blacks and whether they equal 4
Games score

#Global Variables


from os import system, name


#If game is still going
game_still_going = True


#current player
current_player = "X"


#win or tie
winner = None


#game board
board=[ "-", "-", "-", 
        "-", "-", "-", 
        "-", "-", "-"	]


#display board
def display_board():
	print(board[0] + " | " + board[1] + " | " + board[2] + " | ")
	print(board[3] + " | " + board[4] + " | " + board[5] + " | ")
	print(board[6] + " | " + board[7] + " | " + board[8] + " | ")


#clear screen
def screen_clear():
   if name == 'nt':
      _ = system('cls')
  #  for mac and linux(here, os.name is 'posix')
   else:
      _ = system('clear')


#play game
def play_game():  
  
  #display initial board
  display_board()
  #game structure
  while game_still_going:
    
    #handle turn for an arbitrary player
    handle_turn(current_player)

    #check if game over on every turn, can be optimized to implement it after 4 turns
    check_if_game_over()

    #give turn to other player 
    flip_player()

  #print the winner
  if winner == "X" or winner == "O":
    print(winner + " won")
  elif winner == None:
    print("Tie")  

#handles every turn
def handle_turn(player):

  print("\n\n" + player + "'s turn.")
  position = input("choose a position from 1-9: ")
  
  valid = False
  while not valid:
    
    #check if user entered the required posotion
    while position not in ["1","2","3","4","5","6","7","8","9"]:
      position = input("Invalid input. Go again. ")

    #the index of list starts from 0, so it is necessary to decline the entered value by 1
    position = int(position) -1  
    
    #validate the entry
    if board[position] == "-":
      valid = True
    else:
      print("You can't place there. Go again\n\n")
    
  
  board[position]=player
  screen_clear()
  display_board()


def check_if_game_over():
  check_for_win()
  check_if_tie()


def check_for_win():

  global winner

  row_winner = check_rows()
  col_winner = check_col()
  diagonal_winner = check_diagonals()

  if row_winner:
    winner = row_winner
  elif col_winner:
    winner = col_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner=None


def check_rows():
  global game_still_going
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  
  if row_1 or row_2 or row_3:
    game_still_going = False
  
  #return who won
  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]


def check_col():
  global game_still_going
  col_1=board[0] == board[3] == board[6] != "-"
  col_2=board[1] == board[4] == board[7] != "-"
  col_3=board[2] == board[5] == board[8] != "-"

  if col_1 or col_2 or col_3:
    game_still_going = False

  if col_1:
    return board[0]
  elif col_2:
    return board[1]
  elif col_2:
    return board[2]


def check_diagonals():
  global game_still_going
  d_1 = board[0] == board[4]  == board[8]  !="-"
  d_2 = board[2] == board[4]  == board[6]  !="-"

  if d_1 or d_2:
    game_still_going = False
  
  if d_1:
    return board[0]
  elif d_2:
    return board[2]


def check_if_tie():

  global game_still_going
  if "-" not in board:
    game_still_going=False


#it changes the turn
def flip_player():

  global current_player

  if current_player == "X":
    current_player = "O"
  elif current_player=="O":
    current_player = "X"


play_game()

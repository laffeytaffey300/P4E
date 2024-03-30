import random

def check_win(turn_counter, board_values, winner):
  game_over = 0
  if turn_counter >= 5 and (
    (board_values["A1"] != " " and board_values["A1"] == board_values["B1"] and board_values["B1"] == board_values["C1"]) or 
    (board_values["A2"] != " " and board_values["A2"] == board_values["B2"] and board_values["B2"] == board_values["C2"]) or 
    (board_values["A3"] != " " and board_values["A3"] == board_values["B3"] and board_values["B3"] == board_values["C3"]) or 
    (board_values["A1"] != " " and board_values["A1"] == board_values["A2"] and board_values["A2"] == board_values["A3"]) or 
    (board_values["B1"] != " " and board_values["B1"] == board_values["B2"] and board_values["B2"] == board_values["B3"]) or 
    (board_values["C1"] != " " and board_values["C1"] == board_values["C2"] and board_values["C2"] == board_values["C3"]) or 
    (board_values["A1"] != " " and board_values["A1"] == board_values["B2"] and board_values["B2"] == board_values["C3"]) or 
    (board_values["C1"] != " " and board_values["C1"] == board_values["B2"] and board_values["B2"] == board_values["A3"])):
    print ("Game over. {} win!".format(winner))
    game_over = 1
  elif turn_counter == 9:
    print("It's a tie")
    game_over = 1
  return game_over
    
def show_board(board_values):
  print("""
      A.  B.  C.  
  1.  {} | {} | {} 
     -----------   
  2.  {} | {} | {} 
     -----------
  3.  {} | {} | {} """.format(board_values["A1"], board_values["B1"], board_values["C1"], board_values["A2"], board_values["B2"], board_values["C2"], board_values["A3"], board_values["B3"], board_values["C3"]))

def opening(board_values):
  player_input = ""
  while player_input != "X" and player_input != "O":
    player_input = str(input("Do you want to be X's or O's? ")).upper()
    if player_input != "X" and player_input != "O":
      print("Oops! Please enter 'x' or 'o'")
    else:
      if player_input == "X": computer = "O"
      else: computer = "X"
      show_board(board_values)
  return player_input, computer

def player_turn(player_symbol, turn_counter, available_spaces, board_values):
  player_choice = ""
  while player_choice not in available_spaces:
    player_space_input = input("Where would you like to go? ")
    player_choice = player_space_input.upper()
    if player_choice not in available_spaces:
      print("Oops! That spot either isn't available, or isn't on the board. Here are your available spaces:")
      print(available_spaces)
  board_values[player_choice] = player_symbol
  available_spaces.remove(player_choice)
  print("You went here: " + str(player_choice))
  show_board(board_values)
  turn_counter += 1
  game_over = check_win(turn_counter, board_values, "You")
  return board_values, turn_counter, game_over

def computer_turn(computer_symbol, turn_counter, available_spaces, board_values):
  computer_choice = random.choice(available_spaces)
  board_values[computer_choice] = computer_symbol
  available_spaces.remove(computer_choice)
  print("I'll go here: " + str(computer_choice))
  show_board(board_values)
  turn_counter += 1
  game_over = check_win(turn_counter, board_values, "I")
  return board_values, turn_counter, game_over
  
def game():
  while 1==1:
    board_values = {"A1": " ", "A2":" ", "A3": " ", "B1": " ", "B2":" ", "B3": " ", "C1": " ", "C2":" ", "C3": " "}
    available_spaces = [key for key, value in board_values.items() if value == " "]
    turn_counter = 0 
    game_over = 0
    player_symbol, computer_symbol = opening(board_values)
    while game_over != 1:
      board_values, turn_counter, game_over = player_turn(player_symbol,turn_counter, available_spaces, board_values)
      if game_over !=1 and len(available_spaces) > 0:
        board_values, turn_counter, game_over = computer_turn(computer_symbol,turn_counter, available_spaces, board_values)
    print("Let's play again!")

game()

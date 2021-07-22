import random

def display_board(board):
	#print('\n'*100)
	print(board[7] +'|'+ board[8] +'|'+ board[9])
	print(board[4] +'|'+ board[5] +'|'+ board[6])
	print(board[1] +'|'+ board[2] +'|'+ board[3])


def player_input_marker():
	marker = ''

	while marker != 'X' and marker != 'O':
			marker = input("Player 1 choose your marker: ").upper()
	if marker == 'X':
		print("Player 2 is O.")
		return ('X', 'O')
	else:
		print("Player 2 is X.")
		return ('O', 'X')

def place_marker_on_board(board, marker, position):
	board[position] = marker


def win_check(board):
	return((board[7] == board[8] == board[9] != ' ') or
		   (board[4] == board[5] == board[6] != ' ') or
		   (board[1] == board[2] == board[3] != ' ') or
		   (board[7] == board[4] == board[1] != ' ') or
		   (board[8] == board[5] == board[2] != ' ') or
		   (board[9] == board[6] == board[3] != ' ') or
		   (board[1] == board[5] == board[9] != ' ') or
		   (board[7] == board[5] == board[3] != ' '))

def choose_first():
	flip = random.randint(1,2)
	if flip == 1:
		return 'Player 1'

	else:
		return 'Player 2'


def space_check(board, position):
	return board[position] == ' '

def full_board_check(board):
	for i in range (1,10):
		if space_check(board, i):
			return False
	return True

def player_choice(board, turn):
	position = 0

	while position not in range(1,10) or not space_check(board, position):
		position = int(input(turn + " choose a position: (1 - 9): "))

	return position

def replay():
	choice = input("Play again? Enter y or n")
	return choice == 'y'



print("Welcome")

while True:

	# PLAY THE GAME
	## SET EVERYTHING UP 
	the_board = [' ']*10
	player1_marker, player2_marker = player_input_marker()
	turn = choose_first()
	print(turn + ' will go first')
	play_game = input("Ready to play? y or n: ")

	if play_game == 'y':
		game_on = True
	else:
		game_on = False

	while game_on:
		if turn == 'Player 1':

			# show the board
			display_board(the_board)

			# choose position
			position = player_choice(the_board, turn)

			# place the marker
			place_marker_on_board(the_board, player1_marker, position)

			# check if player won
			if win_check(the_board):
				display_board(the_board)
				print("PLAYER 1 WIN ")

				game_on = False


			else:
				if full_board_check(the_board):
					display_board()
					print("tie")
					game_on = False
				else:
					turn = 'Player 2'


		else:
			# show the board
			display_board(the_board)

			# choose position
			position = player_choice(the_board, turn)

			# place the marker
			place_marker_on_board(the_board, player2_marker, position)

			# check if player won
			if win_check(the_board):
				display_board(the_board)
				print("PLAYER 2 WIN ")

				game_on = False


			else:
				if full_board_check(the_board):
					display_board(the_board)
					print("tie")
					game_on = False
				else:
					turn = 'Player 1'























	if not replay():
		break




































# table = [[' ', ' ', ' '],
# 		 [' ', ' ', ' '],
# 		 [' ', ' ', ' ']]


# def permutation(mylist):

# 	if len(mylist) == 0:
# 		return []

# 	if len(mylist) == 1:
# 		return [mylist]

# 	temp = [] 
	
# 	for i in range(len(mylist)):
# 		m = mylist[i]
# 		restList = mylist[:i] + mylist[i+1:]

# 		for p in permutation(restList):
# 			temp.append([m] + p)

# 	return temp


# def display_board(table):
# 	k1, k2, k3 = table[0][0], table[0][1], table[0][2]
# 	k4, k5, k6 = table[1][0], table[1][1], table[1][2]
# 	k7, k8, k9 = table[2][0], table[2][1], table[2][2]

# 	print("\t\t|\t \t|")
# 	print("\t{}\t|\t{}\t|\t{}".format(k7, k8, k9))
# 	print("\t \t|\t \t|")
# 	print("\t-----------------------------------")
# 	print("\t \t|\t \t|")
# 	print("\t{}\t|\t{}\t|\t{}".format(k4, k5, k6))
# 	print("\t \t|\t \t|")
# 	print("\t-----------------------------------")
# 	print("\t \t|\t \t|")
# 	print("\t{}\t|\t{}\t|\t{}".format(k1, k2, k3))
# 	print("\t \t|\t \t|")

# def check_win(posicoes):
# 	table_check = [[1, 2, 3],
# 				   [4, 5, 6],
# 				   [7, 8, 9]]
# 	# line win
# 	if   posicoes in permutation([1, 2, 3]):
# 		return True
# 	elif posicoes in permutation([4, 5, 6]):
# 		return True
# 	elif posicoes in permutation([7, 8, 9]):
# 		return True

# 	# column win
# 	elif posicoes in permutation([1, 4, 7]):
# 		return True
# 	elif posicoes in permutation([2, 5, 8]):
# 		return True
# 	elif posicoes in permutation([3, 6, 9]):
# 		return True

# 	elif posicoes in permutation([3, 5, 7]):
# 		return True
# 	elif posicoes in permutation([1, 5, 9]):
# 		return True
# 	else:
# 		pass

# 	# # line win
# 	# if table[0][0] == table[0][1] and table[0][1] == table[0][2]:
# 	# 	return True
# 	# elif table[1][0] == table[1][1] and table[1][1] == table[1][2]:
# 	# 	return True
# 	# elif table[2][0] == table[2][1] and table[2][1] == table[2][2]:
# 	# 	return True

# 	# # column win
# 	# elif table[0][0] == table[1][0] and table[1][0] == table[2][0]:
# 	# 	return True
# 	# elif table[0][1] == table[1][1] and table[1][1] == table[2][1]:
# 	# 	return True
# 	# elif table[0][2] == table[1][2] and table[1][2] == table[2][2]:
# 	# 	return True
	
# 	# # column win
# 	# elif table[0][0] == table[1][1] and table[1][1] == table[2][2]:
# 	# 	return True
# 	# elif table[0][2] == table[1][1] and table[1][1] == table[2][0]:
# 	# 	return True
# 	# else:
# 	# 	pass

# def player_move(value, pos, table):
# 	if   pos == 1:
# 		table[0][0] = value
# 	elif pos == 2:
# 		table[0][1] = value
# 	elif pos == 3:
# 		table[0][2] = value
# 	elif pos == 4:
# 		table[1][0] = value
# 	elif pos == 5:
# 		table[1][1] = value
# 	elif pos == 6:
# 		table[1][2] = value
# 	elif pos == 7:
# 		table[2][0] = value
# 	elif pos == 8:
# 		table[2][1] = value
# 	elif pos == 9:
# 		table[2][2] = value		
# 	else:
# 		pass
# 	return table

# def input_valid(player_position):
# 	if player_position in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
# 		return True
# 	else:
# 		return False


# player_1 = input("\tPlayer 1 choose a marker: X or O: ")

# if player_1 == 'X':
# 	player_2 = 'O'
# else:
# 	player_2 = 'X'
# print("\tPlayer 2 is {}\n".format(player_2))
# print("Welcome to Tic Tac Toe!!!")	
# display_board(table)
# player_1_pos = []
# player_2_pos = []

# while True:

# 	p1_pos = int(input("Player 1 choose your position: "))
# 	player_1_pos.append(p1_pos)
# 	player_move(player_1, player_1_pos[-1], table)
# 	display_board(table)
# 	if check_win(player_1_pos):
# 		print("\n\t{} WINS!\n".format(player_1))
# 		break

# 	p2_pos = int(input("Player 2 choose your position: "))
# 	player_2_pos.append(p2_pos)
# 	player_move(player_2, player_2_pos[-1], table)
# 	display_board(table)
# 	print(player_2_pos)
# 	if check_win(player_2_pos):
# 		print("\n\t{} WINS!\n".format(player_2))
# 		break

# # display_board(table)
# # p1_pos = input("Player 1 choose a position for your marker:")
# # player_move(player_1, p1_pos, table)
# # display_board(player_move(player_1, p1_pos, table))
# # p2_pos = input("Player 2 choose a position for your marker:")
# # player_move(player_2, p2_pos, table)
# # display_board(player_move(player_2, p1_pos, table))
# # check_win(table)





# # table = ['', '', '', '', '', '', '', '', '']

# # while True:
# # 	print("Player 1 choose your position on the board.")
# # 	player_pos = int(input("Choose a position from (1 - 9): "))
# # 	table[player_pos - 1] = player_1
# # 	display_board(table)	
# # 	print("Player 2 choose your position on the board.")
# # 	player_pos = int(input("Choose a position from (1 - 9): "))
# # 	table[player_pos - 1] = player_2
# # 	display_board(table)
# # 	check_win(table)
# # # print("You choose {}.".format(player_1))
# # # display_board(player_choice)



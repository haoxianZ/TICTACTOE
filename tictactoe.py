
def display_board(board):
	print(board[7]+'|'+ board[8]+'|'+ board[9])
	print(board[4]+'|'+ board[5]+'|'+ board[6])
	print(board[1]+'|'+ board[2]+'|'+ board[3])

def player_input():
    
    player1_marker=''
    while player1_marker !='X' and player1_marker!='O':
        player1_marker= input('Player1 chooses X or O:')
        if player1_marker == 'X':
            player2_marker='O'
            print('player 1, X, goes first')
            
            
        else:
            player2_marker='X'
            player1_marker='O'
            print('player 2, X, goes first')
        return(player1_marker, player2_marker)
def place_maker(board,player_marker,position):
	board[position]= player_marker
#if someone win, returns true
def win_check(board, mark):
    if board[1]==board[2]==board[3]==mark or board[4]==board[5]==board[6]==mark or board[7]==board[8]==board[9]==mark:
        return True
    elif board[1]==board[4]==board[7]==mark or board[2]==board[5]==board[8]==mark or board[3]==board[6]==board[9]==mark:
        return True
    elif board[1]==board[5]==board[9]==mark or board[3]==board[5]==board[7]==mark:
        return True
    
    else:
        return False
# if is occupied, return false
def space_check(board, position):
	return board[position] == ''
#if it is full, return true
def full_board(board):
	for i in range(1,len(board)+1):
		if board[i] != 'X' or 'O':
			return False
		else:
			return True

# player choosing where they want to put it
def player_choice(board, player_marker):
	x=int(input('where do you want to put it? from 1 to 9'))
	if space_check(board,x) == False:
		print('this is occupied, try again')
		x=int(input('where do you want to put it? from 1 to 9'))
	else:
		board[x] = player_marker
			

# putting the game together

print('This is tic tac toe')

#set up the board

board = ['']*10

display_board(board)
# player one's turn
(player1_marker,player2_marker)= player_input()
if player1_marker == 'X':
	turn = 'player 1'
else:
	turn = 'player 2'
while True:
	if turn == 'player 1':
		display_board(board)
		player_choice(board,player1_marker)
		if win_check(board,player1_marker) == True:
			print('player 1 won')
			break
		elif full_board(board) == True:
			print('this is a tie')
			break
		else:

			turn = 'player 2'
	if turn == 'player 2':
		display_board(board)
		player_choice(board,player2_marker)
		
		if win_check(board,player2_marker) == True:
			print("player 2 won")
			break
		elif full_board(board) == True:
			print('this is tie')
			break
		else:
			turn = 'player 1'
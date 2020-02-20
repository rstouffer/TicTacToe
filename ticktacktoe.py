
board=[[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']] 

def printBoard(): 
	print '\n\n'
	print ' +-----+-----+-----+'
	print ' | lt  | ct  | rt  |'
	print ' +-----+-----+-----+'
	print ' |     |     |     |'
	print ' |  ' + board[0][0] + '  |  ' + board[0][1] + '  |  ' + board[0][2] + '  |'
	print ' |     |     |     |'
	print ' +-----+-----+-----+'
	print ' | lm  | cm  | rm  |'
	print ' +-----+-----+-----+'
	print ' |     |     |     |'
	print ' |  ' + board[1][0] + '  |  ' + board[1][1]+ '  |  ' + board[1][2] + '  |'
	print ' |     |     |     |'
	print ' +-----+-----+-----+'
	print ' | lb  | cb  | rb  |'
	print ' +-----+-----+-----+'
	print ' |     |     |     |'
	print ' |  ' + board[2][0] + '  |  ' + board[2][1] + '  |  ' + board[2][2] + '  |'
	print ' |     |     |     |'
	print ' +-----+-----+-----+'
	print '\n'

def checkBoardForWin(player, cx1,cy1,cx2,cy2,cx3,cy3):
	if board[cy1][cx1] == player and board[cy2][cx2] == player and board[cy3][cx3] == player:
		board[cy1][cx1] = '*'
		board[cy2][cx2] = '*'
		board[cy3][cx3] = '*'

		return True
	else:
		return False

def checkBoardForWinStep1(player):
	if checkBoardForWin(player, 0,0,0,1,0,2) or checkBoardForWin(player, 1,0,1,1,1,2) or checkBoardForWin(player, 2,0,2,1,2,2) or checkBoardForWin(player, 0,0,1,0,2,0) or checkBoardForWin(player, 0,1,1,1,2,1) or checkBoardForWin(player, 0,2,1,2,2,2) or checkBoardForWin(player, 0,0,1,1,2,2) or checkBoardForWin(player, 0,2,1,1,2,0):
		return player
	else:
		for row in board:
			for col in row:
				if col == ' ':
					return ''
	return 'No one'

input=''

player = "X"

message = ''

while input != 'q' and input != 'quit':

	printBoard()

	input = raw_input(message + "Enter command player " + player + ":")

	message = ''

	cord=input.split(',')

	if (len(cord)==1 and len(input)>1):
		cord=[input[0:1], input[1:2]]

	if (cord[0] in ['t','m','b']):
		tmp=cord[0]
		cord[0]=cord[1]
		cord[1]=tmp

	if (len(cord) > 1) :

		x=-1
		y=-1

		if cord[0] == 'l':
			x=0
		elif cord[0] == 'c':
			x=1
		elif cord[0] == 'r':
			x=2
		else:
			message = 'Invalid command. '
			continue

		if cord[1]=='t':
			y=0
		elif cord[1]=='m':
			y=1
		elif cord[1]=='b':
			y=2
		else:
			message = 'Invalid command. '
			continue

		if board[y][x] == ' ':
			board[y][x] = player
		else:
			message = 'No cheating! '
			continue

		winplayer = checkBoardForWinStep1(player)
		
		if winplayer != '':
			printBoard()
			print winplayer + ' wins!' 
			board=[[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']] 
			player = 'X'
			continue
			
		if player=="X":
			player="O"
		else:
			player="X"
	else:
		message = 'Invalid command. '


# This Python file uses the following encoding: utf-8

import sys
import random

rows = 6
cols = 7
board = [[0 for col in xrange(cols)]for row in xrange(rows)]

testcase = [4,5,6,7,5,6,7,7,6,3,7]

characters = [" ","?","?"]

def show():
	for i in xrange(1,cols+1):
		sys.stdout.write(" "+str(i))
	print " "
	k = 0
	for i in board:
		print k,
		k +=1
		for j in i:
			#print "|",characters[j],
			sys.stdout.write("|" +characters[j])
		print "|"
	for i in xrange(1,cols+1):
		sys.stdout.write(" "+str(i))
	print " "


def dropcoin(col, player):
	if (col >= cols or col < 0):
		return False
	if (board[0][col] != 0):
		return False
	for row in xrange(rows):
		if (board[row][col]!=0):
			row -= 1
			break
			#checkwinner(row-1, col, player)
			#return True
	board[row][col] = player
	#print row,col
	checkwinner(row, col, player)
	return True


def checkwinner(row, col, player):
	#check up down
	coincount = 0
	for rowi in xrange(rows):
		if(board[rowi][col] == player):
			coincount += 1
		else:
			coincount = 0
		if(coincount >= 4):
			winner(player)
			return True
	#check horizontal
	coincount = 0
	for coli in xrange(cols):
		if(board[row][coli] == player):
			coincount += 1
		else:
			coincount = 0
		if(coincount >= 4):
			winner(player)
	#check diagonal
	coincount = 0
	if (row > col):
		coli = 0
		rowi = row - col
	elif (col > row):
		coli = col - row
		rowi = 0
	else:
		rowi = 0
		coli = 0
	try:
		while True:
			if (board[rowi][coli] == player):
				coincount += 1
			else:
				coincount = 0
			if(coincount >= 4):
				print "right diag"
				winner(player)
			coli +=1
			rowi +=1
	except IndexError:
		pass

	coincount = 0
	if (row > col):
		coli = 0
		rowi = row + col
	elif (col > row):
		coli = cols-col-1
		rowi = cols-col-1
	else:
		rowi = 0
		coli = cols-1
	try:
		while True:
			if (board[rowi][coli] == player):
				coincount += 1
			else:
				coincount = 0
			if(coincount >= 4):
				print "left diag"
				winner(player)
			coli -=1
			if (coli < 0):	#python arrays don't throw an exception with negative indexes
				break
			rowi +=1
	except IndexError:
		pass
	return False

def winner(player):
	show()
	print characters[player], "wins"
	sys.exit()
	
def spaces():
        for i in xrange(5):
                print

def main():
	player = 1
	c=2 
	r=0
	board[5+r][0+c] = player
	board[4+r][1+c] = player
	board[3+r][2+c] = player
	board[2+r][3+c] = player
	checkwinner(2+r,3+c,player)
	
	
	i = rows*cols
	while True:
		show()
		try:
			print "player",characters[player],"move:",
			#try:
			#	col = testcase[rows*cols-i]
			#	col -= 1
			#except :
			#	col = int(raw_input(""))-1
			col = int(raw_input(""))-1
			spaces()
			#col = random.randrange(0,cols,1)
			if not (dropcoin(col ,player)):
				print "no"
			else:
				i -= 1
				if (i == 0):
					show()
					print "everybody loses"
					break
				if (player == 1):
					player = 2
				else:
					player = 1
				print
		except ValueError:
			spaces()
			print "no"
	
main()



# This Python file uses the following encoding: utf-8

import sys
import random

rows = 6
cols = 7
board = [[0 for col in xrange(cols)]for row in xrange(rows)]

#characters = [" ","?","?"]
characters = [" ","o","x"]

def show():
	for i in xrange(1,cols+1):
		sys.stdout.write(" "+str(i))
	print " "
	#k = 0
	for i in board:
		#print k,
		#k +=1
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
	board[row][col] = player
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
			print "up down"
			winner(player)
			return True
	#check horizontal
	coincount = 0
	for coli in xrange(cols):
		#print "r",row,"c",coli
		if(board[row][coli] == player):
			coincount += 1
		else:
			coincount = 0
		if(coincount >= 4):
			print "horizontal"
			winner(player)
			return True
	#check diagonal
		
	coincount = 0
	rowi = row
	coli = col
	while True:
		if (rowi==0 or coli == 0):
			break
		rowi-=1
		coli-=1
	while True:
		if (board[rowi][coli] == player):
			coincount += 1
			#print "row:",rowi,"col:",coli
		else:
			coincount = 0
		if(coincount >= 4):
			print "right diag"
			winner(player)
			return True
		coli +=1
		rowi +=1
		if (coli > cols-1 or rowi > rows-1):	#python arrays don't throw an exception with negative indexes
			break
			
	coincount = 0
	rowi = row
	coli = col
	while True:
		if (rowi==0 or coli == (cols-1)):
			break
		rowi-=1
		coli+=1
	while True:
		if (board[rowi][coli] == player):
			coincount += 1
			#print "row:",rowi,"col:",coli
		else:
			coincount = 0
		if(coincount >= 4):
			print "left diag"
			winner(player)
			return True
		coli -=1
		rowi +=1
		if (coli < 0 or rowi >= rows or row < 0):	#python arrays don't throw an exception with negative indexes
			break
	
	return False

def winner(player):
	show()
	print characters[player], "wins"
	sys.exit()
	
def spaces():
        for i in xrange(5):
                print
def test(player):
	for c in xrange(0,cols-3):
		for r in xrange(0, rows-3):
			board[rows-4-r][0+c] = player
			board[rows-3-r][1+c] = player
			board[rows-2-r][2+c] = player
			board[rows-1-r][3+c] = player
			#show()
			if not checkwinner(rows-1-r,3+c,player):
				sys.exit()
			board[rows-4-r][0+c] = 0
			board[rows-3-r][1+c] = 0
			board[rows-2-r][2+c] = 0
			board[rows-1-r][3+c] = 0
			
def main():
	player = 1
	#test(player)
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
			#col = int(raw_input(""))-1
			spaces()
			col = random.randrange(0,cols,1)
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



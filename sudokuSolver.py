import sys
from collections import defaultdict
sys.setrecursionlimit(1500)
cantHaveValues = defaultdict(list)
trackList = dict()
tList = list()
# SampleBoards
# board1
# board = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
#          [5, 2, 0, 0, 0, 0, 0, 0, 0],
#          [0, 8, 7, 0, 0, 0, 0, 3, 1],
#          [0, 0, 3, 0, 1, 0, 0, 8, 0],
#          [9, 0, 0, 8, 6, 3, 0, 0, 5],
#          [0, 5, 0, 0, 9, 0, 6, 0, 0],
#          [1, 3, 0, 0, 0, 0, 2, 5, 0],
#          [0, 0, 0, 0, 0, 0, 0, 7, 4],
#          [0, 0, 5, 2, 0, 6, 3, 0, 0]]

#board2
board = [[0, 0, 0, 2, 6, 0, 7, 0, 1],
         [6, 8, 0, 0, 7, 0, 0, 9, 0],
         [1, 9, 0, 0, 0, 4, 5, 0, 0],
         [8, 2, 0, 1, 0, 0, 0, 4, 0],
         [0, 0, 4, 6, 0, 2, 9, 0, 0],
         [0, 5, 0, 0, 0, 3, 0, 2, 8],
         [0, 0, 9, 3, 0, 0, 0, 7, 4],
         [0, 4, 0, 0, 5, 0, 0, 3, 6],
         [7, 0, 3, 0, 1, 8, 0, 0, 0]]

def solveBoard(theBoard,cantHaveValues):

    for a in range(9):
        for b in range(9):
            
            if theBoard[a][b] == 0:
                val = checkConstraint(a,b,cantHaveValues,theBoard)
                if val:
                    theBoard[a][b] = val
                    trackList.update({(a,b) : theBoard[a][b] })
                    tList.append((a,b))
                else:
                    #Backtracking
                    endVal = tList.pop()
                    flag = trackList.pop(endVal)
                    
                    try:
                        cantHaveValues[(endVal[0],endVal[1])].append(flag)
                    except KeyError:
                        cantHaveValues.update({ (endVal[0],endVal[1]) : [flag] })
                    theBoard[endVal[0]][endVal[1]] = 0
                    solveBoard(theBoard,cantHaveValues)
    
def checkConstraint(a,b,cantHaveValues,theBoard):
    for num in range(1,10):
        
        if num in cantHaveValues[(a,b)]: continue
        
        if num in theBoard[a]: continue #checking for rows
        
        if num in ([board[x][b] for x in range(9)]): continue #checking for columns
        
        #checking for n * n boxes
        if (a >= 0 and a <= 2):
            if (b >= 0 and b <= 2):
                if num in ([ theBoard[x][y] for x in range(0,3) for y in range(0,3)]): continue
            if (b >= 3 and b <= 5):
                if num in ([ theBoard[x][y] for x in range(0,3) for y in range(3,6)]): continue
            if (b >= 6 and b <= 8):
                if num in ([ theBoard[x][y] for x in range(0,3) for y in range(6,9)]): continue
        if (a >=3 and a <= 5):
            if (b >= 0 and b <= 2):
                if num in ([ theBoard[x][y] for x in range(3,6) for y in range(0,3)]): continue
            if (b >= 3 and b <= 5):
                if num in ([ theBoard[x][y] for x in range(3,6) for y in range(3,6)]): continue
            if (b >= 6 and b <= 8):
                if num in ([ theBoard[x][y] for x in range(3,6) for y in range(6,9)]): continue
            
        if (a >=6 and a <= 8):
            if (b >= 0 and b <= 2):
                if num in ([ theBoard[x][y] for x in range(6,9) for y in range(0,3)]): continue
            if (b >= 3 and b <= 5):
                if num in ([ theBoard[x][y] for x in range(6,9) for y in range(3,6)]): continue
            if (b >= 6 and b <= 8):
                if num in ([ theBoard[x][y] for x in range(6,9) for y in range(6,9)]): continue
        
        return num
    
    cantHaveValues.update({(a,b) : []})
    return False
        


solveBoard(board,cantHaveValues)
print('solvedSudoku')
for a in board:
    print(a)



    
    
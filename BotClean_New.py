#!/usr/bin/python

# Head ends here

def next_move(posr, posc, board):
    print("")
    """
    dirt_row, dirt_col = [],[]
    distance = []
    closest = []
    for i in board:
        #print("Row :",board.index(i))
        for n, j in enumerate(i):
            if j == 'd':
                print('Dirt:', board.index(i), n)
                dirt_row.append(board.index(i))
                dirt_col.append(n)
    for i in range(len(dirt_row)):
        distance.append(((posr - dirt_row[i] + posc - dirt_col[i]))*-1)
        closest.append(i)
        #print(distance,closest )

    print(distance.index(min(distance)))#,':', closest)
    """
    i, j = min(((i, j) for i, row in enumerate(board) if 'd' in row for j, c in enumerate(row) if c == 'd'), key=lambda x: abs(posr - x[0]) + abs(posc - x[1]))
    print("LEFT" if j < posc else "RIGHT" if j > posc else "UP" if i < posr else "DOWN" if i > posr else "CLEAN")
    
    

        
# Tail starts here

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    #board = [[j for j in input().strip()] for i in range(5)]
    #print(board)
    board = [['b', '-', '-', '-', 'd'], ['-', 'd', '-', '-', 'd'], ['-', '-', 'd', 'd', '-'], ['-', '-', 'd', '-', '-'], ['-', '-', '-', '-', 'd']]
    next_move(pos[0], pos[1], board)

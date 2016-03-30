import random


# Size of board, and useful range to iterate
size = 3
r = range(0, size)


# Players
players = ('X', 'O')


# Return a valid point from user input
def GetPos():
    while True:
        i = raw_input().split(',')
        if len(i) != 2:
            print "Please enter position like so: 1,2"
            continue

        try:
            x = int(i[0])
            y = int(i[1])
        except ValueError:
            print "Please enter position as two integers: 0,1"
            continue

        if x not in r:
            print "First number must be between 0 and 2"
            continue

        if y not in r:
            print "Second number must be between 0 and 2"
            continue

        return x,y


# Is this position a draw? Assumes already tested for wins
def IsDraw(board):
    return len(board) == size * size


# List of all possible lines
lines = [[(x,y) for x in r] for y in r] + [[(x,y) for y in r] for x in r]
lines += [[(x,x) for x in r]] + [[(x, size - x - 1) for x in r]]


# Is this board a win for c where c is 'X' or 'O'
def HasWon(board, c):
    return any(all(p in board and board[p] == c for p in l) for l in lines)


# Print out this board
def PrintBoard(board):
    for x in r:
        print "".join(board[x,y] if (x,y) in board else ' ' for y in r)


# Test to see result of this move, doing tree search
def TestMove(board, point, c):
    board[point] = c
    if HasWon(board, c):
        result = 1
    elif IsDraw(board):
        result = 0
    else:
        result = -FindMove(board, "".join(filter(lambda x: x != c, players)))[1]
    board.pop(point)
    return result


# Look for possible moves and test them. Return move,score
def FindMove(board, c):
    score = -1
    moves = []

    for p in [(x,y) for x in r for y in r]:
        if p in board:
            continue
        newScore = TestMove(board, p, c)
        if newScore < score:
            continue

        if newScore > score:
            score = newScore
            moves = []

        moves.append(p)

    return random.choice(moves), score

play = {c:raw_input("Play %c (y/n)?" % c).upper() == "Y" for c in players}
board = {}

while True:
    for c in players:
        if play[c]:
            print "Enter move for %c:" % c
            while True:
                p = GetPos()
                if p in board:
                    print "Position not free"
                    continue
                board[p] = c
                break
        else:
            print "Thinking ..."
            board[FindMove(board, c)[0]] = c
        PrintBoard(board)

        if HasWon(board, c):
            print c + " won!"
            quit()

        if IsDraw(board):
            print "Draw!"
            quit()

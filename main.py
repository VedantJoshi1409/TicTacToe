def evaluate(board, player):
    win_positions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8], [2, 4, 6], [0, 3, 6], [1, 4, 7], [2, 5, 8]]
    enemy = (player + 1) % 2
    for i in range(0, len(win_positions)):
        line_not_broken = True
        enemy_line_not_broken = True
        for j in range(0, len(win_positions[i])):
            if line_not_broken and board[win_positions[i][j]] != player:
                line_not_broken = False
            if enemy_line_not_broken and board[win_positions[i][j]] != enemy:
                enemy_line_not_broken = False
        if enemy_line_not_broken:
            return -99
        if line_not_broken:
            return 99
    return 0


def getMoves(board):
    moves = []
    for i in range(0, len(board)):
        if board[i] == -1:
            moves.append(i)
    return moves


def makeMove(board, move, player):
    board[move] = player
    return board


def miniMax(board, player, ply):
    score = evaluate(board, player)
    if score != 0:
        return score - ply

    moves = getMoves(board)
    if len(moves) != 0:
        maxScore = 0
        for i in range(0, len(moves)):
            newBoard = makeMove(board.copy(), moves[i], player)
            score = -miniMax(newBoard, (player + 1) % 2, ply + 1)
            maxScore = max(score, maxScore)
        return maxScore - ply
    return 0


def engineMove(board, player):
    moves = getMoves(board)
    maxScore = -999
    bestMove = moves[0]
    for i in range(0, len(moves)):
        newBoard = makeMove(board.copy(), moves[i], player)
        score = -miniMax(newBoard, (player + 1) % 2, 0)
        if score > maxScore:
            bestMove = moves[i]
            maxScore = score
    return makeMove(board, bestMove, player)


def printBoard(board):
    letters = [" ", "X", "O"]
    print(letters[board[0] + 1], "|", letters[board[1] + 1], "|", letters[board[2] + 1])
    print("---------")
    print(letters[board[3] + 1], "|", letters[board[4] + 1], "|", letters[board[5] + 1])
    print("---------")
    print(letters[board[6] + 1], "|", letters[board[7] + 1], "|", letters[board[8] + 1])


def main():
    board = [-1, -1, -1, -1, -1, -1, -1, -1, -1]
    player = 0
    human = 0  # 0 if human goes first, 1 if computer goes first

    while len(getMoves(board)) != 0 and evaluate(board, player) == 0:
        printBoard(board)
        print()
        if player == human:
            move = -1
            moves = getMoves(board)
            while move not in moves:
                move = int(input("Enter move ")) - 1
                if move in moves:
                    board = makeMove(board, move, player)
                else:
                    print("Invalid")
        else:
            engineMove(board, player)
        player = (player + 1) % 2
    printBoard(board)
    score = evaluate(board, human)
    if score > 0:
        print("YOU WIN")
    elif score < 0:
        print("YOU Lose")
    else:
        print("DRAW")


main()

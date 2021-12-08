def task1(): 
  with open(inputFile) as f:
    board = None
    boards = []
    sequence = []

    for i, line in enumerate(f.readlines()):
      if i == 0: 
        sequence = [ int(n) for n in line[:-1].split(',') ]
        continue

      line = line[:-1].replace("  ", " ")

      if line == '':
        if board != None: boards.append(board)
        board = []
        continue
      else:
        if line[0] == ' ': line = line[1:]
        line = [int(str) for str in line.split(' ')]
        board += line
    
    boards.append(board)

    last_sum = None
    # loop all target number in sequence
    for target in sequence:
      boards = [ [( -1000 if ((num >= 0) and (num == target)) else num ) for num in board] for board in boards ]
      
      winningBoards = checkBoardsWin(boards, target)
      this_last_sum = None
      for boardIndex in sorted(winningBoards.keys(), reverse=True):
        temp_sum = winningBoards[boardIndex]
        print(boardIndex, temp_sum)
        if this_last_sum is None: this_last_sum = temp_sum
        del boards[boardIndex]

      if len(winningBoards) > 0: last_sum = this_last_sum

    return last_sum

def checkBoardsWin(boards, target, boardLength = 5):
  winningBoards = {}
  for k, board in enumerate(boards):
    for i in range(boardLength):
      checkingLines = [
        board[i*5:(i+1)*5], # horizontal
        list(map(lambda j: board[j*5 + i], list(range(boardLength)))), # veritcal
      ]

      for line in checkingLines:
        lineWinScore = checkLineWin(line, board, target, k)
        if lineWinScore: 
          winningBoards[k] = lineWinScore
      
  return winningBoards

def checkLineWin(line, board, target, k):
  if all(map(lambda n: n == -1000, line)):
    s = sum(map(lambda n: n if n > 0 else 0, board))
    return target * s
  return None 

def printBoard(board):
  for i in range(5):
    print(board[i*5:(i+1)*5])

if __name__ == "__main__":
  inputFile = 'source/day4.txt'
  print(task1())
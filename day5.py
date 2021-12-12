class solution:

  def task(inputFile): 
    veryDangerous = set()
    danger = {}

    def addToDanger(k):
      if k not in danger:
        danger[k] = 1
      else:
        danger[k] += 1
        veryDangerous.add(k)

    def loopLine(fr, to, keyName):
      # swap if not in order
      fr, to = solution.swap(fr, to)
      # record each coord in the line
      for temp in range(fr, to + 1):
        k = keyName(temp)
        addToDanger(k)

    with open(inputFile) as f:
      for i, line in enumerate(f.readlines()):
        fromCoord, toCoord = line[:-1].split(" -> ")
        fromX, fromY = fromCoord.split(',')
        toX, toY = toCoord.split(',')
        fromX, fromY, toX, toY = int(fromX), int(fromY), int(toX), int(toY)

        # vertical
        if fromX == toX:
          loopLine(fromY, toY, lambda tempY: f"{fromX}:{tempY}")
        # vertical
        elif fromY == toY:
          loopLine(fromX, toX, lambda tempX: f"{tempX}:{fromY}")
        # diagonals
        else: 
          tempX, tempY = fromX, fromY
          while tempX != toX:
            k = f"{tempX}:{tempY}"
            addToDanger(k)
            tempX += 1 if toX > fromX else -1
            tempY += 1 if toY > fromY else -1
          assert tempY == toY, str((fromX, tempX, toX, fromY, tempY, toY))
          k = f"{toX}:{toY}"
          addToDanger(k)

    return len(veryDangerous)

  def swap(fr, to):
    if fr > to: 
      temp = fr
      fr = to
      to = temp
    return fr, to

if __name__ == "__main__":
  inputFile = 'source/day5.txt'
  print(solution.task(inputFile))
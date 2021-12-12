class solution:

  def task1(inputFile): 
    veryDangerous = set()
    danger = {}
    def loopLine(fr, to, keyName):
      # swap if not in order
      if fr > to: 
        temp = fr
        fr = to
        to = temp

      # record each coord in the line
      for temp in range(fr, to + 1):
        k = keyName(temp)
        if k not in danger:
          danger[k] = 1
        else:
          danger[k] += 1
          veryDangerous.add(k)

    with open(inputFile) as f:
      for i, line in enumerate(f.readlines()):
        fromCoord, toCoord = line[:-1].split(" -> ")
        fromX, fromY = fromCoord.split(',')
        toX, toY = toCoord.split(',')
        fromX, fromY, toX, toY = int(fromX), int(fromY), int(toX), int(toY)

        # ignore diagonals
        if fromX != toX and fromY != toY: continue

        # vertical
        if fromX == toX:
          loopLine(fromY, toY, lambda tempY: f"{fromX}:{tempY}")
        # vertical
        elif fromY == toY:
          loopLine(fromX, toX, lambda tempX: f"{tempX}:{fromY}")

    return len(veryDangerous)


if __name__ == "__main__":
  inputFile = 'source/day5.txt'
  print(solution.task1(inputFile))
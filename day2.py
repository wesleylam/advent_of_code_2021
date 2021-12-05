inputFile = 'source/day2.txt'
with open(inputFile) as f:
  horizontal = 0
  depth = 0
  aim = 0

  for line in f.readlines():
    tokens = line[:-1].split(' ')
    assert len(tokens) == 2, f"only command and length allowed: {line}"
    com, length = tokens
    length = int(length)
    if com == "forward":
      horizontal += length
      depth += length * aim
    elif com == "down":
      aim += length
    elif com == "up":
      aim -= length
    else: 
      raise Exception("Unknown command")
    
    
  print(f"horizontal: {horizontal}")
  print(f"depth: {depth}")
  print(f"Product: {depth * horizontal}")
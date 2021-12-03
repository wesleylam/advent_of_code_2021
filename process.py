inputFile = 'input.txt'

with open(inputFile) as f:
  incCount = -1
  decCount = 0
  prev = -1
  for line in f.readlines():
    num = int(line[:-1])
    print(num)
    if num > prev:
      incCount += 1
    elif num < prev:
      decCount += 1
    else:
      raise Exception("Should this happen?")
    prev = num
    
print("Increased:", incCount)
print("Decreased:", decCount)
inputFile = 'source/day1.txt'
with open(inputFile) as f:
  slidingWindow = []
  incCount = 0
  decCount = 0
  eqCount = 0
  for i, line in enumerate(f.readlines()):
    num = int(line[:-1])
    
    if i == 2: # set the first sum
      prev = sum(slidingWindow)
    
    if i >= 3: # start comparing there are 2 groups with 3 elements
      # update sliding window and calculate
      slidingWindow.pop(0)
      slidingWindow.append(num)
      currentSum = sum(slidingWindow)
      
      # Compare
      if currentSum > prev:
        incCount += 1
      elif currentSum < prev:
        decCount += 1
      else:
        eqCount += 1
    
      prev = currentSum
    else:
      slidingWindow.append(num)

print("Increased:", incCount)
print("Decreased:", decCount)
print("No Change:", eqCount)
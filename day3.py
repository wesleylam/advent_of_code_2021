inputFile = 'source/day3.txt'
with open(inputFile) as f:
  counter = []
  for line in f.readlines():
    line = line[:-1]
    # init
    if counter == []:
      bitstringLength = len(line)
      counter = [ 0 for i in range(bitstringLength) ]
    
    # loop every bit
    for i, char in enumerate(line):
      counter[i] += 1 if char == '1' else -1

  # find bit by bit for the rates, and convert to decimal
  gammaRateBitString = ""
  gammaRate = 0
  epsilonRateBitString = ""
  epsilonRate = 0
  print(counter)
  for i, c in enumerate(counter):
    exponent = bitstringLength - 1 - i
    if c > 0:
      gammaRateBitString += "1"
      gammaRate += 2 ** exponent
      epsilonRateBitString += "0"
    elif c < 0:
      gammaRateBitString += "0"
      epsilonRateBitString += "1"
      epsilonRate += 2 ** exponent
    else:
      raise Exception("No most common bit")

  # results
  print("gammaRateBitString: ", gammaRateBitString, gammaRate)
  print("epsilonRateBitString: ", epsilonRateBitString, epsilonRate)
  print("Product: ", gammaRate * epsilonRate)
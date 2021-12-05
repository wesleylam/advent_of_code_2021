inputFile = 'source/day3.txt'
def task1(): 
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

def task2():
  match = []
  with open(inputFile) as f:
    for line in f.readlines():
      line = line[:-1]
      match.append(line)

  o2Rate = findMatch(match, True)
  co2Rate = findMatch(match, False)
  print(o2Rate)
  print(co2Rate)
  print(o2Rate * co2Rate)

# loop each num, find match with most common or least common accordingly
def findMatch(match, keepCommon = True):
  i = 0
  while len(match) > 1:
    count = 0
    submatch1 = []
    submatch0 = []
    for num in match:
      if num[i] == '1':
        count += 1  
        submatch1.append(num)
      else:
        count -= 1
        submatch0.append(num)

    if count > 0: 
      match = submatch1 if keepCommon else submatch0
    elif count < 0: 
      match = submatch0 if keepCommon else submatch1
    else:
      match = submatch1 if keepCommon else submatch0
    i += 1

  # binary to decimal
  length = len(match[0])
  num = 0
  for i, char in enumerate(match[0]):
    exponent = length - i - 1
    if char == '1': num += 2 ** exponent
  return num

if __name__ == "__main__":
  task2()
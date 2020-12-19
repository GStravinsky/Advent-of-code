import itertools

data = open("data.txt")
data = data.read()

data = data.split("\n")
data = data[:-1]
data = [int(i) for i in data]

def number_is_valid(number, preamble):
 #preamble - list of 25 digits
 # 26th number
  
  tuples = itertools.combinations(preamble,2)
  result = [True for i in tuples if sum(i) == number]

  return number, len(result) >= 1


#i = 0
#result = True
#while result == True:
#  preamble = data[0+i:25+i]
#  number = data[25+i]
  
#  checked_number, result = number_is_valid(number, preamble)
  
#  print(checked_number, result) 
#  i += 1


### Part 2

# get data up to a number above

subdata = data[:data.index(29221323)+1]

def find_the_block(data):
  number = 29221323
  lower = 0
  summed = 0
  while summed != number:
    print("Block moved")
    summed = 0
    i = 1
    while summed < number:
      if lower+i > len(data):
        print("Shit")
        return 
      print("Lower", lower,"Upper", lower+i)
      summed = sum(data[lower:lower+i])
      i += 1
    print(summed)
    if summed == number:
      print("Found it")
      return data[lower:lower+i-1]
    lower += 1

theblock = find_the_block(data)

print (min(theblock)+max(theblock))



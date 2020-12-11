data = open("data.txt")
data = data.read()

data = data.split('\n')


# Base functions

def acc_do(acc, number, index):
    # number - the [4:] of the i in data - just the number part
    # acc - most recent acc value
    # index = which index is being querried
    value = int(number[1:])
    sign = number[0]
    if sign == "+":
        acc += value
    else:
        acc -=value
    index += 1
    return acc, index


def jmp_do(number, index):
    value = int(number[1:])
    sign = number[0]
    if sign == "+":
        index += value
    else:
        index -= value

    return index

def nop_do(index):
    index += 1
    return index

def command_parser(command_line):
    number = command_line[4:]
    command = command_line[:3]
    return command, number
    
def count_duplicates(sequence_of_indices):
    # takes the list of indices visited
    return len(sequence_of_indices) - len(set(sequence_of_indices))

def calc_acc_one_loop(data):
    indices = []
    no_duplicates = 0
    index = 0
    acc = 0
    while no_duplicates <=1:
      command, number = command_parser(data[index])
      if command == "acc":
        acc, index = acc_do(acc, number, index)

      elif command == "jmp":
        index = jmp_do(number, index)
    
      elif command == "nop":
        index = nop_do(index)
      
      indices.append(index)       
      no_duplicates = count_duplicates(indices)
      print(acc, no_duplicates, index)
    return acc, no_duplicates

def jmp_to_nop(data, index):
  data[index] = "nop%s" %data[index][3:] 
  return data

### PART 2 ###

def islastcommand642(data):
    data.append("")
    index = 0
    acc = 0
    no_duplicates = 0
    indices = []
    while index <= 642 and no_duplicates == 0:

      command, number = command_parser(data[index])
      if command == "acc":
        acc, index = acc_do(acc, number, index)
      elif command == "jmp":
        index = jmp_do(number, index)
    
      elif command == "nop":
        index = nop_do(index)
      indices.append(index)
      no_duplicates = count_duplicates(indices)
    return acc, index
    
     
def nop_to_jmp(data, index):
    data[index] = "jmp%s" %data[index][3:]
    return data
def fix_loop(data):
  acc = 0
  for i in range(10):
    print("index", i)
    print("acc", acc)
    command, number = command_parser(data[i])
    print(command, number)
    if command == "nop":
        data2 = nop_to_jmp(data,i)
        print(data2[:10])
        print("Adjusted string", data2[i])
        acc, index = islastcommand642(data2)
        if index == 642:
         print("This one", index, acc)
    
  return acc

print(fix_loop(data))

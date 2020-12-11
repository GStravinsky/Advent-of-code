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
    while no_duplicates == 0:
      command, number = command_parser(data[index])
      if command == "acc":
        acc, index = acc_do(acc, number, index)

      elif command == "jmp":
        index = jmp_do(number, index)
    
      elif command == "nop":
        index = nop_do(index)
      
      indices.append(index)       
      no_duplicates = count_duplicates(indices)
    print(acc)     
    return acc, no_duplicates

def jmp_to_nop(data, index):
  data[index] = "nop%s" %data[index][3:] 
  return data

 
print(len(data)) 
def fix_loop(data):
  acc = 0
  for i in range(len(data)):
    print(acc)
    command, number = command_parser(data[i])
    print(command, number)
    if command == "jmp":
       data = jmp_to_nop(data,i)
       acc, no_duplicates = calc_acc_one_loop(data)
       if no_duplicates == 0:
        break
  return acc, i

data2 = jmp_to_nop(data,3)
print(data2[3])
print(calc_acc_one_loop(data2))

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
    return len(sequence_of_indices) - list(set(sequence_of_indices))

def calc_acc_one_loop():
    indices = []




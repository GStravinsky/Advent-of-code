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
    
print(acc_do(10, data[0][4:], 0))

print(jmp_do(data[1][4:], 1))

print(nop_do(2))

print(command_parser(data[0]))

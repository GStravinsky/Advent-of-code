

input = open("input.txt")
input = input.read()
input = input.split("\n")

remainder = set([ 2020 - int(x) for x in input ])
nums = set([int(x) for x in input])

same = nums.intersection(remainder)
print(same)
print(list(same)[0] * list(same)[1])

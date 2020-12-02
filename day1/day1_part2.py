import itertools

input = open("input.txt")
input = input.read()
input = input.split("\n")

nums = [int(x) for x in input]

for n1, n2 in itertools.combinations(nums, 2):
    semi_sum = n1 + n2
    remainder = 2020 - semi_sum 
    if remainder in nums:
        print(n1, n2, 2020 - semi_sum)
        print("Product", n1 * n2 * (2020 - semi_sum))
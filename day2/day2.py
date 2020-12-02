import pandas as pd
import numpy as np

input = pd.read_csv('input.txt', sep=" ", header=None)
input.columns = ["Policy", "Letter", "Password"]

input["Letter"] = input["Letter"].str.replace(':','')
input[["Min", "Max"]] = input["Policy"].str.split('-', expand=True)

data = input.to_numpy()

# valid_passwords = 0

# for i in range(len(input)):
#     password = input.loc[i, "Password"]
#     count = password.count(input.loc[i, "Letter"])
#     minimum = int(input.loc[i, "Min"])
#     maximum = int(input.loc[i, "Max"])
#     if count >= minimum and count <= maximum:
#         valid_passwords += 1

# print(valid_passwords)
 
def isvalid(line):
    password = line[2]
    count = password.count(line[1])
    minimum = int(line[3])
    maximum = int(line[4])

    return count >= minimum and count <= maximum

valids = len([x for x in data if isvalid(x)])

print(valids)
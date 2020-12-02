import pandas as pd

input = pd.read_csv('input.txt', sep=" ", header=None)
input.columns = ["Policy", "Letter", "Password"]

input["Letter"] = input["Letter"].str.replace(':','')
input[["Loc1", "Loc2"]] = input["Policy"].str.split('-', expand=True)
print(input)

valid_password = 0
for i in range(len(input)):
    # case 1: first position has it - second does not
    # case 2: first does not, second does
    # case 3: no one does
    # case 4 : both do

    password = input.loc[i, "Password"]
    letter = input.loc[i, "Letter"]
    lc1 = int(input.loc[i, "Loc1"]) - 1
    lc2 = int(input.loc[i, "Loc2"]) - 1

    if password[lc1] == letter and password[lc2] != letter:
        valid_password += 1
    elif password[lc1] != letter and password[lc2] == letter:
        valid_password += 1

print(valid_password)

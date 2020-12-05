import numpy as np
import re

data = open("data.txt")
data = data.read()
data = data.split('\n\n')

for p in range(len(data)):
  data[p] = re.split('\n| ', data[p])

def isvalid(person):
  cleaned = [x[:3] for x in person]
  
  must_have = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
 
  has_all_keys = True
  for key in must_have:
    has_all_keys &= key in cleaned
  return has_all_keys


no_valid = sum([int(isvalid(x)) for x in data])

print(no_valid)

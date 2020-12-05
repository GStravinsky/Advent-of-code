import re

data = open("data.txt")
data = data.read()
data = data.split('\n\n')

for p in range(len(data)):
  data[p] = re.split('\n| ', data[p])

def convert_dic(lst):

  my_dict = {elem[:3]: elem[4:] for elem in lst}
  return my_dict

data_n = [convert_dic(x) for x in data]

def isvalid(person):
  keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

  

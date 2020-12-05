data = open("data.txt")
data = data.read()
data = data.split('\n')

data2 = [ x.replace('B','1').replace('R','1').replace('F','0').replace('L','0') for x in data]

import numpy as np
sort_bin = np.sort(data2)

ID = int(sort_bin[-1],2)

###  PART 2 ####

ID = [int(x,2) for x in sort_bin]
print(ID[:3])


def neighbours(seat):
  has_both = (seat + 1) in ID and (seat-1) in ID

  return has_both


lonely_boys = [x for x in ID if not neighbours(x)]

print(lonely_boys)


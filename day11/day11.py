data = open("data.txt")
data = data.read()
data = data.split("\n")

import numpy as np
from collections import Counter

data = np.array(data)

data2 = np.empty((90,92), dtype=object)

# first itteration would just make all the seats occupied
# defines occupied seat as 1, empty as 0
for r in range(len(data)):
    data2[r] = [1 if i == "L" else "." for i in data[r]]

def summarise_neighbours(data, row, column):
    neighbours = []
    if row == 0 and column == 0:
        neighbours.append(data[row,column+1])
        neighbours.append(data[row+1,column+1])
        neighbours.append(data[row+1,column])
    elif row == 0 and column != 0 and column != (np.shape(data)[1]-1):
        neighbours.append(data[row,column+1])
        neighbours.append(data[row+1,column+1])
        neighbours.append(data[row+1,column])
        neighbours.append(data[row-1,column-1])
        neighbours.append(data[row-1,column])
    elif row == 0 and column == (np.shape(data)[1]-1):
        neighbours.append(data[row,column-1])
        neighbours.append(data[row+1,column-1])
        neighbours.append(data[row+1,column])
    elif row != 0 and row != (np.shape(data)[0]-1) and column == 0:
        neighbours.append(data[row-1,column])
        neighbours.append(data[row-1,column+1])
        neighbours.append(data[row,column+1])
        neighbours.append(data[row+1,column+1])
        neighbours.append(data[row+1,column])
    elif row !=0 and row != (np.shape(data)[0]-1) and column == (np.shape(data)[1]-1):
        neighbours.append(data[row+1,column])
        neighbours.append(data[row+1,column-1])
        neighbours.append(data[row,column-1])
        neighbours.append(data[row-1,column-1])
        neighbours.append(data[row-1,column])
    elif row == (np.shape(data)[0]-1) and column == 0:
        neighbours.append(data[row-1,column])
        neighbours.append(data[row-1,column+1])
        neighbours.append(data[row,column+1])
    elif row == (np.shape(data)[0]-1) and column != 0 and column != (np.shape(data)[1]-1):
        neighbours.append(data[row,column-1])
        neighbours.append(data[row-1,column-1])
        neighbours.append(data[row-1,column])
        neighbours.append(data[row-1,column+1])
        neighbours.append(data[row,column+1])
    elif row == (np.shape(data)[0]-1) and column == (np.shape(data)[1]-1):
        neighbours.append(data[row,column-1])
        neighbours.append(data[row-1,column-1])
        neighbours.append(data[row-1,column])
    else:
        neighbours.append(data[row,column+1])
        neighbours.append(data[row+1,column+1])
        neighbours.append(data[row+1,column])
        neighbours.append(data[row+1,column-1])
        neighbours.append(data[row,column-1])
        neighbours.append(data[row-1,column-1])
        neighbours.append(data[row-1,column])
        neighbours.append(data[row-1,column+1])
    count_neighbours = Counter(neighbours)
    return count_neighbours[1]


def one_iteration(data):
    data_new = np.copy(data)
    for row_n, row in enumerate(data):
      for column_n, column in enumerate(row):
        # if the seat is empty and has no neighbours - it becomes occupied
        count = summarise_neighbours(data,row_n,column_n)
        if column == 0 and count == 0:
            data_new[row_n,column_n] = 1
        # if the seat is occupied and has more or exactly 4 neighbours - it becomes empty
        elif column == 1 and count >= 4:
          data_new[row_n,column_n] = 0
    count = np.count_nonzero(data_new == 1)
    return data_new, count


  
def all_iterations(data):
  # setting dummy values
  count = 0
  diff = 1
  while diff  != 0:
    data_new, count_new = one_iteration(data)
    diff = count-count_new
    count = count_new
    print(count)
    data = np.copy(data_new)
  return(count)

print(all_iterations(data2))
 
## if column == 'L" and the count==0 column == Occupies

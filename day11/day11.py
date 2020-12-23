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

print(data2)
def summarise_neighbours(data, row, column):
    neighbours = []
    if row == 0 and column == 0:
        neighbours.append(data[row,column+1])
        neighbours.append(data[row+1,column+1])
        neighbours.append(data[row+1,column])
    elif row == 0 and column > 0 and column < (np.shape(data2)[1]-1):
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
    elif row !=0 and column == (np.shape(data)[1]-1):
        neighbours.append(data[row+1,column])
        neighbours.append(data[row+1,column-1])
        neighbours.append(data[row,column-1])
        neighbours.append(data[row-1,column-1])
        neighbours.append(data[row-1,column])
    elif row == (np.shape(data)[0]-1) and column == 0:
        neighbours.append(data[row-1,column])
        neighbours.append(data[row-1,column+1])
        neighbours.append(data[row,column+1])
    elif row == (np.shape(data)[0]-1) and column != 0:
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

print(summarise_neighbours(data2,0,4))

def one_iteration(data):
    data_new = data
    for row_n, row in enumerate(data_new):
      for column_n, column in enumerate(row):
        # if the seat is empty and has no neighbours - it becomes occupied
        if column == 0 and summarise_neighbours(data_new, row_n, column_n) == 0:
            data_new[row_n,column_n] == 1
        # if the seat is occupied and has more or exactly 4 neighbours - it becomes empty
        elif column == 1 and summarise_neighbours(data_new, row_n, column_n) >= 4:
            data_new[row_n,column_n] == 0
    return data_new

print(one_iteration(data2))



## if column == 'L" and the count==0 column == Occupies
## if column =="Occupied" and the count>=4 column == L
## if column == ., skip. 
# make sure you do the changes on a NEW MAP 

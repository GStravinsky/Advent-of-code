data = open("data.txt")
data = data.read()
data = data.split("\n")

import numpy as np

data = np.array(data)

data2 = np.empty((90,92), dtype=object)

for r in range(len(data)):
    data2[r] = [i for i in data[r]]

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
    elif row != 0 and column == 0:
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
    return neighbours

print(summarise_neighbours(data2,0,4))

for row_n, row in enumerate(data2[:2]):
    count = [summarise_neighbours(data2,row_n,column_no) for column_no, column in enumerate(row) if column == "L"]
    print(len(count))
       

## if column == 'L" and the count==0 column == Occupies
## if column =="Occupied" and the count>=4 column == L
## if column == ., skip. 
# make sure you do the changes on a NEW MAP 

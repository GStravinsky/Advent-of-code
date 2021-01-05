data = open("data.txt")
data = data.read()
data = data.split("\n")
import numpy as np

data = np.array(data)
data2 = np.empty((np.shape(data)[0], len(data[1])), dtype=object)

# first itteration would just make all the seats occupied
# defines occupied seat as 1, empty as 0
for r in range(len(data)):
    data2[r] = [1 if i == "L" else "." for i in data[r]]

## Attempt 2 to get all 8 neighbours and go along the line if needed

def get_relevant_neighbours(data, row, column):
    row_no = np.shape(data)[0] - 1
    column_no = np.shape(data)[1] - 1
    neighbours = 0 

    for row_offset in range(-1,2):
        for column_offset in range(-1,2):
            x = row + row_offset
            y = column + column_offset
            # skip the centre itself
            if x == row and y == column:
                continue
            
            while True:
                if (x > row_no or y > column_no or x < 0 or y < 0):
                    break
                tile = data[x,y]
                if tile == 1:
                    neighbours += 1
                    break
                elif tile == 0:
                    break
                elif tile == ".":
                    x += row_offset
                    y += column_offset
    return neighbours
                
def one_iteration(data):
    data_new = np.copy(data)
    for row_n, row in enumerate(data):
      for column_n, column in enumerate(row):
        # if the seat is empty and has no neighbours - it becomes occupied
        count = get_relevant_neighbours(data,row_n,column_n)
        if column == 0 and count == 0:
            data_new[row_n,column_n] = 1
        # if the seat is occupied and has more or exactly 4 neighbours - it becomes empty
        elif column == 1 and count >= 5:
          data_new[row_n,column_n] = 0
    count = np.count_nonzero(data_new == 1)
    return data_new, count

def all_iterations(data):
  # setting dummy values
  count = 0 
  diff = 1
  while diff != 0:
    data_new, count_new = one_iteration(data)
    diff = count-count_new
    count = count_new
    print(count)
    data = np.copy(data_new)
  return count

print(all_iterations(data2))


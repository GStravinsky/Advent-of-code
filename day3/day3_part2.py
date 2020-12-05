import numpy as np

map = open("map.txt")
map = map.read()

map = np.array(list(map))

binary = np.where(map==".", 0, map)
binary = np.where(binary=="#", 1, binary)

parsed = np.reshape(binary, (323,32))

parsed = parsed[:,:31].astype(int)

def trees(data, steps):
  vert = steps[1]
  horz = steps[0]
  expansion = 323
  big = np.hstack([data]*expansion)
  moves = int(322/vert)
  
  ver_start = 0
  hor_start = 0
  symbol = 0
  for i in range(moves):
    hor_start += horz
    ver_start += vert
    symbol += big[ver_start,hor_start]
   
  return symbol

steps = [ [1,1], [3,1], [5,1], [7,1], [1,2] ]

total = np.prod([trees(parsed, x) for x in steps])
print(total) 

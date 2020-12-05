import numpy as np

map = open("map.txt")
map = map.read()

map = np.array(list(map))

binary = np.where(map==".", 0, map)
binary = np.where(binary=="#", 1, binary)

parsed = np.reshape(binary, (323,32))

parsed = parsed[:,:31].astype(int)

big = np.hstack([parsed]*33)

horizontal = 0
vertical = 0
symbol = 0
for i in range(322):
  horizontal += 3
  vertical += 1
  symbol += big[vertical,horizontal]

print(symbol)

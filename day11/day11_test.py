import numpy as np

data_2061 = np.load("data_2061.npy", allow_pickle=True)
data_2291 = np.load("data_2291.npy", allow_pickle=True)

print(np.where(data_2061 != data_2291))

print(data_2061[6:25,65:74])
print(data_2291[6:25,65:74])

data = open("data.txt")                                                              
data = data.read()                                                                   
data = data.split('\n\n')


print(data[-1])
### PART 2 #####

def all_yes(group):
  parsed = group.split('\n')

  parsed = [p for p in parsed if len(p)>0]
  seted = [set(x) for x in parsed]
  u = len(set.intersection(*seted))
  
  return u

summed = sum([all_yes(x) for x in data])
print(summed)

print(all_yes(data[-1]))


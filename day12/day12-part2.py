data = open("data.txt")
data = data.read()
data = data.split("\n")


from collections import defaultdict

def right(value, current, directions):
    # takes d - command, current direction and the list of directions
    # returns the new direction
    index = (directions.index(current) + (value/90))%4
    new_direction = directions[int(index)]
    return new_direction
    

def left(value, current, directions):
    index = (directions.index(current) - (value/90))
    new_direction = directions[int(index)]
    return new_direction

def manhattan(data):
    
    travel_log = defaultdict(int)
    
    current = "E"
    directions = ["E", "S", "W", "N"]

    for d in data:
        symbol = d[:1]
        value = int(d[1:])

        if symbol == "E":
            travel_log["E"]  += value
        elif symbol == "S":
            travel_log["S"]  += value
        elif symbol == "W":
            travel_log["W"]  += value
        elif symbol == "N":
            travel_log["N"]  += value

        elif symbol == "R":
            current = right(value, current, directions)

        elif symbol == "L":
            current = left(value, current, directions)

        elif symbol == "F":
            travel_log[current] += value
         
    N_S = abs(travel_log["N"] - travel_log["S"])
    E_W = abs(travel_log["E"] - travel_log["W"])
    
    return N_S + E_W

print(manhattan(data))

data = open("data.txt")
data = data.read()
data = data.split("\n")


from collections import defaultdict

def right(value, waypoint_position, directions):
    # takes d - command, current direction and the list of directions
    # returns the new directions in a dictionary
    rotation = int(value/90)
    index = [(directions.index(country) + rotation)%4 for country in waypoint_position.keys()] 
    new_directions = {directions[i]: value for i, value in zip(index, waypoint_position.values())}
    return waypoint_position

print(right(90,{"E":1, "N":10}, ["E", "S", "W", "N"]))
    

def left(value, waypoint_position, directions):
    rotation = int(value/90)
    index = [(directions.index(country) - rotation)%4 for country in waypoint_position.keys()]
    new_directions = {directions[i]: value for i, value in zip(index, waypoint_position.values())}
    return new_directions


print(left(90,{"E":1, "N":10}, ["E", "S", "W", "N"]))
def manhattan(data):
    
    waypoint_travel_log = defaultdict(int)
    
    waypoint_travel_log["N"] = 1
    waypoint_travel_log["E"] = 10
    directions = ["E", "S", "W", "N"]

    for d in data:
        symbol = d[:1]
        value = int(d[1:])

        if symbol == "E":
            waypoint_travel_log["E"]  += value
        elif symbol == "S":
            waypoint_travel_log["N"]  -= value
        elif symbol == "W":
            waypoint_travel_log["E"]  -= value
        elif symbol == "N":
            waypoint_travel_log["N"]  += value

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

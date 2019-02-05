import math
import operator
import sys

# globals
ops_min = 0
ops_max = 0
num_frds = 0
plyrs_data = None
prgm_data = None


# writes INVALID INPUT to output.txt
def invalid_input():
    out = open('output.txt', 'w')
    out.write('INVALID INPUT\n')
    sys.exit()


# Reads in the file and shapes the player data and opponent data
def load_data(filename):
    global num_frds, ops_min, ops_max, plyrs_data, prgm_data
    with open(filename, 'r+') as f:
        plyrs_data = f.read().splitlines()
        if len(plyrs_data) < 2: 
            invalid_input()
        for x in range(len(plyrs_data)):
            if x == 0:
                prgm_data = plyrs_data[x]
                prgm_data = [int(i) for i in prgm_data.split()]
                num_frds = prgm_data[0]
                ops_min = prgm_data[1]
                ops_max = prgm_data[2]
                
                if ops_min < 1 or ops_max > 1000000000: 
                    invalid_input()
                if ops_min > ops_max: 
                    invalid_input()
                if num_frds < 1 or num_frds > 50000: 
                    invalid_input()
            else:
                plyr = plyrs_data[x].split(' ')
                plyr[1] = float(plyr[1])
                if plyr[1] < 1 or plyr[1] > 1000000000: 
                    invalid_input()
                plyrs_data[x] = plyr
        plyrs_data.pop(0)  # remove the program data, only player info left
        if num_frds != len(plyrs_data):
            invalid_input()


# Computes the euclidean distance between, of the hours played,
# a friend and the current opponent we are evaluating.
def eucld_dist(frnd, opp):
    return math.sqrt(pow((frnd[1] - opp[1]), 2))


# Determines the possible nearest neighbors based on the hours
# played
def determine_neighbors(plyrs_data, opp, k):
    dists = []
    for x in range(len(plyrs_data)):
        dist = eucld_dist(plyrs_data[x], opp)
        dists.append([plyrs_data[x], dist])
    dists.sort(key=operator.itemgetter(1))

    neighbors = []
    nearest_distance = dists[0][1]
    loop_range = k
    if (len(dists) < k): loop_range = len(dists)
    for y in range(loop_range):
        # only add distances that are the same as the nearest
        if dists[y][1] == nearest_distance:
            neighbors.append(dists[y][0])
    return neighbors


# Classifies whether an opponent has the sword or not
def classify(neighbors, opp):
    prev = neighbors[0][0]
    for x in range(len(neighbors)):
        curr = neighbors[x]
        if curr[0] == 'S':
            return 'S'
        elif x > 0 and prev == 'NS' and curr[0] == 'S':
            return 'S'
        prev = neighbors[x]
    return 'NS'


def main():
    load_data('input.txt')
    opp_data = []
    for i in range(1, ops_max + 1):
        opp_data.append(["", float(i)])

    k = 3
    count = 0
    predictions = []
    for x in range(len(opp_data)):
        neighbors = determine_neighbors(plyrs_data, opp_data[x], k)
        classification = classify(neighbors, opp_data[x])
        if classification == 'S': 
            count += 1
        predictions.append([classification, opp_data[x][1]])
    out = open("output.txt", "w")
    out.write(str(count) + '\n')

main()

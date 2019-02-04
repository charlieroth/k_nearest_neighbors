import math
import operator
import sys

# globals
num_ops = 0
plyrs_data = None
prgm_data = None


# Reads in the file and shapes the player data and opponent data
def load_data(filename):
    global num_frs, num_ops, plyrs_data, prgm_data
    with open(filename, 'r+') as f:
        plyrs_data = f.read().splitlines()
        for x in range(len(plyrs_data)):
            if x == 0:
                prgm_data = plyrs_data[x]
                prgm_data = [int(i) for i in prgm_data.split()]
                num_ops = prgm_data[2]
            else:
                plyr = plyrs_data[x].split(' ')
                plyr[1] = float(plyr[1])
                plyrs_data[x] = plyr

        plyrs_data.pop(0)  # remove the first line of the array


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
    for y in range(k):
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

# Returns the percentage of accuracy between the expected
# results and the predicted ones by the algorithm
def get_accuracy(expected, predictions):
    print("Expected: ", expected)
    correct = 0
    for x in range(len(expected)):
        if expected[x][0] == predictions[x][0]:
            correct += 1
    return (correct/float(len(expected))) * 100.0


def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        load_data(filename)
    else:
        print('Usage:')
        print('python3 main.py <input_file_to_test>')
        sys.exit()

    opp_data = []
    for i in range(1, num_ops + 1):
        opp_data.append(["", float(i)])

    k = 3
    predictions = []
    count = 0
    for x in range(len(opp_data)):
        neighbors = determine_neighbors(plyrs_data, opp_data[x], k)
        classification = classify(neighbors, opp_data[x])
        if classification == 'S':
            count += 1
        predictions.append([classification, opp_data[x][1]])
    
    out = open("output.txt", "w")
    out.write(str(count) + '\n')
    
    print("Predictions: ", predictions)
    correctness = get_accuracy([
        ['S', 1.0],
        ['S', 2.0],
        ['NS', 3.0],
        ['NS', 4.0],
        ['S', 5.0],
        ['S', 6.0],
    ], predictions)
    print("Correctness: ", correctness)


main()

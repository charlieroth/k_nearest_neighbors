# PROBLEM DESCRIPTION

John loves to play an online game. He wants to know if opponents have the ultimate sword so that he can avoid fighting with such players. He has data of his friends and decides to make a classifier based on the data. For each of his N friends (1 <= N <= 50,000), he knows the amount of the time a friend has played, and whether the friend have the item or not. Each of his friend have distinct amount of playtime. With the data, he builds a “nearest neighbor classifier”. For a new player P, first he finds a friend P’ in the data whose playtime is the closest to the playtime of P. If P’ has the item, he predicts that the new player P also has the item. If P’ does not have the item, he guessed that the new player P does not have the item. If there are more than one closest player among his friends, he guessed the new player P has the item if any one of them have it. John carefully observes the possible opponents and finds out that there is one opponent of every integer playtime between A and B (inclusive). Please determine that how many of the opponents will have the ultimate sword, using the John’s classifier. Note that the classifier guesses based on the information of the friends and does not use information on the new opponents. Also note that, A and B can be very large and your program may not be effective if you test each opponent between A and B against the entire friends. i.e. **you will not want to simply iterate from A to B one by one and find the friend with the closest time among the entire dataset.**

# Input

Read from a file called `input.txt`

The first line contains 3 integers `N`, `A`, `B`, where `1 <= A <= B <= 1,000,000,000`.

The next `N` lines each describe one friend. Each line is (`S` or `NS`) and `T`, meaning that
the palyer has played for time T followed by, `S`, which means the player has the sword or, `NS`, no sword.

Time `T` are all integers where `1 <= T <= 1,000,000,000`

#### `input.txt`

```
3 1 6
S 1
NS 4
S 6
```

# Output

A single integer giving the number of opponents that the algorithm will classify
as having the sword. In the example, opponents with playtime 1, 2, 5, 6 will be
classified as having the sword. Therefore the output will be:

#### `output.txt`

```
4
```

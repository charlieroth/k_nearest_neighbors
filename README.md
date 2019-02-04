# INPUT

Read from a file called `input.txt`

The first line contains 3 integers N, A, B `1 <= A <= B <= 1,000,000,000`.

The next N lines each describe one friend. Each line is either S, T, meaning that
the palyer played for time T has the sword, or NS, T, meaning that the player
played for time T doesn't have the sword. Time T are all integers and
`1 <= T <= 1,000,000,000`

# Sample Input
```
3 1 6
S 1
NS 4
S 6
```

# OUTPUT

Write to a file called `output.txt`

A single integer giving the number of opponents that the algorithm will classify
as having the sword. In the example, opponents with playtime 1, 2, 5, 6 wil be
classified as having the sword. Therefore the output will be 4.

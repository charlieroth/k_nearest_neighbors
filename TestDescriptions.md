# Test Descriptions

#### `input1.txt`
This is the example test case that was given to us.

#### `input2.txt`
This file is empty and results in "INVALID INPUT" in output.txt

#### `input3.txt`
This file provides our N, A and B but there is no player information, therefore 
the result will be "INVALID INPUT" in output.txt

#### `input4.txt`
This file tests the case where N does not match the number of players provided 

#### `input5.txt`
This file tests a high number of opponents (1000), the result will be 998 due to
the fact that opponents 7-1000 will all have the closest neighbor of "S 6" and
that player has the sword, therefore so opponents 1-1000.

#### `input6.txt`
This file tests when there is only 1 friend, who has the sword, therefore 
all opponents will be classified as not having the sword also so
output.txt should contain the same number of opponents.

#### `input7.txt`
This file tests when there is only 1 friend, who does not have the sword,
therefore all opponents will be classified as not having the sword also so
output.txt should contain 0.

#### `input8.txt`
This file tests whether the N number of friends is within a valid range (-1)

#### `input9.txt`
This file tests whether the N number of friends is within a valid range (50,001)

#### `input10.txt`
This file tests whether the range of opponent playtime A is within the valid
range `(1 <= A <= B <= 1000000000)`. In this case A is -1.

#### `input11.txt`
This file tests whether opponent playtime A is less than or equal to B.

#### `input12.txt`
This file tests whether a friends playtime is within the valid range
`(1 <= T <= 1000000000)`. In this case the 3rd friend's playtime is -1.

#### `input13.txt`
This file tests whether a friends playtime is within the valid range
`(1 <= T <= 1000000000)`. In this case the 3rd friend's playtime is 1000000001.

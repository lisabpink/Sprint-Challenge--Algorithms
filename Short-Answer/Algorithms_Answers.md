#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)Runtime complexity: 0(n)
One while loop.
Linear algorithm.  
 The runtime/space used will grow at the same rate because n is increasing linearly with a single step.

b)Runtime complexity: O(n^2)
These are nested loops.
The outside for loop runs O(n).  
 The inside while loop, checks n again and runs operation at O(n).  
 Both of the loops checked n and need to be combined.

c)Runtime complexity: O(n)
Linear and recursive.
The algorithm will call itself until 0 is returned.
The runtime/space used will grow at the same rate.

## Exercise II

UNDERSTAND

Need to find the lowest floor where the egg would break if thrown from that floor.
Need to find the last floor that the egg doesn't break, and the first floor that it does.

PLAN

Assuming the floors in the building are in order, can use a pre-sorted list.
Use binary search tree data structure because it would be the fastest, returning in constant time 0(1).
Also, BST nodes have the following properties:
The left subtree of a node has a key less than or equal to its parent node's key.
The right subtree of a node has a key greater than to its parent node's key.

Use recursion to break down the problem into smaller and smaller subproblems until the subproblem is solved.

EXECUTE

Find the midpoint index and start there. Length of pre-sorted list divided by two.
If the egg breaks at the midpoint index, go to the pre-sorted list/side with smaller values and start from the midpoint of the lower floors.
If the egg does not break, go to the pre-sorted list/side with larger values and start from the midpoint of the higher floors.
Continue recursion until there are only two floors left(base case), the smaller floor number should not break the egg and the bigger floor number should break the egg.

Runtime complexity of this is O(logn).

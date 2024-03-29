<h1 align="center">
    Burnt Toast Conjecture
</h1>

*solved* relates to https://oeis.org/A002326

## Introduction

The burnt toast problem deals with certain states of an ordered array
the method to count number of these states is described below, and an reference
python implementation has been provided.

### Inputs
- x (size)

### Glossary
 - element

   bistated data with position

### Operation
- `flip(n)`

    take the first n elements change their state and prepend in reverse order
    
    That is we first take the first N elements in array
    Then we flip their states

    #### Example

    ```
    array = [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1)]
    ```

    1. Performing `flip(2)` operation on array

        ```
        // 1st step
        array = [(0, 0), (1, 0), (2, 1), (3, 1), (4, 1)]

        // 2nd step
        array = [(1, 0), (0,0), (2, 1), (3, 1), (4, 1)]
        ```

    2. Performing `flip(3)` operation on array

        ```
        // 1st step (flipping 1s to 0s and 0s to 1s for 1st 3 elements)
        array = [(0, 0), (1, 0), (2, 0), (3, 1), (4, 1)]
        // 2nd step select pivot and rearrange element
        array = [(2, 0), (1, 0), (0, 0), (3, 1), (4, 1)]
        // 3rd element went to 1st, 1st went to 3rd,
        // 2nd remained at 2nd since it was the pivot
        ```
        
    3. `flip(3)` alternative illustraion
       
        ```
        array = [(0, True), (1, True), (2, True), (3, True)]
        // first step
        array = [(0, False), (1, False), (2, False), (3,True)] // first 3 elements are pointing down
        // 2nd step, reversing the first three elements
        // python: array[0:3] = reverse(array[0:3])
        array = [(2, False), (1, False), (0, False), (3, True)]
        ```

### Setup
- make an array
- create x elements with same initial direction and assign positions to each

### Steps
- let n = 1
- start loop
- perform `flip(n)` on array
- check if array is back to the original, with each element back to it's original position and state.
   - if yes, return number of iterations
   - else `n = (n % x) + 1`, where x is array length.

## The Conjecture

The conjecture that was established after checking 2021 values is that.

> Starting from any initial array state, after a finite number of cyclically
> paramaterized flip operations the array returns to the initial state.

where "cyclically paramaterized flip operations" refers to
`flip(iteration % array_size + 1)` applied every iteration.

To extend this trivially, "this set of ordered operations can be applied
to every array of the same or greater size to return the array to it's initial
state"

## The Original Problem

*solved*

Find an algebraic expression for the problem which accepts input and
gives the answer that is, the number iterations it takes to return to the original
state of the array. This goal was not achieved due to the randomness of the data.

## Why the name?

Because burnt toast's top and bottom can be differentiated which represents two
states

## Extending

This problem can be extended from bistated to multistated with the corresponding
flip operation

## Implementation

Thanks to martian17 for optimisations for computing 2021 values for previous version
https://github.com/martian17/Burned_Toast_Conjecture

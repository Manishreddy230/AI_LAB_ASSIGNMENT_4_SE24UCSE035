
---

## Problem 3: Sudoku Solver

### Description
Sudoku is modeled as a CSP where each empty cell is a variable with domain values from 1 to 9.

### Constraints
- Each number must appear only once in each row
- Each number must appear only once in each column
- Each number must appear only once in each 3x3 subgrid

### Approach
- Use backtracking to fill empty cells
- Validate constraints before placing a number

### Output
[5, 3, 4, 6, 7, 8, 9, 1, 2]
[6, 7, 2, 1, 9, 5, 3, 4, 8]
[1, 9, 8, 3, 4, 2, 5, 6, 7]
[8, 5, 9, 7, 6, 1, 4, 2, 3]
[4, 2, 6, 8, 5, 3, 7, 9, 1]
[7, 1, 3, 9, 2, 4, 8, 5, 6]
[9, 6, 1, 5, 3, 7, 2, 8, 4]
[2, 8, 7, 4, 1, 9, 6, 3, 5]
[3, 4, 5, 2, 8, 6, 1, 7, 9]

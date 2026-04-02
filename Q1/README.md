# Constraint Satisfaction Problems (CSP) Assignment

This repository contains implementations of classic Constraint Satisfaction Problems (CSP) using Python.  
All problems are solved using the Backtracking algorithm while ensuring that constraints are satisfied.

---

## Problem 1: Australia Map Coloring

### Description
The Australia map coloring problem is a CSP where each state (WA, NT, SA, Q, NSW, V, T) is treated as a variable.  
Each variable is assigned a color from the domain {Red, Green, Blue}.

### Constraint
No two adjacent states can have the same color.

### Approach
- Represent the map as a graph using adjacency lists
- Assign colors using backtracking
- Check constraints before assigning each color

### Output

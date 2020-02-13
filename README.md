# Sudoku-Solver
Two Sudoku solver implementations written in C++ and Python, capable of solving any arbitrary sudoku grids (or determining if they don't have a possible solution). Both programs use a recursive backtracking algorithim to find and verify solutions.

## Install
Both the Python and C++ implementations are entirely self contained: no external dependencies are required besides the base langauges.

## Usage

### C++

Create an object of class Sudoku and a file object containing the grid to solve:
```
ifstream fin("grid.txt");
Sudoku obj;
```
Use the method `input(istream&)` to load your grid:
```
obj.input(fin);
```
Use the method `solve()` to solve the puzzle:
```
obj.solve()
```
The grid can be output at any stage with the `output(istream&)` method:
```
obj.output(cout);
```


### Python

The Python implementation includes driver code to generate and solve random grids. If you want to solve a specific puzzle, define it as a two-dimensional list called `grid` at the top of main.

The python implementation also supports arbitrary sized grids! Try it out with a 16x16 puzzle.


## License
This project is licensed under the terms of the MIT license.


# sudoku-solve

Implimented 2 sudoku solving algorithms and comparing the runtime of both on complex sudoku puzzles.

sudoku.py is a tradition backtracking algorithm.Puzzle is solved one piece at a time,while removing the numbers that does no meet some specified conditions.

sudoku2.py is the algorith which uses the fact that at any given time at least one place in the sudoku puzzle can be filled with absolute certainty.The entire state of the game is stored and the possible values for each block are recursively eliminated.

Overall sudoku.py performed better than sudoku2.py.

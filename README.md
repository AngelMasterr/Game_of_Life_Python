# Game_of_Life_Python

The Game of Life is a simulation of a population of cells that evolve over time according to a set of simple rules. The simulation takes place on a two-dimensional grid, where each cell can be either alive or dead↳

The rules of the Game of Life are as follows:

1. Any live cell with fewer than two live neighbors dies, as if by underpopulation.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

# Requirements:

- [x] All rules applied
- [x] The game starts paused, with any key unpause and vice versa
- [x] With the left mouse button, make the cells live
- [x] With the right mouse button, make the cells dead
- [x] With the center mouse button, clean the screen

have fun

![Alt Text](clip_Game_of_Life.gif)

# How to use

1. Clone Github repository:

```bash
git clone git@github.com:AngelMasterr/Game_of_Life_Python.git
```

2. Navigate to the project directory:

```bash
cd Game_of_Life_Python
```

3. Install required dependencies:

```bash
pip install -r requirements.txt
```

4. Run the project:

```bash
python main.py
```

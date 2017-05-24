# Rubik's Cube
The most famous puzzle of the world.

![Animated GIF](/animation.gif)

## Installation
* Python 2
* VPython
* pygame (Install using `pip install pygame`)

## Capabilities
The app is able to do the following:
* Solve the rubik's cube game
* Give the output algorithm for an unsolved Rubik's cube
* Interactive guide for noobs :>

Although the generated algorithm may not be the best in the world, I assure you, it is a very good algorighm out there :-)

## Instructions:
Run `python main.py` in your command prompt/terminal to start the program.

However, you might want to modify `main.py` for providing commands.
* `c.action(algorithm)` would apply `algorithm` (For e.g., `algorithm='F2 L2 U R'`) to the cube.
* `c.solve()` will give the algorithm to solve the cube.
* Therefore, `c.action(c.solve()` will solve the rubik's cube.

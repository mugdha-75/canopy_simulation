
# Canopy Simulation

A python simulation project using libraries like `numpy`, `matploblib` and others. The project consist of two `.py` files.
- `cano.py`
  - It is the main file to run the program
  - It imports `House, Tree, Sky, Land, Cat, Dog, Sun, Water` from `canopy.py`
  - Depending on the `timestamp` and the position of the `Sun` others changes states or color in the simulation.
- `canopy.py`
  - It contains blocks that is imported in the `cano.py`
  - `Cat, Dog` contains `stepChange` method.
  - `Cat` states are`["kitten","mature"]`
  - `Dog` states are`["puppy","mature"]`

## Requirements
Install matplotlib into the system or environment 
```python
pip install matplotlib
```
## How to run
Run the command in the terminal from the project directory 
```bash
python cano.py
```
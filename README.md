# CECS 427: Game Theory

#### Martin Silva (#030854159), Zachary Padilla (#033497475)

## Dependencies
Required Libraries:
- networkx
- pandas
- matplotlib
- scipy

In order to run this project via git:

```
~/: git clone https://github.com/zachfpadilla/CECS-427-Game-Theory
~/: cd CECS-427-Game-Theory/

### Optionally ###
~/CECS-427-Game-Theory/: python3 -m venv .venv
~/CECS-427-Game-Theory/: source .venv/bin/activate
(.venv) ~/CECS-427-Game-Theory/: pip install networkx, pandas, matplotlib, scipy
```

```
~/CECS-427-Game-Theory/: python3 ./traffic_analysis.py -h

usage: traffic_analysis.py [-h] digraph_file n initial final [--plot]

Python application that handles Girvan-Newman graph partitioning, edge removal, homophily/balance verification, and visualization.

positional arguments:
  digraph_file            Path to the input graph file in .gml format
  n                       An integer representing the number of vehicles
  initial                 An integer representing the initial node
  final                   An integer representing the final node

options:
  --plot                  Plots the output of the command
```

## Usage Instructions
* ``--plot`` outputs an image of the plot to a new window.

## Description of Implementation
- All instructions were followed as listed—interpretations were made where needed.

## Examples of Commands and Outputs
``python ./traffic_analysis.py traffic.gml 4 0 3 --plot``
```
Successfully loaded graph from 'traffic.gml'.
Nodes: 4, Edges: 5
Nash Equilibrium: {('0', '1'): 2.0087271010019605, ('0', '2'): 1.9912728989980364, ('1', '3'): 1.9730143070798423, ('1', '2'): 0.03571279392212056, ('2', '3'): 2.0269856929201575}
Social Optimum: {('0', '1'): 2.002869162237398, ('0', '2'): 1.9971308377626016, ('1', '3'): 1.9790189950138668, ('1', '2'): 0.023850167223531584, ('2', '3'): 2.0209810049861328}

--- Nash Equilibrium (User Optimum) ---
Edge (0 -> 1): 2.0087 vehicles
Edge (0 -> 2): 1.9913 vehicles
Edge (1 -> 3): 1.9730 vehicles
Edge (1 -> 2): 0.0357 vehicles
Edge (2 -> 3): 2.0270 vehicles

--- Social Optimum ---
Edge (0 -> 1): 2.0029 vehicles
Edge (0 -> 2): 1.9971 vehicles
Edge (1 -> 3): 1.9790 vehicles
Edge (1 -> 2): 0.0239 vehicles
Edge (2 -> 3): 2.0210 vehicles

Generating plot...

Displaying plot... Close the plot window to exit.
```
<img width="1800" height="833" alt="Screenshot_3" src="https://github.com/user-attachments/assets/ecc2e6ae-9ac1-4ba6-bbaf-fd8c89ddc336" />

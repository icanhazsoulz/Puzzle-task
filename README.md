# Solution
Based on the task conditions, the set of fragments can be represented as a graph, where each number is associated with a set of numbers such that the last two digits of the number match the first two digits of each associated number.

Such relationships naturally form a graph structure, where each number is represented as a node, and a directed edge connects two nodes if the linking rule is satisfied.

The solution to the task is reduced to finding the longest path.

We use the Depth-First Search (DFS) algorithm to explore all possible paths and find the longest one.

***Note:*** For the sake of brevity of the solution, we assume that the source dataset is in the `source.txt` file in the project root, is provided in the required format, and does not contain invalid data.

# Setup and run

Ensure you have Python v3.12 installed on your machine, then run the program:

`python main.py`

Alternatively, you can run the program in a Docker container:

Ensure you have Docker and Docker Compose installed. Build and run the program using Docker Compose:

`docker compose up --build`
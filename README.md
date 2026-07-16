# LangGraph Multi Conditional Graph

A LangGraph project demonstrating multi-level conditional routing using sequential decision nodes, branching, merging, and workflow visualization.

## Graph Overview

The workflow performs two stages of conditional routing:

1. **Operation 1**

   * Addition (`+`)
   * Subtraction (`-`)
2. **Operation 2**

   * Multiplication (`*`)
   * Division (`/`)

Both conditional branches merge before proceeding to the next stage, ending in a common `END` node.

```text
                START
                  |
                  v
          operation1_node
            /          \
           /            \
     add_node      subtract_node
           \            /
            \          /
          operation2_node
            /          \
           /            \
   multiply_node   divide_node
           \          /
            \        /
               END
```

## Features

* Multi-level conditional routing
* Sequential decision nodes
* Branching and merging workflow
* Dynamic execution based on user input
* Shared state using `TypedDict`
* Automatic generation of the workflow graph as a PNG image

## Project Structure

```text
.
├── multi_conditional_graph.py
├── multi_conditional_graph.png
└── README.md
```

## Requirements

* Python 3.10+
* LangGraph

Install the dependency:

```bash
pip install langgraph
```

## How to Run

Run the program:

```bash
python multi_conditional_graph.py
```

The application will:

1. Generate and save the workflow graph as `multi_conditional_graph.png`.
2. Ask the user for three numbers.
3. Ask the user to choose:

   * First operation (`+` or `-`)
   * Second operation (`*` or `/`)
4. Execute the corresponding workflow path.
5. Display the final result.

## Example

### Input

```text
Enter first number: 10
Enter second number: 5
Enter third number: 2

Choose first operation (+ or -): +
Choose second operation (* or /): *
```

### Execution

```text
10 + 5 = 15
15 × 2 = 30
```

### Output

```text
Final Result: 30
```

## Technologies Used

* Python
* LangGraph

## Concepts Demonstrated

* StateGraph
* TypedDict state management
* Conditional edges
* Sequential routing
* Branch merging
* START and END nodes
* Graph visualization
* Dynamic user-driven execution

## License

This project is intended for educational and learning purposes.

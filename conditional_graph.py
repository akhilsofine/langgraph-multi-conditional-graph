from typing import TypedDict
from langgraph.graph import StateGraph, START, END


# -----------------------
# State
# -----------------------
class AgentState(TypedDict):
    num1: int
    num2: int
    num3: int
    operation1: str
    operation2: str
    find_num: float


# -----------------------
# First Router Node
# -----------------------
def operation1_node(state: AgentState):
    return state


def add_node(state: AgentState):
    state["find_num"] = state["num1"] + state["num2"]
    return state


def subtract_node(state: AgentState):
    state["find_num"] = state["num1"] - state["num2"]
    return state


# -----------------------
# Second Router Node
# -----------------------
def operation2_node(state: AgentState):
    return state


def multiply_node(state: AgentState):
    state["find_num"] *= state["num3"]
    return state


def divide_node(state: AgentState):
    if state["num3"] == 0:
        raise ValueError("Cannot divide by zero.")
    state["find_num"] /= state["num3"]
    return state


# -----------------------
# Routing Functions
# -----------------------
def route_operation1(state: AgentState):
    if state["operation1"] == "+":
        return "add_node"
    elif state["operation1"] == "-":
        return "subtract_node"
    else:
        raise ValueError("Invalid first operation. Use '+' or '-'.")


def route_operation2(state: AgentState):
    if state["operation2"] == "*":
        return "multiply_node"
    elif state["operation2"] == "/":
        return "divide_node"
    else:
        raise ValueError("Invalid second operation. Use '*' or '/'.")


# -----------------------
# Build Graph
# -----------------------
graph = StateGraph(AgentState)

graph.add_node("operation1_node", operation1_node)
graph.add_node("add_node", add_node)
graph.add_node("subtract_node", subtract_node)

graph.add_node("operation2_node", operation2_node)
graph.add_node("multiply_node", multiply_node)
graph.add_node("divide_node", divide_node)

# START -> Operation 1
graph.add_edge(START, "operation1_node")

# Conditional Routing 1
graph.add_conditional_edges(
    "operation1_node",
    route_operation1,
    {
        "add_node": "add_node",
        "subtract_node": "subtract_node",
    },
)

# Merge
graph.add_edge("add_node", "operation2_node")
graph.add_edge("subtract_node", "operation2_node")

# Conditional Routing 2
graph.add_conditional_edges(
    "operation2_node",
    route_operation2,
    {
        "multiply_node": "multiply_node",
        "divide_node": "divide_node",
    },
)

# Merge to END
graph.add_edge("multiply_node", END)
graph.add_edge("divide_node", END)

# -----------------------
# Compile Graph
# -----------------------
app = graph.compile()

# -----------------------
# Save Graph as PNG
# -----------------------
png_data = app.get_graph().draw_mermaid_png()

with open("multi_conditional_graph.png", "wb") as f:
    f.write(png_data)

print("Graph saved successfully as 'multi_conditional_graph.png'")

# -----------------------
# User Input
# -----------------------
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

operation1 = input("Choose first operation (+ or -): ").strip()
operation2 = input("Choose second operation (* or /): ").strip()

# -----------------------
# Execute Graph
# -----------------------
result = app.invoke(
    {
        "num1": num1,
        "num2": num2,
        "num3": num3,
        "operation1": operation1,
        "operation2": operation2,
        "find_num": 0,
    }
)

print("\nFinal State:")
print(result)

print(f"\nFinal Result: {result['find_num']}")
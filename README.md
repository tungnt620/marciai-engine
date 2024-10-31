## What is MarciAI-Engine?
- It is the brain of MarciAI. Give it a task, and it will return instructions step by step and execute them to achieve the goal.

## How Does It Work?
- It utilizes a graph. A graph is a combination of nodes that can refer to skills. The engine generates the graph and executes it to get the result.
- Skills can vary, from copying files and editing files to calling APIs and taking notes.
- When MarciAI-Engine receives a task, it uses LLM to create the graph, execute it, validate the result, and reiterate until it gets the correct one.

## Advantages
- Explainable AI: When it runs, it can show the execution path (a graph) and execution log for the user.
- Adaptable: It has the ability to allow the user to change the logic by modifying the graph and adding new skills.
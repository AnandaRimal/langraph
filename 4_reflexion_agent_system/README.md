# Reflexion Agent System

This folder contains an implementation of a **Reflexion Agent** using LangGraph.

## Overview

Reflexion is a framework that reinforces language agents through linguistic feedback. Unlike the basic reflection agent, this system includes an **external tool execution step** to gather information for improvement.

The process involves:
1.  **Draft**: The agent generates an initial answer and search queries.
2.  **Execute Tools**: The system executes the search queries using Tavily.
3.  **Revise**: The agent revises its answer based on the search results and its own reflection.
4.  **Loop**: This cycle repeats for a specified number of iterations.

## Code Structure

- `reflexion_graph.py`: Defines the main LangGraph workflow.
- `chains.py`: Contains the `first_responder` and `revisor` chains.
- `execute_tools.py`: Handles the execution of search queries using `TavilySearchResults`.
- `schema.py`: Defines the Pydantic models for structured output (`AnswerQuestion`, `ReviseAnswer`).

## Flow Visualization

```mermaid
graph TD
    Start([Start]) --> Draft
    Draft --> ExecuteTools
    ExecuteTools --> Revisor
    Revisor --> Check{Max Iterations?}
    Check -->|Yes| End([End])
    Check -->|No| ExecuteTools
    
    style Start fill:#f9f,stroke:#333,stroke-width:2px
    style End fill:#9f9,stroke:#333,stroke-width:2px
    style Draft fill:#bbf,stroke:#333,stroke-width:2px
    style Revisor fill:#bfb,stroke:#333,stroke-width:2px
    style ExecuteTools fill:#ff9,stroke:#333,stroke-width:2px
```

## How to Run

```bash
python reflexion_graph.py
```

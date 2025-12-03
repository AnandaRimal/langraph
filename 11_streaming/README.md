# Streaming

This folder demonstrates **streaming** in LangGraph for real-time output.

## Overview

Streaming allows you to:
- **Display intermediate results** as the agent works.
- **Improve user experience** by showing progress in real-time.
- **Debug workflows** by observing each step as it happens.

## Example

### Stream Events (`1_stream_events.ipynb`)
Demonstrates event streaming:
- Stream **node outputs** as they are generated.
- Stream **LLM tokens** for real-time text generation.
- Stream **tool calls** and their results.

## Streaming Modes

LangGraph supports several streaming modes:

### 1. `stream()` - Stream Node Outputs
Yields the output of each node as it completes:
```python
for chunk in app.stream(inputs):
    print(chunk)
```

### 2. `stream_events()` - Stream All Events
Streams detailed events including:
- LLM token generation
- Tool invocations
- Node starts/ends
- State updates

### 3. `astream_events()` - Async Streaming
For async applications with real-time updates.

## Flow Visualization

```mermaid
graph LR
    Start([Input]) --> Node1[Node 1]
    Node1 -->|Stream| Output1[Output 1]
    Node1 --> Node2[Node 2]
    Node2 -->|Stream| Output2[Output 2]
    Node2 --> Node3[Node 3]
    Node3 -->|Stream| Output3[Output 3]
    
    style Start fill:#f9f,stroke:#333,stroke-width:2px
    style Output1 fill:#9f9,stroke:#333,stroke-width:2px
    style Output2 fill:#9f9,stroke:#333,stroke-width:2px
    style Output3 fill:#9f9,stroke:#333,stroke-width:2px
    style Node1 fill:#bbf,stroke:#333,stroke-width:2px
    style Node2 fill:#bbf,stroke:#333,stroke-width:2px
    style Node3 fill:#bbf,stroke:#333,stroke-width:2px
```

## How to Run

Open `1_stream_events.ipynb` in Jupyter or VS Code to see streaming in action.

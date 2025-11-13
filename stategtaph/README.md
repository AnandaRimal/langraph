# 🎯 StateGraph Fundamentals

This folder contains examples demonstrating the core concepts of LangGraph's StateGraph - the foundation for building stateful workflows.

## 📚 Notebooks Overview

### 1. **basicstate.ipynb** - StateGraph Basics
**Difficulty:** ⭐ Beginner  
**Concepts:** StateGraph, nodes, edges, conditional routing

Learn the fundamentals:
- How StateGraph works
- Creating nodes (processing functions)
- Adding edges (connections)
- Conditional routing based on state
- Looping workflows

**Example:** A counter that increments until reaching a threshold, demonstrating loops and conditional logic.

**Use this when:** Getting started with LangGraph or understanding state-based workflows.

---

### 2. **complexstate.ipynb** - Advanced State with Reducers
**Difficulty:** ⭐⭐ Intermediate  
**Concepts:** Reducers, state merging, complex data structures

Advanced state management:
- Multiple state fields
- Custom reducers (`operator.add`, `operator.concat`)
- Automatic state aggregation
- Managing lists and accumulated values

**Example:** A counter with history tracking, demonstrating:
- `count`: Simple replacement
- `sum`: Accumulated total with `operator.add`
- `history`: Growing list with `operator.concat`

**Use this when:** Building workflows that need to aggregate or accumulate data across iterations.

---

## 🎓 Key Concepts

### StateGraph
The container for your entire workflow:
```python
graph = StateGraph(StateType)
graph.add_node("node_name", function)
graph.add_edge("source", "target")
app = graph.compile()
```

### Nodes
Functions that process and update state:
```python
def my_node(state: MyState) -> MyState:
    # Process state
    return {"field": new_value}  # Updates merged into state
```

### Edges
Connections between nodes:
- **Static Edge**: Always goes to same next node
- **Conditional Edge**: Routes based on state value

### Reducers
Control how state updates are merged:

| Reducer | Behavior | Example Use |
|---------|----------|-------------|
| **Default** | Replace value | `count: int` |
| **operator.add** | Add numbers | `sum: Annotated[int, operator.add]` |
| **operator.concat** | Concatenate lists | `history: Annotated[List, operator.concat]` |
| **add_messages** | Append messages | `messages: Annotated[list, add_messages]` |

---

## 📊 State Patterns

### Simple State (Replace)
```python
class SimpleState(TypedDict):
    count: int  # Each update replaces the value

def increment(state):
    return {"count": state["count"] + 1}
```

### Accumulating State
```python
class AccumulatingState(TypedDict):
    total: Annotated[int, operator.add]  # Values are summed
    
def add_value(state):
    return {"total": 5}  # Adds 5 to existing total
```

### List Building
```python
class HistoryState(TypedDict):
    items: Annotated[List[str], operator.concat]  # Lists are merged
    
def add_item(state):
    return {"items": ["new_item"]}  # Appends to list
```

---

## 🎯 Learning Path

```
1. basicstate.ipynb
   ↓ (Understand core concepts)
   - StateGraph structure
   - Nodes and edges
   - Conditional routing
   
2. complexstate.ipynb
   ↓ (Master state management)
   - Multiple fields
   - Reducers
   - Data accumulation
```

## 🔍 Workflow Patterns

### Loop Pattern (basicstate.ipynb)
```
START → increment → [check] → continue? → increment
                      ↓
                     END
```

### Accumulate Pattern (complexstate.ipynb)
```
START → process → accumulate data → process → END
         ↓            ↓              ↓
      count++      sum+=count   history.append(count)
```

---

## 💡 When to Use Each Pattern

### Basic StateGraph
- Simple workflows
- Sequential processing
- Learning fundamentals
- Prototyping

### Complex State with Reducers
- Aggregating data across iterations
- Building histories or logs
- Calculating running totals
- Managing multiple related values

---

## 🚀 Real-World Applications

### Basic StateGraph
- ✅ Retry logic with counters
- ✅ Status checking loops
- ✅ Conditional branching workflows
- ✅ State machines

### Complex State
- ✅ Data pipeline aggregations
- ✅ Multi-step calculations
- ✅ Audit trails and logging
- ✅ Conversation history management

---

## 📖 Next Steps

After mastering StateGraph:
1. **Chatbots** (`../chatbot/`) - Apply state to conversation management
2. **Human-in-the-Loop** (`../humman in the loop/`) - Add interruptions and approvals
3. **ReAct Agents** (`../react agent/`) - Build reasoning agents
4. **Reflection** (`../Basic reflection agent/`) - Self-improving systems

---

**💡 Tip:** Start with `basicstate.ipynb` to understand the fundamentals, then move to `complexstate.ipynb` to learn advanced state management techniques.

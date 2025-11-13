# 🙋 Human-in-the-Loop Patterns

This folder demonstrates techniques for adding human oversight and control to LangGraph workflows - essential for production AI systems requiring approval, feedback, or manual intervention.

## 📚 Notebooks Overview

### 1. **command.ipynb** - Dynamic Routing with Command
**Difficulty:** ⭐⭐ Intermediate  
**Concepts:** Command object, dynamic routing, programmatic control

Learn to control graph flow programmatically:
- Using `Command` for explicit routing
- Combining state updates with navigation
- Dynamic node selection at runtime
- Alternative to static edges

**Example:** Sequential nodes (A→B→C) controlled via Command objects instead of static edges.

**Use this when:** You need flexible routing that changes based on runtime conditions.

---

### 2. **input.ipynb** - Interactive Human Feedback
**Difficulty:** ⭐⭐ Intermediate  
**Concepts:** interrupt(), human input, resume patterns

Interactive workflow control:
- `interrupt()` function for pausing execution
- Collecting human input mid-workflow
- Conditional routing based on user decisions
- Resume execution with user response

**Example:** LinkedIn post generator with human approval - user decides whether to post or request revisions.

**Use this when:** Building workflows that need human decision-making at specific points.

---

### 3. **3_resume.ipynb** - Resume with Command
**Difficulty:** ⭐⭐⭐ Advanced  
**Concepts:** Command resume, interrupt + resume, decision flows

Advanced human-in-the-loop:
- Combining `interrupt()` with `Command`
- Resuming execution with decisions
- Multi-path routing after interruption
- State preservation across pauses

**Example:** Multi-branch workflow where human chooses path (C or D) after interruption.

**Use this when:** Complex workflows requiring human choice between multiple options.

---

### 4. **4_approval.ipynb** - Tool Approval Workflow
**Difficulty:** ⭐⭐⭐ Advanced  
**Concepts:** interrupt_before, checkpointing, tool approval

Production-ready approval pattern:
- `interrupt_before` for pre-execution pauses
- Checkpointing with MemorySaver
- Approval before tool execution
- Resume without new input

**Example:** Chatbot with web search that requires approval before searching.

**Use this when:** Building production systems where certain actions need approval.

---

## 🎯 Learning Path

```
1. command.ipynb
   ↓ (Learn dynamic routing)
2. input.ipynb
   ↓ (Add human input)
3. 3_resume.ipynb
   ↓ (Master resume patterns)
4. 4_approval.ipynb
   ↓ (Production workflows)
```

## 📊 Pattern Comparison

| Feature | Command | input() | resume | interrupt_before |
|---------|---------|---------|--------|------------------|
| Dynamic Routing | ✅ | ❌ | ✅ | ❌ |
| Human Input | ❌ | ✅ | ✅ | Implicit |
| Pause Execution | ❌ | ✅ | ✅ | ✅ |
| Multi-path Choice | ✅ | ✅ | ✅ | ❌ |
| Production Ready | ⚠️ | ❌ | ✅ | ✅ |
| Requires Checkpointer | ❌ | ❌ | ✅ | ✅ |

## 🔑 Key Concepts

### Command Object
```python
return Command(
    goto="next_node",  # Where to go
    update={"key": "value"}  # State updates
)
```

**Benefits:**
- Explicit routing control
- Combines navigation + state update
- Decided at runtime, not graph-build time

### interrupt() Function
```python
response = interrupt("Question for human?")
# Execution pauses here
# Human provides input
# Continues with response value
```

**Benefits:**
- Direct human interaction
- Simple syntax
- Automatic pause/resume

### interrupt_before
```python
app = graph.compile(
    checkpointer=memory,
    interrupt_before=["critical_node"]
)
```

**Benefits:**
- Production-safe pattern
- Works without code changes in nodes
- Controlled via graph compilation

### Resume Patterns
```python
# Resume with input
app.invoke(Command(resume="user_choice"), config)

# Resume without input
app.stream(None, config)
```

---

## 🎭 Use Cases

### Command
- ✅ Dynamic workflow routing
- ✅ Conditional branching
- ✅ Error handling flows
- ✅ State-dependent navigation

### interrupt() with input
- ✅ Content approval
- ✅ Parameter collection
- ✅ Quality review
- ✅ Interactive refinement

### interrupt_before
- ✅ Tool execution approval
- ✅ Cost control (expensive API calls)
- ✅ Compliance requirements
- ✅ Safety-critical operations

### Resume Patterns
- ✅ Multi-option decisions
- ✅ Approval workflows
- ✅ Human-guided navigation
- ✅ Conditional continuation

---

## 🏗️ Architecture Patterns

### Simple Approval
```
node_a → [pause] → human approval → continue or stop
```

### Multi-path Decision
```
node_a → [pause] → human choice → path_b or path_c → END
```

### Tool Approval
```
chatbot → detect tool need → [pause] → approve? → execute tool → chatbot
```

### Iterative Refinement
```
generate → [pause] → review → good? → END
             ↑                   ↓
             └────── revise ─────┘
```

---

## 🚀 Production Best Practices

### 1. Use interrupt_before for Safety
```python
# ✅ Good: Controlled at compile time
app = graph.compile(interrupt_before=["risky_operation"])

# ❌ Avoid: input() in production (blocking)
response = input("Approve?")
```

### 2. Always Use Checkpointers
```python
from langgraph.checkpoint.memory import MemorySaver

memory = MemorySaver()
app = graph.compile(checkpointer=memory)
```

### 3. Thread IDs for Multi-user
```python
config = {"configurable": {"thread_id": user_id}}
app.invoke(input, config)
```

### 4. Check State Before Resume
```python
snapshot = app.get_state(config)
print(snapshot.next)  # Which node is waiting?
```

---

## 📖 Stream Modes

All notebooks demonstrate different `stream_mode` options:

| Mode | Returns | Best For |
|------|---------|----------|
| `"values"` | Full state | User-facing output |
| `"updates"` | Only changes | Incremental UI |
| `"events"` | Detailed trace | Debugging |

---

## 🎓 Next Steps

After mastering human-in-the-loop:
1. **Combine with Tools** - Add approval to tool-using agents
2. **Multi-Agent Systems** - Human oversight of agent collaboration
3. **Production Deployment** - Scale with proper checkpointing
4. **Monitoring** - Track approval rates and decisions

---

**💡 Tip:** Start with `command.ipynb` to understand dynamic routing, then progress through `input.ipynb` and `3_resume.ipynb` before tackling the production-ready `4_approval.ipynb` pattern.

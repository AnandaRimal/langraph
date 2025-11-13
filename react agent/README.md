# 🤖 ReAct Agent Implementations

This folder contains implementations of the ReAct (Reasoning + Acting) pattern using both LangChain and LangGraph, demonstrating different approaches to building intelligent agents.

## 📚 Notebooks Overview

### 1. **react agent_langchain.ipynb** - Traditional LangChain Approach
**Difficulty:** ⭐⭐ Intermediate  
**Framework:** LangChain  
**Concepts:** create_react_agent, AgentExecutor, tool integration

Traditional LangChain implementation:
- `create_react_agent` helper function
- `AgentExecutor` for running the agent
- Simpler API, less control
- Good for quick prototypes

**Use this when:** You need a fast, simple ReAct agent without custom flow control.

---

### 2. **react_agent_langraph.ipynb** - Modern LangGraph Approach  
**Difficulty:** ⭐⭐⭐ Advanced  
**Framework:** LangGraph  
**Concepts:** StateGraph, tool calling, conditional routing

Modern LangGraph implementation:
- Full control over agent flow
- Custom state management
- Conditional edge routing
- Tool node integration
- Transparent execution flow

**Use this when:** You need fine-grained control, custom logic, or want to extend agent behavior.

---

## 🎯 ReAct Pattern Explained

### What is ReAct?

**ReAct** = **Rea**soning + **Act**ing

A pattern where the LLM:
1. **Thinks** (Reasoning) - Analyzes the task
2. **Acts** (Action) - Uses tools to gather information
3. **Observes** - Sees the tool results
4. **Repeats** - Until the task is complete

### ReAct Loop

```
User Query
    ↓
┌───────────────┐
│ 1. Reasoning  │ "I need to search for X"
└───────┬───────┘
        ↓
┌───────────────┐
│ 2. Action     │ Call search_tool(X)
└───────┬───────┘
        ↓
┌───────────────┐
│ 3. Observation│ Tool returns results
└───────┬───────┘
        ↓
    [Complete?]
    ↙         ↘
  YES         NO
   ↓           ↓
  END      Repeat loop
```

---

## 📊 LangChain vs LangGraph Comparison

| Aspect | LangChain | LangGraph |
|--------|-----------|-----------|
| **Complexity** | ⭐⭐ Simple | ⭐⭐⭐ More complex |
| **Control** | Limited | Full control |
| **Customization** | Constrained | Highly flexible |
| **Transparency** | Black box | Transparent flow |
| **Learning Curve** | Easy | Steeper |
| **Production** | ⚠️ Limited | ✅ Recommended |
| **State Management** | Automatic | Manual but powerful |
| **Debugging** | Harder | Easier (visible flow) |

---

## 🔑 Key Differences

### LangChain Approach
```python
# Simple, opinionated
from langchain.agents import create_react_agent, AgentExecutor

agent = create_react_agent(llm, tools, prompt)
executor = AgentExecutor(agent=agent, tools=tools)
result = executor.invoke({"input": query})
```

**Pros:**
- ✅ Quick setup
- ✅ Less code
- ✅ Good for simple use cases

**Cons:**
- ❌ Limited customization
- ❌ Hard to debug
- ❌ Can't modify flow easily

### LangGraph Approach
```python
# Explicit, customizable
from langgraph.graph import StateGraph
from langgraph.prebuilt import ToolNode

# Define state
class AgentState(TypedDict):
    messages: Annotated[list, add_messages]

# Build graph
graph = StateGraph(AgentState)
graph.add_node("agent", agent_node)
graph.add_node("tools", ToolNode(tools))
graph.add_conditional_edges("agent", should_continue)
app = graph.compile()
```

**Pros:**
- ✅ Full transparency
- ✅ Easy to customize
- ✅ Better debugging
- ✅ Can add checkpointing, human-in-loop, etc.

**Cons:**
- ❌ More code
- ❌ Steeper learning curve

---

## 🎓 Learning Path

```
1. react agent_langchain.ipynb
   ↓ (Understand ReAct pattern)
   - See how agents think + act
   - Learn tool integration
   
2. react_agent_langraph.ipynb
   ↓ (Master control and customization)
   - Build custom agent flows
   - Add checkpointing
   - Implement human oversight
```

---

## 🛠️ Tool Integration

Both approaches use tools the same way:

```python
from langchain_community.tools import TavilySearchResults

search = TavilySearchResults(max_results=3)
tools = [search]
```

### Common Tools
- **TavilySearch** - Web search
- **WikipediaQuery** - Wikipedia lookup
- **Calculator** - Math operations
- **PythonREPL** - Execute Python code
- **Custom Tools** - Your own functions

---

## 🔄 Execution Flow Comparison

### LangChain
```
User → AgentExecutor (black box) → Result
          ↓
    [Hidden loop of think/act/observe]
```

### LangGraph
```
User → agent node → [need tools?] → tool node → agent → Result
         ↓               ↓              ↓          ↓
       Think           YES            Act       Observe
                       ↓
                      NO
                       ↓
                     END
```

---

## 💡 When to Use Which

### Use LangChain ReAct When:
- ✅ Prototyping quickly
- ✅ Simple question-answering
- ✅ Don't need custom logic
- ✅ Standard tool usage

### Use LangGraph ReAct When:
- ✅ Production deployment
- ✅ Need custom flow control
- ✅ Want to add checkpointing
- ✅ Require human oversight
- ✅ Complex multi-step reasoning
- ✅ Need to debug agent behavior

---

## 🚀 Advanced Extensions (LangGraph Only)

### Add Memory
```python
from langgraph.checkpoint.memory import MemorySaver

memory = MemorySaver()
app = graph.compile(checkpointer=memory)
```

### Add Human Approval
```python
app = graph.compile(
    checkpointer=memory,
    interrupt_before=["tools"]
)
```

### Stream Execution
```python
for event in app.stream(input, stream_mode="values"):
    print(event["messages"][-1])
```

---

## 📖 Resources

- [ReAct Paper](https://arxiv.org/abs/2210.03629)
- [LangChain Agents](https://python.langchain.com/docs/modules/agents/)
- [LangGraph ReAct](https://langchain-ai.github.io/langgraph/tutorials/introduction/)

---

## 🎯 Next Steps

After mastering ReAct agents:
1. **Reflection Agents** (`../Basic reflection agent/`) - Self-improving agents
2. **Multi-Agent Systems** - Collaborative agent architectures
3. **Custom Tools** - Build domain-specific tools
4. **Production Deployment** - Scale with proper observability

---

**💡 Tip:** Start with `react agent_langchain.ipynb` to understand the ReAct pattern quickly, then move to `react_agent_langraph.ipynb` for production-ready implementations with full control.

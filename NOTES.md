# 📚 LangGraph Learning Repository - Complete Guide

A comprehensive collection of LangGraph examples, from basics to advanced patterns, demonstrating how to build stateful AI applications with LangChain and LangGraph.

---

## 🗂️ Repository Structure

```
langraph/
├── stategtaph/              # StateGraph fundamentals
├── chatbot/                 # Chatbot implementations
├── humman in the loop/      # Human oversight patterns
├── react agent/             # ReAct agent implementations
├── Basic reflection agent/  # Self-improving agents
└── langchain vs langraph/   # Framework comparison
```

---

## 🎯 Learning Paths

### 🌱 Beginner Path (Start Here!)
```
1. stategtaph/basicstate.ipynb          # Learn StateGraph basics
2. chatbot/basic.ipynb                   # Simple chatbot
3. stategtaph/complexstate.ipynb        # Advanced state management
4. chatbot/chatbot_checkpoint_memory.ipynb  # Add memory
```

**Time:** 4-6 hours  
**Outcome:** Understand core LangGraph concepts and build basic chatbots

---

### 🌿 Intermediate Path
```
1. chatbot/chatbotwith_tools.ipynb      # Tool integration
2. humman in the loop/command.ipynb     # Dynamic routing
3. humman in the loop/input.ipynb       # Human feedback
4. react agent/react_agent_langchain.ipynb  # ReAct pattern
```

**Time:** 6-8 hours  
**Outcome:** Build agents with tools and human oversight

---

### 🌳 Advanced Path
```
1. react agent/react_agent_langraph.ipynb  # Advanced ReAct
2. humman in the loop/3_resume.ipynb       # Resume patterns
3. humman in the loop/4_approval.ipynb     # Production workflows
4. Basic reflection agent/basic_reflection_agent.ipynb  # Self-improvement
5. Basic reflection agent/reflexion_agent.ipynb  # Multi-trial learning
```

**Time:** 8-12 hours  
**Outcome:** Production-ready patterns and advanced techniques

---

### 🏆 Expert Path (Production)
```
1. chatbot/chat_with_sqlite.ipynb       # Persistent storage
2. chatbot/reddismemory.ipynb           # Distributed systems
3. All reflection notebooks              # Self-improving systems
4. Custom implementations                # Build your own patterns
```

**Time:** 12+ hours  
**Outcome:** Deploy scalable, production-grade AI systems

---

## 📁 Folder Details

### 1. 🎯 [stategtaph/](stategtaph/)
**Core Concepts:** StateGraph, nodes, edges, reducers

| Notebook | Difficulty | Key Concepts |
|----------|-----------|--------------|
| `basicstate.ipynb` | ⭐ Beginner | StateGraph, conditional edges, loops |
| `complexstate.ipynb` | ⭐⭐ Intermediate | Reducers, state aggregation, multiple fields |

**Start here** to understand the foundation of all LangGraph applications.

---

### 2. 💬 [chatbot/](chatbot/)
**Core Concepts:** Conversations, tools, memory, persistence

| Notebook | Difficulty | Key Concepts |
|----------|-----------|--------------|
| `basic.ipynb` | ⭐ Beginner | Simple chatbot, add_messages |
| `chatbotwith_tools.ipynb` | ⭐⭐ Intermediate | Tool integration, conditional routing |
| `chatbot_checkpoint_memory.ipynb` | ⭐⭐ Intermediate | MemorySaver, checkpointing |
| `chat_with_sqlite.ipynb` | ⭐⭐⭐ Advanced | SQLite persistence, durable storage |
| `reddismemory.ipynb` | ⭐⭐⭐ Advanced | Redis cloud, distributed systems |

**Progressive complexity:** Build from basic chat to production-ready systems.

---

### 3. 🙋 [humman in the loop/](humman%20in%20the%20loop/)
**Core Concepts:** Human oversight, approvals, interruptions

| Notebook | Difficulty | Key Concepts |
|----------|-----------|--------------|
| `command.ipynb` | ⭐⭐ Intermediate | Command object, dynamic routing |
| `input.ipynb` | ⭐⭐ Intermediate | interrupt(), human input |
| `3_resume.ipynb` | ⭐⭐⭐ Advanced | Resume patterns, multi-path decisions |
| `4_approval.ipynb` | ⭐⭐⭐ Advanced | interrupt_before, production workflows |

**Essential for production:** Add human control and safety to AI systems.

---

### 4. 🤖 [react agent/](react%20agent/)
**Core Concepts:** Reasoning + Acting, tool usage, agent loops

| Notebook | Difficulty | Key Concepts |
|----------|-----------|--------------|
| `react agent_langchain.ipynb` | ⭐⭐ Intermediate | LangChain ReAct, AgentExecutor |
| `react_agent_langraph.ipynb` | ⭐⭐⭐ Advanced | LangGraph ReAct, full control |

**Compare approaches:** Understand when to use LangChain vs LangGraph.

---

### 5. 🔄 [Basic reflection agent/](Basic%20reflection%20agent/)
**Core Concepts:** Self-critique, iterative improvement, learning

| Notebook | Difficulty | Key Concepts |
|----------|-----------|--------------|
| `basic_reflection_agent.ipynb` | ⭐⭐⭐ Advanced | Generate-reflect loop, quality improvement |
| `reflexion_agent.ipynb` | ⭐⭐⭐⭐ Expert | Multi-trial learning, persistent memory |

**Self-improving AI:** Build systems that learn and refine outputs.

---

## 🔑 Core Concepts Index

### StateGraph Fundamentals
- **What:** Container for workflow logic
- **Where:** `stategtaph/basicstate.ipynb`
- **Why:** Foundation of all LangGraph applications

### State Management
- **What:** Data that flows between nodes
- **Where:** All notebooks
- **Key Pattern:** `TypedDict` with reducers

### Reducers
- **What:** Control how state updates merge
- **Where:** `stategtaph/complexstate.ipynb`
- **Types:** `operator.add`, `operator.concat`, `add_messages`

### Nodes
- **What:** Processing functions that update state
- **Where:** All notebooks
- **Pattern:** `def node(state) -> state_update`

### Edges
- **What:** Connections between nodes
- **Types:** Static, Conditional
- **Where:** All notebooks

### Checkpointing
- **What:** Saving state between runs
- **Where:** `chatbot/chatbot_checkpoint_memory.ipynb`
- **Types:** MemorySaver, SqliteSaver, RedisSaver

### Tools
- **What:** External functions agents can call
- **Where:** `chatbot/chatbotwith_tools.ipynb`, ReAct agents
- **Examples:** Web search, calculations, databases

### Human-in-the-Loop
- **What:** Human oversight and control
- **Where:** `humman in the loop/` folder
- **Patterns:** Command, interrupt(), interrupt_before

### ReAct Pattern
- **What:** Reasoning + Acting loop
- **Where:** `react agent/` folder
- **Flow:** Think → Act → Observe → Repeat

### Reflection
- **What:** Self-critique and improvement
- **Where:** `Basic reflection agent/` folder
- **Patterns:** Reflection (single-run), Reflexion (multi-trial)

---

## 🎓 Key Patterns Reference

### 1. Basic Chatbot
```python
from langgraph.graph import StateGraph, END, add_messages

class State(TypedDict):
    messages: Annotated[list, add_messages]

def chatbot(state):
    return {"messages": [llm.invoke(state["messages"])]}

graph = StateGraph(State)
graph.add_node("chatbot", chatbot)
graph.set_entry_point("chatbot")
graph.add_edge("chatbot", END)
app = graph.compile()
```

### 2. Chatbot with Tools
```python
from langgraph.prebuilt import ToolNode

def should_use_tools(state):
    last_msg = state["messages"][-1]
    if last_msg.tool_calls:
        return "tools"
    return END

graph.add_node("tools", ToolNode(tools))
graph.add_conditional_edges("chatbot", should_use_tools)
graph.add_edge("tools", "chatbot")
```

### 3. With Memory
```python
from langgraph.checkpoint.memory import MemorySaver

memory = MemorySaver()
app = graph.compile(checkpointer=memory)

config = {"configurable": {"thread_id": "user123"}}
app.invoke(input, config)
```

### 4. Human Approval
```python
app = graph.compile(
    checkpointer=memory,
    interrupt_before=["critical_node"]
)

# First run - pauses before critical_node
app.invoke(input, config)

# Resume after approval
app.stream(None, config)
```

### 5. Reflection Loop
```python
def should_reflect(state):
    if quality_check(state):
        return END
    return "generate"

graph.add_node("generate", generate)
graph.add_node("reflect", reflect)
graph.add_conditional_edges("reflect", should_reflect)
```

---

## 📊 Technology Stack

### Frameworks
- **LangGraph** - State-based workflows
- **LangChain** - LLM integrations
- **LangChain Community** - Tools and utilities

### LLMs
- **Google Gemini** (primary)
- **OpenAI GPT** (examples)
- **Groq** (fast inference)

### Storage
- **MemorySaver** - In-memory (development)
- **SqliteSaver** - File-based (production)
- **RedisSaver** - Distributed (scale)

### Tools
- **TavilySearch** - Web search
- **Python REPL** - Code execution
- **Custom tools** - Domain-specific

---

## 🎯 Use Case Matrix

| Use Case | Notebooks | Difficulty | Time |
|----------|-----------|------------|------|
| **Simple Q&A Bot** | basic.ipynb | ⭐ | 1h |
| **Research Assistant** | chatbotwith_tools.ipynb, react_agent | ⭐⭐ | 3h |
| **Customer Support** | checkpoint_memory, approval | ⭐⭐⭐ | 6h |
| **Content Generator** | reflection_agent | ⭐⭐⭐ | 4h |
| **Code Assistant** | reflexion, tools | ⭐⭐⭐⭐ | 8h |
| **Multi-Agent System** | All advanced patterns | ⭐⭐⭐⭐ | 12h+ |

---

## 🚀 Quick Start Guides

### Build Your First Chatbot (15 minutes)
```bash
# 1. Navigate to basics
cd chatbot/

# 2. Open basic.ipynb
# 3. Run all cells
# 4. Chat with your bot!
```

### Add Web Search (30 minutes)
```bash
# 1. Complete basic chatbot
# 2. Open chatbotwith_tools.ipynb
# 3. Get Tavily API key
# 4. Run and test web search
```

### Add Memory (45 minutes)
```bash
# 1. Complete tools chatbot
# 2. Open chatbot_checkpoint_memory.ipynb
# 3. Test multi-turn conversations
# 4. Observe context retention
```

---

## 🎨 Architecture Patterns

### Linear Flow
```
START → node_a → node_b → node_c → END
```
**Example:** basic.ipynb

### Conditional Flow
```
START → node_a → [decision] → node_b or node_c → END
```
**Example:** chatbotwith_tools.ipynb

### Loop Flow
```
START → node_a → [check] → continue? → node_a or END
```
**Example:** basicstate.ipynb, reflection_agent.ipynb

### Human-in-Loop Flow
```
START → node_a → [PAUSE] → human_input → node_b → END
```
**Example:** 4_approval.ipynb, input.ipynb

---

## 🔧 Environment Setup

### Required Packages
```bash
pip install langgraph langchain langchain-google-genai
pip install langchain-community tavily-python
pip install python-dotenv
```

### API Keys (.env file)
```bash
GOOGLE_API_KEY=your_gemini_key
TAVILY_API_KEY=your_tavily_key
OPENAI_API_KEY=your_openai_key  # optional
```

### Database Setup (Optional)
```bash
# For SQLite
# No setup needed - auto-created

# For Redis
REDIS_URL=rediss://user:pass@host:port
```

---

## 📖 Additional Resources

### Official Documentation
- [LangGraph Docs](https://langchain-ai.github.io/langgraph/)
- [LangChain Docs](https://python.langchain.com/)
- [Google Gemini](https://ai.google.dev/)

### Research Papers
- [ReAct](https://arxiv.org/abs/2210.03629) - Reasoning + Acting
- [Reflexion](https://arxiv.org/abs/2303.11366) - Verbal Reinforcement Learning
- [Self-Refine](https://arxiv.org/abs/2303.17651) - Iterative Refinement

### Community
- [LangChain Discord](https://discord.gg/langchain)
- [GitHub Discussions](https://github.com/langchain-ai/langgraph/discussions)

---

## 🎯 Next Steps

### After Completing This Repository

1. **Build Your Own Project**
   - Identify a real problem
   - Choose appropriate patterns
   - Implement and iterate

2. **Explore Advanced Topics**
   - Multi-agent systems
   - Custom tools
   - Performance optimization
   - Production deployment

3. **Contribute**
   - Share your implementations
   - Help others learn
   - Improve documentation

---

## 💡 Best Practices

### Development
- ✅ Start simple, add complexity gradually
- ✅ Test each component independently
- ✅ Use checkpointing for debugging
- ✅ Log state transitions

### Production
- ✅ Use persistent checkpointers (SQLite/Redis)
- ✅ Implement proper error handling
- ✅ Add human-in-the-loop for critical operations
- ✅ Monitor costs and performance
- ✅ Set iteration limits

### Learning
- ✅ Follow the learning paths
- ✅ Run all code examples
- ✅ Modify and experiment
- ✅ Build your own projects

---

## 🤝 Contributing

Found an issue or want to add examples?
1. Open an issue
2. Submit a pull request
3. Share your learnings

---

## 📝 Notes

- All notebooks are self-contained
- Each folder has its own README
- Code examples are production-ready patterns
- Start with basics before advanced topics

---

**🎉 Happy Learning!** Start with `stategtaph/basicstate.ipynb` and build your way to advanced AI systems!

---

## 📞 Support

Questions? Check the READMEs in each folder or review the specific notebooks for detailed explanations.

**Last Updated:** November 2025  
**LangGraph Version:** Latest  
**Python Version:** 3.11+

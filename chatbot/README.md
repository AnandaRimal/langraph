# 💬 LangGraph Chatbot Examples

This folder contains progressive examples of building chatbots with LangGraph, from basic implementations to advanced features like memory persistence and tool integration.

## 📚 Notebooks Overview

### 1. **basic.ipynb** - Foundation
**Difficulty:** ⭐ Beginner  
**Concepts:** State, add_messages, basic LLM integration

A simple chatbot that demonstrates:
- Basic StateGraph structure
- Message history management with `add_messages`
- Google Gemini LLM integration
- Interactive chat loop

**Use this when:** Learning LangGraph fundamentals or building simple conversational AI.

---

### 2. **chatbotwith_tools.ipynb** - Tool Integration
**Difficulty:** ⭐⭐ Intermediate  
**Concepts:** Tool calling, conditional routing, ToolNode

Extends the basic chatbot with:
- Tavily web search integration
- Conditional edge routing based on tool calls
- ToolNode for executing external functions
- Dynamic decision-making (when to search vs. respond)

**Use this when:** Building chatbots that need external information or actions.

---

### 3. **chatbot_checkpoint_memory.ipynb** - Session Persistence
**Difficulty:** ⭐⭐ Intermediate  
**Concepts:** MemorySaver, checkpointing, thread management

Adds memory persistence:
- MemorySaver for in-memory state storage
- Thread IDs for multi-user sessions
- Conversation continuity across invocations
- State checkpointing between runs

**Use this when:** Building multi-turn conversations that need context across interactions.

---

### 4. **chat_with_sqlite.ipynb** - Durable Storage
**Difficulty:** ⭐⭐⭐ Advanced  
**Concepts:** SQLiteSaver, persistent checkpoints, database storage

Production-ready memory:
- SQLite database for persistent storage
- Conversations survive process restarts
- Long-term memory retention
- Scalable checkpoint management

**Use this when:** Deploying production chatbots that need permanent conversation history.

---

### 5. **reddismemory.ipynb** - Cloud Storage
**Difficulty:** ⭐⭐⭐ Advanced  
**Concepts:** RedisSaver, cloud storage, distributed systems

Enterprise-grade memory:
- Redis cloud integration
- Distributed checkpoint storage
- Multi-instance deployment support
- High-availability memory backend

**Use this when:** Building scalable, distributed chatbot systems.

---

## 🎯 Learning Path

```
1. basic.ipynb
   ↓ (Add tools)
2. chatbotwith_tools.ipynb
   ↓ (Add memory)
3. chatbot_checkpoint_memory.ipynb
   ↓ (Make persistent)
4. chat_with_sqlite.ipynb
   ↓ (Scale up)
5. reddismemory.ipynb
```

## 📊 Feature Comparison

| Feature | basic | with_tools | checkpoint | sqlite | redis |
|---------|-------|------------|------------|--------|-------|
| Simple Chat | ✅ | ✅ | ✅ | ✅ | ✅ |
| Web Search | ❌ | ✅ | ✅ | ✅ | ✅ |
| Session Memory | ❌ | ❌ | ✅ | ✅ | ✅ |
| Persistent Storage | ❌ | ❌ | ❌ | ✅ | ✅ |
| Multi-instance | ❌ | ❌ | ❌ | ❌ | ✅ |
| Production Ready | ❌ | ⚠️ | ⚠️ | ✅ | ✅ |

## 🔑 Key Concepts

### State Management
All chatbots use `add_messages` reducer for automatic message list management.

### Memory Types
- **No Memory**: Stateless, forgets after each run
- **MemorySaver**: In-memory, lost on restart
- **SqliteSaver**: Persistent, file-based storage
- **RedisSaver**: Distributed, cloud-based storage

### Tool Integration
Tools extend chatbot capabilities by connecting to external APIs and services.

## 🚀 Quick Start

### Basic Chatbot
```python
from langgraph.graph import StateGraph
from langchain_google_genai import ChatGoogleGenerativeAI

# Define state, node, build graph
# Run chat loop
```

### With Memory
```python
from langgraph.checkpoint.memory import MemorySaver

memory = MemorySaver()
app = graph.compile(checkpointer=memory)
```

### With Tools
```python
from langgraph.prebuilt import ToolNode
from langchain_community.tools import TavilySearchResults

tools = [TavilySearchResults(max_results=2)]
llm_with_tools = llm.bind_tools(tools)
```

## 📖 Resources

- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [Checkpointing Guide](https://langchain-ai.github.io/langgraph/concepts/persistence/)
- [Tool Integration](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/)

---

**💡 Tip:** Start with `basic.ipynb` and progressively add features as you understand each concept.

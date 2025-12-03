# LangGraph Examples & Tutorials

A comprehensive collection of LangGraph examples demonstrating agent architectures, from basic concepts to advanced multi-agent systems.

## 📚 Table of Contents

1. [Introduction](#1-introduction)
2. [Basic Reflection System](#2-basic-reflection-system)
3. [Structured Outputs](#3-structured-outputs)
4. [Reflexion Agent System](#4-reflexion-agent-system)
5. [State Deep Dive](#5-state-deep-dive)
6. [ReAct Agent](#6-react-agent)
7. [Chatbot](#7-chatbot)
8. [Human-in-the-Loop](#8-human-in-the-loop)
9. [RAG Agent](#9-rag-agent)
10. [Multi-Agent Architecture](#10-multi-agent-architecture)
11. [Streaming](#11-streaming)

## 🚀 Getting Started

### Prerequisites

```bash
# Python 3.14+ required
python --version
```

### Installation

```bash
# Install dependencies
pip install -e .
```

### Environment Setup

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_openai_key
GROQ_API_KEY=your_groq_key
TAVILY_API_KEY=your_tavily_key
GOOGLE_API_KEY=your_google_key
```

## 📖 Examples Overview

### 1. Introduction
**Path**: `1_Introduction/`

Introduction to the ReAct (Reasoning and Acting) pattern using LangChain agents.

**Key Concepts**:
- ReAct agent loop
- Tool integration (Tavily Search, custom tools)
- Basic agent reasoning

[View README](1_Introduction/README.md)

---

### 2. Basic Reflection System
**Path**: `2_basic_reflection_system/`

An agent that improves outputs through self-critique and iteration.

**Key Concepts**:
- Generator-Reflector cycle
- Self-improvement through critique
- Iterative refinement

[View README](2_basic_reflection_system/README.md)

---

### 3. Structured Outputs
**Path**: `3_structured_outputs/`

Generate structured data from LLMs using Pydantic, TypedDict, and JSON Schema.

**Key Concepts**:
- Pydantic models
- TypedDict annotations
- JSON schema validation

[View README](3_structured_outputs/README.md)

---

### 4. Reflexion Agent System
**Path**: `4_reflexion_agent_system/`

Advanced reflection with external tool integration for information gathering.

**Key Concepts**:
- Draft → Execute → Revise cycle
- Tool-enhanced reflection
- Search-driven improvement

[View README](4_reflexion_agent_system/README.md)

---

### 5. State Deep Dive
**Path**: `5_state_deepdive/`

Understanding state management in LangGraph.

**Key Concepts**:
- Basic state (overwrite)
- Complex state (reducers)
- State aggregation patterns

[View README](5_state_deepdive/README.md)

---

### 6. ReAct Agent
**Path**: `6_react_agent/`

Custom ReAct implementation using LangGraph's StateGraph.

**Key Concepts**:
- StateGraph architecture
- Custom node implementation
- AgentAction vs AgentFinish

[View README](6_react_agent/README.md)

---

### 7. Chatbot
**Path**: `7_chatbot/`

Four chatbot implementations with progressive enhancements.

**Key Concepts**:
- Basic chatbot (stateless)
- Tool-calling chatbot
- Memory with MemorySaver
- Persistence with SqliteSaver

[View README](7_chatbot/README.md)

---

### 8. Human-in-the-Loop
**Path**: `8_human-in-the-loop/`

Interactive agents that request human input and approval.

**Key Concepts**:
- `input()` for simple HITL
- Command API
- Interrupt and resume patterns
- Approval workflows

[View README](8_human-in-the-loop/README.md)

---

### 9. RAG Agent
**Path**: `9_RAG_agent/`

Retrieval-Augmented Generation for knowledge-based answers.

**Key Concepts**:
- Basic RAG pipeline
- Classification-driven routing
- RAG as a tool
- Multi-step reasoning

[View README](9_RAG_agent/README.md)

---

### 10. Multi-Agent Architecture
**Path**: `10_multi_agent_architecture/`

Systems where multiple specialized agents collaborate.

**Key Concepts**:
- Subgraphs for modularity
- Supervisor pattern
- Agent orchestration

[View README](10_multi_agent_architecture/README.md)

---

### 11. Streaming
**Path**: `11_streaming/`

Real-time output streaming for better UX.

**Key Concepts**:
- Node output streaming
- Event streaming
- Token-level streaming

[View README](11_streaming/README.md)

---

## 🎓 Learning Path

We recommend following this progression:

### Beginner
1. **Introduction** - Understand ReAct basics
2. **State Deep Dive** - Learn state management
3. **Chatbot** - Build conversational agents

### Intermediate
4. **Basic Reflection System** - Self-improving agents
5. **Structured Outputs** - Typed LLM responses
6. **ReAct Agent** - Custom graph implementation
7. **Streaming** - Real-time outputs

### Advanced
8. **Reflexion Agent System** - Tool-enhanced reflection
9. **Human-in-the-Loop** - Interactive workflows
10. **RAG Agent** - Knowledge-based systems
11. **Multi-Agent Architecture** - Collaborative agents

## 🛠️ Tech Stack

- **LangGraph**: Agent workflow orchestration
- **LangChain**: LLM abstractions and tools
- **OpenAI / Groq**: LLM providers
- **Tavily**: Search API
- **Google Gemini**: Alternative LLM provider

## 📝 Project Structure

```
langraph/
├── 1_Introduction/
│   ├── README.md
│   └── react_agent_basic.py
├── 2_basic_reflection_system/
│   ├── README.md
│   ├── basic.py
│   └── chains.py
├── 3_structured_outputs/
│   ├── README.md
│   └── types.ipynb
├── 4_reflexion_agent_system/
│   ├── README.md
│   ├── reflexion_graph.py
│   ├── chains.py
│   ├── execute_tools.py
│   └── schema.py
├── 5_state_deepdive/
│   ├── README.md
│   ├── 1_basic_state.py
│   └── 2_complex_state.py
├── 6_react_agent/
│   ├── README.md
│   ├── react_graph.py
│   ├── nodes.py
│   ├── agent_reason_runnable.py
│   └── react_state.py
├── 7_chatbot/
│   ├── README.md
│   ├── 1_basic_chatbot.py
│   ├── 2_chatbot_with_tools.py
│   ├── 3_chat_with_in_memory_checkpointer.py
│   └── 4_chat_with_sqlite_checkpointer.py
├── 8_human-in-the-loop/
│   ├── README.md
│   ├── 1_using_input().py
│   ├── 2_command.ipynb
│   ├── 3_resume.ipynb
│   ├── 4_approval.ipynb
│   └── 5_multiturn_conversation.py
├── 9_RAG_agent/
│   ├── README.md
│   ├── 1_basic.ipynb
│   ├── 2_classification_driven_agent.ipynb
│   ├── 3_rag_powered_tool_calling.ipynb
│   └── 4_advanced_multi_step_reasoning.ipynb
├── 10_multi_agent_architecture/
│   ├── README.md
│   ├── 1_subgraphs.ipynb
│   └── 2_supervisor_multiagent_workflow.ipynb
├── 11_streaming/
│   ├── README.md
│   └── 1_stream_events.ipynb
├── pyproject.toml
└── README.md
```

## 🤝 Contributing

Feel free to add more examples or improve existing ones!

## 📄 License

This project is for educational purposes.

## 🔗 Resources

- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [LangChain Documentation](https://python.langchain.com/)
- [ReAct Paper](https://arxiv.org/abs/2210.03629)
- [Reflexion Paper](https://arxiv.org/abs/2303.11366)

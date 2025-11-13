# 🚀 LangGraph Learning Repository

A comprehensive, hands-on collection of LangGraph tutorials and examples - from basics to production-ready patterns.

## 📚 What's Inside

This repository contains **15+ Jupyter notebooks** organized into **5 focused folders**, covering everything from simple chatbots to self-improving AI agents.

### 🗂️ Repository Structure

```
📁 stategtaph/              ⭐ Start Here - StateGraph fundamentals
📁 chatbot/                 💬 Build chatbots with tools & memory
📁 humman in the loop/      🙋 Add human oversight & approvals
📁 react agent/             🤖 Reasoning + Acting agents
📁 Basic reflection agent/  🔄 Self-improving AI systems
```

---

## 🎯 Quick Start

### For Complete Beginners
```
1. Read NOTES.md (complete guide)
2. Start with stategtaph/basicstate.ipynb
3. Build your first chatbot: chatbot/basic.ipynb
4. Follow the beginner learning path
```

### For Intermediate Developers
```
1. Review chatbot/chatbotwith_tools.ipynb
2. Explore humman in the loop/ patterns
3. Build a ReAct agent
```

### For Advanced Users
```
1. Production patterns in chatbot/chat_with_sqlite.ipynb
2. Human approval workflows in humman in the loop/4_approval.ipynb
3. Self-improving agents in Basic reflection agent/
```

---

## 📖 Complete Documentation

### **[📚 NOTES.md](NOTES.md)** - Master Guide
**Your complete learning companion!**
- All learning paths (beginner → expert)
- Complete pattern reference
- Code examples for every concept
- Use case matrix
- Best practices

### Folder READMEs
Each folder contains a detailed README with:
- ✅ Notebook descriptions
- ✅ Key concepts explained
- ✅ Comparison tables
- ✅ Code patterns
- ✅ When to use each approach

---

## 🎓 Learning Paths

### 🌱 Beginner (4-6 hours)
```
stategtaph/basicstate.ipynb → chatbot/basic.ipynb → 
stategtaph/complexstate.ipynb → chatbot/chatbot_checkpoint_memory.ipynb
```
**Outcome:** Build basic chatbots with state management

### 🌿 Intermediate (6-8 hours)
```
chatbot/chatbotwith_tools.ipynb → humman in the loop/command.ipynb → 
humman in the loop/input.ipynb → react agent/react_agent_langchain.ipynb
```
**Outcome:** Agents with tools and human oversight

### 🌳 Advanced (8-12 hours)
```
react agent/react_agent_langraph.ipynb → humman in the loop/3_resume.ipynb → 
humman in the loop/4_approval.ipynb → Basic reflection agent/
```
**Outcome:** Production-ready AI systems

---

## 🔥 Featured Notebooks

### Must-Start: **stategtaph/basicstate.ipynb**
Understanding StateGraph fundamentals - the foundation of everything.

### Most Practical: **chatbot/chatbotwith_tools.ipynb**
Build chatbots that can search the web and use external tools.

### Production-Ready: **humman in the loop/4_approval.ipynb**
Enterprise-grade approval workflows for safe AI deployment.

### Most Advanced: **Basic reflection agent/reflexion_agent.ipynb**
Self-improving AI that learns from failures across multiple trials.

---

## 🛠️ Setup

### 1. Install Dependencies
```bash
pip install langgraph langchain langchain-google-genai
pip install langchain-community tavily-python python-dotenv
```

### 2. Configure API Keys
Create a `.env` file:
```bash
GOOGLE_API_KEY=your_gemini_api_key
TAVILY_API_KEY=your_tavily_api_key  # For web search
```

### 3. Start Learning
```bash
# Open first notebook
jupyter notebook stategtaph/basicstate.ipynb
```

---

## 📊 What You'll Learn

| Concept | Notebooks | Difficulty |
|---------|-----------|------------|
| **StateGraph Basics** | stategtaph/ | ⭐ |
| **Chatbots** | chatbot/ | ⭐⭐ |
| **Tool Integration** | chatbot/, react agent/ | ⭐⭐ |
| **Memory & Persistence** | chatbot/ | ⭐⭐ |
| **Human Oversight** | humman in the loop/ | ⭐⭐⭐ |
| **ReAct Agents** | react agent/ | ⭐⭐⭐ |
| **Self-Improvement** | Basic reflection agent/ | ⭐⭐⭐⭐ |

---

## 🎯 Use Cases Covered

- ✅ **Q&A Chatbots** - Simple conversational AI
- ✅ **Research Assistants** - Web-connected agents
- ✅ **Customer Support** - Multi-turn conversations with memory
- ✅ **Content Generators** - Self-improving writing systems
- ✅ **Code Assistants** - ReAct agents for programming
- ✅ **Approval Workflows** - Production-safe AI operations

---

## 🌟 Key Features

- **15+ Complete Notebooks** - Every concept explained
- **Progressive Complexity** - Start simple, build up
- **Production Patterns** - Real-world implementations
- **No Code Omitted** - Full working examples
- **Comprehensive Docs** - NOTES.md + folder READMEs
- **Multiple LLMs** - Gemini, GPT, Groq examples

---

## 📚 Resources

### Documentation
- **[NOTES.md](NOTES.md)** - Complete learning guide
- **Folder READMEs** - Detailed concept explanations
- **Inline Code Comments** - Every example explained

### External Links
- [LangGraph Official Docs](https://langchain-ai.github.io/langgraph/)
- [LangChain Documentation](https://python.langchain.com/)
- [Google Gemini API](https://ai.google.dev/)

### Research Papers
- [ReAct: Synergizing Reasoning and Acting](https://arxiv.org/abs/2210.03629)
- [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366)

---

## 🎓 Recommended Order

1. **Read [NOTES.md](NOTES.md)** - Understand the big picture
2. **Choose Your Path** - Beginner, Intermediate, or Advanced
3. **Follow Folder READMEs** - Detailed guidance in each section
4. **Run All Notebooks** - Hands-on learning
5. **Build Your Own** - Apply to real projects

---

## 💡 Philosophy

This repository follows a **learn-by-doing** approach:
- ✅ Every concept has a working example
- ✅ Complexity increases gradually
- ✅ Production patterns emphasized
- ✅ No shortcuts - understand the fundamentals

---

## 🤝 Contributing

Found this helpful? Consider:
- ⭐ Starring this repository
- 🐛 Reporting issues
- 💡 Suggesting improvements
- 📖 Sharing with others

---

## 📝 License

MIT License - Feel free to use these examples in your projects!

---

## 🚀 Get Started Now!

```bash
# 1. Clone the repository
git clone https://github.com/AnandaRimal/langraph.git

# 2. Install dependencies
pip install langgraph langchain langchain-google-genai
pip install langchain-community tavily-python python-dotenv

# 3. Read the master guide
cat NOTES.md

# 4. Start learning!
jupyter notebook stategtaph/basicstate.ipynb
```

---

**🎉 Happy Learning!** Go from zero to building production AI agents in days, not months.

**Questions?** Check [NOTES.md](NOTES.md) for comprehensive guidance on every topic.

---

**Last Updated:** November 2025  
**Maintained by:** [@AnandaRimal](https://github.com/AnandaRimal)
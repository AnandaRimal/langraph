# 🔄 Reflection & Reflexion Agents

This folder demonstrates self-improving AI agents that can critique and refine their own outputs - essential patterns for high-quality content generation and iterative problem-solving.

## 📚 Notebooks Overview

### 1. **basic_reflection_agent.ipynb** - Reflection Pattern
**Difficulty:** ⭐⭐⭐ Advanced  
**Concepts:** Generate-Reflect loop, self-critique, iterative refinement

Core reflection pattern:
- **Generate** node - Creates initial content
- **Reflect** node - Critiques the output
- **Conditional routing** - Continue refining or finish
- **Iterative improvement** - Multiple rounds of enhancement

**Example:** Tweet generator that refines content through self-reflection until quality criteria are met.

**Use this when:** Building systems that need to iteratively improve outputs (writing, code, analysis).

---

### 2. **reflexion_agent.ipynb** - Reflexion Pattern (Advanced)
**Difficulty:** ⭐⭐⭐⭐ Expert  
**Concepts:** Multi-trial learning, memory across attempts, failure analysis

Advanced self-improvement:
- **External Memory** - Stores learnings across trials
- **Trial-based learning** - Improves with each attempt
- **Failure analysis** - Learns from mistakes
- **Long-term memory** - Retains knowledge between runs

**Example:** Multi-trial problem solver that learns from failures and improves strategy over time.

**Use this when:** Complex tasks requiring learning from failures or multi-attempt problem-solving.

---

## 🎯 Reflection vs Reflexion

### Reflection (Single-run improvement)
```
Generate → Reflect → Improve → Reflect → ... → Done
   ↓          ↓          ↓
Draft    Critique   Better Draft
```

**Characteristics:**
- Single execution context
- Immediate improvements
- No memory between runs
- Perfect for content refinement

### Reflexion (Multi-trial learning)
```
Trial 1: Attempt → Fail → Analyze → Store Learning
                                          ↓
Trial 2: Attempt (using learnings) → Fail → Analyze → Store
                                                         ↓
Trial 3: Attempt (all learnings) → Success!
```

**Characteristics:**
- Multiple execution trials
- Learns from failures
- Persistent memory
- Perfect for complex problem-solving

---

## 📊 Pattern Comparison

| Aspect | Reflection | Reflexion |
|--------|-----------|-----------|
| **Scope** | Single run | Multiple trials |
| **Memory** | Temporary (within run) | Persistent (across trials) |
| **Learning** | Immediate refinement | Accumulative learning |
| **Use Case** | Content quality | Problem solving |
| **Complexity** | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Iterations** | Within one invoke | Across multiple invokes |
| **Failure Handling** | Improve immediately | Learn for next trial |

---

## 🔑 Key Concepts

### 1. Reflection Loop

```python
def generate(state):
    # Create initial output
    return {"draft": llm.invoke(prompt)}

def reflect(state):
    # Critique the draft
    critique = llm.invoke(f"Review: {state['draft']}")
    return {"reflections": [critique]}

def should_continue(state):
    # Check if good enough
    if quality_check(state):
        return END
    return "generate"  # Try again
```

**Benefits:**
- ✅ Self-improving outputs
- ✅ Quality assurance
- ✅ Iterative refinement
- ✅ No human review needed

### 2. Reflexion Pattern

```python
class ReflexionState(TypedDict):
    task: str
    attempts: List[str]
    reflections: List[str]  # Learnings from failures
    solution: Optional[str]

def actor(state):
    # Try to solve using past reflections
    context = "\n".join(state["reflections"])
    attempt = llm.invoke(f"Task: {state['task']}\nLearnings: {context}")
    return {"attempts": [attempt]}

def evaluator(state):
    # Check if solution works
    if is_correct(state["attempts"][-1]):
        return {"solution": state["attempts"][-1]}
    return {}

def self_reflect(state):
    # Analyze failure and store learning
    reflection = llm.invoke(f"Why failed: {state['attempts'][-1]}")
    return {"reflections": [reflection]}
```

**Benefits:**
- ✅ Learns from mistakes
- ✅ Improves over trials
- ✅ Persistent knowledge
- ✅ More robust solutions

---

## 🎭 Use Cases

### Reflection Pattern
- ✅ **Content Generation** - Blog posts, tweets, emails
- ✅ **Code Review** - Self-reviewing generated code
- ✅ **Writing Quality** - Iterative document improvement
- ✅ **Creative Work** - Refining ideas and outputs
- ✅ **Translation** - Improving translation quality

### Reflexion Pattern
- ✅ **Problem Solving** - Math, logic, algorithms
- ✅ **Code Generation** - Complex coding tasks
- ✅ **Strategic Planning** - Multi-step strategy development
- ✅ **Research Tasks** - Finding answers through iteration
- ✅ **Game Playing** - Learning winning strategies

---

## 🏗️ Architecture Patterns

### Basic Reflection Flow
```
START → generate → reflect → [good enough?]
           ↑                        ↓
           └──────── NO ────────────┘
                                    ↓ YES
                                   END
```

### Reflexion Flow
```
Trial 1:
START → actor → evaluator → [correct?]
                               ↓ NO
                          self_reflect → store learning
                               
Trial 2 (with learnings):
START → actor (using reflections) → evaluator → [correct?]
                                                    ↓ YES
                                                   END
```

---

## 🎓 Implementation Details

### Reflection State
```python
class ReflectionState(TypedDict):
    messages: Annotated[list, add_messages]
    # Messages include both drafts and reflections
```

### Reflexion State
```python
class ReflexionState(TypedDict):
    task: str
    attempts: List[str]  # All attempts
    reflections: List[str]  # Accumulated learnings
    iteration: int
    solution: Optional[str]
```

### Conditional Logic

```python
# Reflection
def should_continue(state):
    if meets_criteria(state["messages"][-1]):
        return END
    if len(state["messages"]) > MAX_ITERATIONS:
        return END
    return "generate"

# Reflexion
def should_continue(state):
    if state.get("solution"):
        return END
    if state["iteration"] >= MAX_TRIALS:
        return END
    return "actor"
```

---

## 🚀 Advanced Features

### Quality Metrics
```python
def assess_quality(content):
    # Check length, clarity, engagement
    score = llm.invoke(f"Rate 1-10: {content}")
    return int(score) >= 8
```

### Learning Storage
```python
# Persistent reflexion memory
from langgraph.checkpoint.sqlite import SqliteSaver

memory = SqliteSaver.from_conn_string("reflexion.db")
app = graph.compile(checkpointer=memory)
```

### Human Override
```python
app = graph.compile(
    checkpointer=memory,
    interrupt_before=["generate"]  # Review before each attempt
)
```

---

## 📊 Performance Comparison

| Metric | No Reflection | Reflection | Reflexion |
|--------|---------------|------------|-----------|
| **Quality** | ⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Speed** | Fast | Medium | Slow |
| **Cost** | Low | Medium | High |
| **Reliability** | Low | High | Very High |
| **Learning** | None | Per-run | Across runs |

---

## 🎓 Learning Path

```
1. basic_reflection_agent.ipynb
   ↓ (Master single-run improvement)
   - Understand generate-reflect loop
   - Implement quality checks
   - Practice iterative refinement
   
2. reflexion_agent.ipynb
   ↓ (Master multi-trial learning)
   - Add persistent memory
   - Implement failure analysis
   - Build learning systems
```

---

## 📖 Research Papers

- **Reflection**: "Self-Refine: Iterative Refinement with Self-Feedback"
- **Reflexion**: "Reflexion: Language Agents with Verbal Reinforcement Learning"

---

## 🎯 Next Steps

After mastering reflection patterns:
1. **Combine with Tools** - Self-improving agents with external tools
2. **Multi-Agent Collaboration** - Agents that critique each other
3. **Human-in-the-Loop** - Human feedback in reflection loop
4. **Production Deployment** - Scale with proper monitoring

---

## 💡 Best Practices

### For Reflection
1. Set maximum iterations (avoid infinite loops)
2. Define clear quality criteria
3. Use specific reflection prompts
4. Monitor LLM costs

### For Reflexion
1. Store learnings persistently
2. Limit trial attempts
3. Clear failure definitions
4. Track improvement metrics

---

**💡 Tip:** Start with `basic_reflection_agent.ipynb` for immediate output improvement, then explore `reflexion_agent.ipynb` for complex problem-solving that benefits from learning across attempts.

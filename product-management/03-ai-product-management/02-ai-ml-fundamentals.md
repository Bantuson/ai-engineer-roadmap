# AI/ML Fundamentals for PMs

## Learning Objectives

- [ ] Understand the types of machine learning (supervised, unsupervised, reinforcement)
- [ ] Grasp how neural networks work at a conceptual level
- [ ] Know the difference between training and inference
- [ ] Understand what makes LLMs (Large Language Models) special
- [ ] Speak the ML vocabulary needed for PM conversations

## Prerequisites

- Completed: [01 - Why AI PM is Different](./01-why-ai-pm-different.md)

---

## Core Content

### Why PMs Need ML Fundamentals

You don't need to code models. You need to:
- Have intelligent conversations with ML engineers
- Recognize what's possible, difficult, or impossible
- Make informed decisions about AI product trade-offs
- Spot red flags and unrealistic expectations

### The Machine Learning Paradigm

Traditional programming:
```
Rules + Data → Output
"If email contains 'FREE MONEY', mark as spam"
```

Machine learning:
```
Data + Output → Rules (Model)
"Here's 1M emails labeled spam/not-spam. Figure out the rules."
```

**The key insight:** Instead of writing rules, you provide examples, and the algorithm finds patterns.

### Types of Machine Learning

#### 1. Supervised Learning

**What it is:** Learning from labeled examples.

```
Input (Features) → Model → Output (Label)
[Email text]     →   ?   → [Spam/Not Spam]
```

The model learns to map inputs to outputs based on labeled training data.

**Common supervised tasks:**

| Task | Input | Output | Examples |
|------|-------|--------|----------|
| **Classification** | Features | Category | Spam detection, sentiment analysis |
| **Regression** | Features | Number | Price prediction, demand forecasting |

**PM relevance:** Most production ML is supervised. You need labeled data, which can be expensive.

#### 2. Unsupervised Learning

**What it is:** Finding patterns in data without labels.

```
Input (Data) → Model → Patterns/Structure
[Customer data] → ? → [Customer segments]
```

**Common unsupervised tasks:**

| Task | Purpose | Examples |
|------|---------|----------|
| **Clustering** | Group similar items | Customer segmentation |
| **Dimensionality reduction** | Simplify data | Feature engineering |
| **Anomaly detection** | Find outliers | Fraud detection |

**PM relevance:** Useful when you don't have labels but want to discover structure.

#### 3. Reinforcement Learning

**What it is:** Learning from trial and error with rewards.

```
Agent → Action → Environment → Reward/Penalty
                     ↓
                 Update Agent
```

**Examples:** Game playing, robotics, recommendation systems (reward = engagement)

**PM relevance:** Harder to set up, but powerful for optimization problems with clear rewards.

### Neural Networks: The Building Blocks

Neural networks are the foundation of modern AI. Here's the intuition:

#### The Artificial Neuron

```
           ┌───────────┐
Input 1 ──▶│           │
           │   Neuron  │──▶ Output
Input 2 ──▶│ (weighted │
           │    sum +  │
Input 3 ──▶│ function) │
           └───────────┘
```

Each neuron:
1. Takes multiple inputs
2. Multiplies each by a weight (learned importance)
3. Sums them up
4. Applies a function (to add non-linearity)
5. Outputs a value

#### The Neural Network

Stack neurons in layers:

```
Input      Hidden       Output
Layer      Layers       Layer

  O          O   O         O
  O          O   O         O
  O    →     O   O    →    O
  O          O   O
  O          O   O
```

**Training:** Adjust weights so the network produces correct outputs for training examples.

**Depth:** More layers = can learn more complex patterns (but needs more data and computation).

### Deep Learning

"Deep learning" = neural networks with many layers.

**Why it matters:**
- Enabled breakthroughs in image recognition, speech, language
- Powers most modern AI features
- Requires significant data and computation

**Architectures you'll hear about:**

| Architecture | Good For | Examples |
|--------------|----------|----------|
| **CNN** (Convolutional) | Images, spatial data | Image classification, object detection |
| **RNN** (Recurrent) | Sequences, time series | Language (older), audio |
| **Transformer** | Sequences, attention | LLMs (GPT, Claude), modern NLP |

### Training vs. Inference

Two distinct phases with different implications:

#### Training
Teaching the model from data.

```
Training Data → Training Process → Model
(Labeled examples) (Hours/days/weeks) (Learned weights)
```

**Characteristics:**
- Happens offline, in advance
- Computationally expensive
- Requires labeled data
- Done by ML engineers

**PM relevance:**
- Training data quality = model quality
- Training takes time (can't iterate like code)
- Retraining needed for improvement or drift

#### Inference
Using the trained model to make predictions.

```
New Input → Model → Prediction
(User query) (Milliseconds) (Response)
```

**Characteristics:**
- Happens in real-time, in production
- Must be fast and reliable
- Runs on serving infrastructure
- Each prediction has a cost

**PM relevance:**
- Inference latency affects UX
- Inference cost affects unit economics
- Monitor inference quality over time

### The LLM Revolution

Large Language Models (LLMs) like GPT-4, Claude, and Gemini have transformed AI products.

#### How LLMs Work (Simplified)

1. **Pre-training:** Model reads massive amounts of text, learns language patterns
2. **Next token prediction:** Given text, predict the next word (token)
3. **Scaling:** Larger models + more data = emergent capabilities
4. **Fine-tuning:** Adapt for specific tasks (optional)
5. **RLHF:** Reinforce learning from human feedback for helpfulness/safety

```
"The quick brown fox" → [LLM] → "jumps" (predicted next token)
```

Repeat this process to generate entire responses.

#### What Makes LLMs Special

| Capability | Before LLMs | With LLMs |
|------------|-------------|-----------|
| Language understanding | Task-specific models | General understanding |
| Generation | Template-based | Fluent, contextual |
| Zero-shot learning | Can't do new tasks | Can attempt any task |
| Few-shot learning | Need thousands of examples | 2-3 examples can work |
| Instruction following | Requires training | Works from natural language |

#### LLM Tradeoffs

| Tradeoff | Consideration |
|----------|---------------|
| **Accuracy vs. speed** | Larger models = smarter but slower |
| **Cost vs. quality** | Better models cost more per token |
| **Consistency vs. creativity** | Temperature controls randomness |
| **Context length** | More context = better answers but higher cost |

### ML Vocabulary for PMs

Key terms you'll encounter:

#### Data Terms
| Term | Meaning |
|------|---------|
| **Features** | Input variables the model uses |
| **Labels** | Correct answers for training |
| **Training set** | Data used to train the model |
| **Validation set** | Data used to tune hyperparameters |
| **Test set** | Data used for final evaluation |
| **Data augmentation** | Creating variations to increase data |

#### Model Terms
| Term | Meaning |
|------|---------|
| **Parameters** | Learned weights in the model (billions in LLMs) |
| **Hyperparameters** | Settings you choose (learning rate, layers) |
| **Architecture** | The model's structure |
| **Fine-tuning** | Additional training on specific data |
| **Transfer learning** | Reusing a trained model for new tasks |

#### Performance Terms
| Term | Meaning |
|------|---------|
| **Overfitting** | Model memorizes training data, fails on new data |
| **Underfitting** | Model is too simple, can't learn patterns |
| **Bias** | Systematic errors in a particular direction |
| **Variance** | Inconsistency in predictions |
| **Generalization** | Ability to work on new, unseen data |

#### LLM-Specific Terms
| Term | Meaning |
|------|---------|
| **Token** | Unit of text (roughly a word or part of word) |
| **Context window** | Maximum tokens the model can process |
| **Temperature** | Controls randomness (0 = deterministic, 1 = creative) |
| **Prompt** | Input text given to the model |
| **Hallucination** | Generating false information confidently |
| **Grounding** | Connecting outputs to verified sources |

### Understanding Model Capabilities

When evaluating what a model can do:

**Questions to ask:**

1. **What was it trained on?**
   - Training data determines capabilities
   - Recency of training affects knowledge

2. **What's the error rate?**
   - On which types of inputs?
   - What do failures look like?

3. **How does it handle edge cases?**
   - Unusual inputs
   - Adversarial inputs
   - Out-of-distribution data

4. **What are the latency and cost?**
   - Acceptable for your use case?
   - Scale considerations?

5. **Can it explain its decisions?**
   - If needed for your domain
   - What level of explainability?

---

## Key Takeaways

1. **ML learns patterns from data rather than following explicit rules—this enables capabilities but requires data**
2. **Supervised learning (labeled data), unsupervised (finding patterns), and reinforcement (trial and error) serve different purposes**
3. **Neural networks learn complex patterns through layers of interconnected neurons**
4. **Training is expensive and offline; inference is fast and in production—both matter differently**
5. **LLMs transformed AI with general language capabilities, but trade off accuracy/speed/cost**
6. **Learn the ML vocabulary—it's essential for productive conversations with ML teams**

---

## Practice

### Reflection Questions
1. Think of a recommendation system you use. What inputs (features) might it use? What's the output?
2. Why might a model that performs perfectly on test data fail in production?
3. For an AI feature you've used, do you think it uses an LLM or a more specialized model? What suggests one vs. the other?

### Exercise
**ML Application Mapping:**

For each product scenario, identify:
1. Type of ML (supervised, unsupervised, RL)
2. Likely architecture (traditional ML, deep learning, LLM)
3. What data would be needed
4. Key challenges

**Scenario A:** A streaming service wants to predict which shows users will enjoy.
```
ML Type: [Your answer]
Architecture: [Your answer]
Data needed: [Your answer]
Challenges: [Your answer]
```

**Scenario B:** A bank wants to detect unusual transactions that might be fraud.
```
ML Type: [Your answer]
Architecture: [Your answer]
Data needed: [Your answer]
Challenges: [Your answer]
```

**Scenario C:** A customer service tool that drafts email responses for agents.
```
ML Type: [Your answer]
Architecture: [Your answer]
Data needed: [Your answer]
Challenges: [Your answer]
```

---

## Further Reading

- **"Deep Learning" by Goodfellow, Bengio, Courville** - Comprehensive (technical)
- **"The Hundred-Page Machine Learning Book" by Andriy Burkov** - Accessible overview
- **3Blue1Brown Neural Network videos** - Excellent visual explanations
- **Anthropic Research Blog** - Claude's technical details
- **Google's Machine Learning Crash Course** - Free, practical introduction
- **Papers With Code** - See what's possible with current AI

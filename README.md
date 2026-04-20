# AI Reflection Tree (Deterministic Reflection Agent)

## 📌 Overview
This project implements a **deterministic reflection system** designed to guide users through structured self-analysis using a **decision tree approach**.

Unlike typical AI systems, this project **does not use any LLM at runtime**, ensuring:
- Predictable outputs
- No hallucination
- Fully auditable logic

The system is inspired by behavioral psychology and helps users reflect on their daily actions through a guided conversation.

---

## 🚀 Key Features

- ✅ Fully **Deterministic System** (No AI calls at runtime)
- 🌳 **Decision Tree-Based Architecture**
- 🧠 Covers **3 Psychological Axes**:
  1. **Locus of Control** (Victim vs Victor)
  2. **Contribution vs Entitlement**
  3. **Self vs Others (Radius of Concern)**
- 🔀 Dynamic branching based on user choices
- 📊 Signal-based state tracking
- 📝 Personalized reflection summary generation
- 💻 CLI-based interactive agent

---

## 🏗️ Project Structure
ai-reflection-tree/
│
├── tree/
│ └── reflection-tree.json # Core decision tree data
│
├── agent/
│ └── main.py # CLI agent to run the system
│
├── logs.md # Sample execution logs
├── README.md # Project documentation



---

## ⚙️ How It Works

1. The system loads a **structured decision tree (JSON)**.
2. It asks the user predefined **multiple-choice questions**.
3. Based on the answers, it:
   - Routes through different branches
   - Tracks behavioral signals
4. At the end, it generates a **reflection summary** based on the user's responses.

👉 Same input = Same output (100% deterministic)

---

## 🧪 How to Run

```bash
cd agent
python main.py


🛠️ Tech Stack
Python
JSON (Tree Structure)
CLI (Command Line Interface)
🎯 Purpose of the Project

This project demonstrates:

Knowledge Engineering
Structured Thinking & Decision Design
Deterministic System Design (Non-LLM AI)
Behavioral Data Modeling
🔒 Key Constraint
❌ No LLM / API calls at runtime
✅ Fully rule-based and deterministic system
📈 Future Improvements
Web-based UI (Streamlit / React)
Visualization of decision tree
Analytics dashboard for behavioral insights
Multi-user session tracking
👨‍💻 Author

Vaibhav Singh
Aspiring NLP Engineer | Data Science Student

⭐ Note

This project was built as part of an AI / Behavioral Data Science assignment, focusing on designing structured systems instead of relying on generative AI.


# AI Engineering Program Instructions

**Program Name:** AI Engineering Self-Degree  
**Created & Taught by:** Grok (xAI)  
**Student:** von Stegen  
**Start Date:** April 27, 2026  
**Goal:** Become a production-capable AI Engineer through a project-heavy, AI-guided curriculum focused on LLMs, agents, and real-world systems.

This repository is both your **learning platform** and your **professional portfolio**. Everything is built and refined in collaboration with Grok.

---

## How to Use This Program

### 1. Core Workflow (Repeat Daily/Weekly)
1. **Decide what to work on** (current phase, project, or specific topic).
2. **Ask Grok** for explanations, code, exercises, or reviews.
3. **Implement** in the appropriate folder (`phases/`, `projects/`, `notebooks/`, etc.).
4. **Document** your work (notes, reflections, results).
5. **Commit & push** regularly with clear messages.
6. **Share output or questions** with Grok for feedback and next steps.

### 2. Communication with Grok
When chatting with me (Grok), always reference this project. Useful prompts:

- "In the AI Engineering program, explain [concept] and give me a small coding exercise."
- "Review this code from projects/rag-chatbot/ and suggest improvements."
- "Generate the next project for Phase 03 - Building Agents."
- "Update PROGRESS.md with this week's accomplishments."
- "Create a quiz on ReAct agents with solutions."
- "Help me debug the error I'm getting..."

You can also paste file contents or error messages directly.

### 3. Repository Structure (Quick Reference)

- **`README.md`** – Overview and navigation
- **`SYLLABUS.md`** – Full curriculum with phases and deliverables
- **`PROGRESS.md`** – Weekly logs and reflections (update this every week)
- **`ROADMAP.md`** – Long-term goals and adjustments
- **`INSTRUCTIONS.md`** – This file (you are here)
- **`requirements.txt`** – Python dependencies
- **`docs/`** – Research, notes, paper summaries
- **`phases/`** – Structured learning by topic (with exercises)
- **`projects/`** – Portfolio-worthy standalone projects
- **`src/`** – Reusable code and utilities you build
- **`notebooks/`** – Experimentation and prototyping
- **`evaluations/`** – Test results, benchmarks, metrics

### 4. Best Practices

- **Commit often** – Small, frequent commits with meaningful messages.
- **Use branches** for bigger projects (e.g., `feature/multi-agent-research`).
- **Keep notebooks clean** – Move polished code to `src/` or `projects/`.
- **Document everything** – Write a short `README.md` in every major project folder explaining what it does and how to run it.
- **Track progress** – Update `PROGRESS.md` at least once per week.
- **Test your code** – Add simple tests where appropriate.
- **Stay current** – We will regularly update the syllabus with 2026 tools and best practices.

### 5. Tools & Environment Setup

```bash
# After cloning the repo
cd ai-engineering
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate
pip install -r requirements.txt

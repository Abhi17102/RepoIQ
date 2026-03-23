# 🚀 RepoIQ (Version 1)

RepoIQ is a backend system that analyzes GitHub profiles to extract meaningful insights about a developer's real skills based on their projects.

## 💡 Problem Statement
Traditional resumes often fail to represent actual technical skills. RepoIQ focuses on analyzing real GitHub repositories to provide a more accurate evaluation.

## ⚙️ Features
- Fetch GitHub repositories using GitHub API
- Analyze repositories based on:
  - Programming languages
  - Machine Learning / AI projects
  - Backend development work
  - DevOps practices
- Generate skill-level insights (Beginner → Advanced)
- Cache results using PostgreSQL for performance optimization

## 🛠️ Tech Stack
- FastAPI (Backend Framework)
- PostgreSQL (Database)
- Python
- GitHub REST API

## 🧠 How It Works
1. Fetch user repositories from GitHub
2. Analyze repo data (name, description, topics, language)
3. Classify projects into ML, Backend, DevOps
4. Calculate skill scores
5. Cache results in PostgreSQL

## 🚀 Future Improvements
- Frontend dashboard
- AI-based deep code analysis
- Resume vs GitHub comparison
- Industry-level candidate shortlisting system

## 🌐 Status
Version 1 completed. Deployment coming soon.

---

from fastapi import FastAPI
from app.services.github_service import fetch_user_repos
from app.services.repo_analyzer import analyze_repositories
from app.services.scoring_engine import calculate_skill_scores
from app.database.db import get_cached_user ,save_cached_user

app = FastAPI()

@app.get("/")
def root():
    return{"message":"RepoIQ API is running"}

@app.get("/github/{username}")
def get_github_data(username: str):
    
    cached_data = get_cached_user(username)
    if cached_data:
        return{
            "username": username,
            "source":"cache",
            "repo_count":cached_data["repo_count"],
            "analysis": cached_data["analysis"],
            "skills": cached_data["skills"]
        } 

    repos= fetch_user_repos(username)

    if "error" in repos:
        return repos

    sorted_repos= sorted(repos, key=lambda x:x["stars"], reverse=True)

    top_repos = sorted_repos[:3]

    analysis =analyze_repositories(repos)

    skills = calculate_skill_scores(analysis)

    save_cached_user(username, len(repos), analysis, skills)

    return{
        "username": username,
        "source":"github",
        "repo_count": len(repos),
        "top_repositories": top_repos,
        "repositories": repos,
        "analysis":analysis,
        "skills":skills
        
    }


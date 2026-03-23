import requests

def fetch_user_repos(username: str):

    repos =[]
    page = 1

    while True:
        url = f"https://api.github.com/users/{username}/repos?page={page}&per_page=30"

        response = requests.get(url)

        if response.status_code == 404:
            return {"error": "User not found"}

        if response.status_code == 403:
            return {"error": "GitHub API rate limit exceeded"}

        if response.status_code != 200:
            return {"error": "GitHub API error"}

        data = response.json()

        if not data:
            break

        for repo in data:
            repos.append({
                "name": repo.get("name"),
                "stars": repo.get("stargazers_count"),
                "language": repo.get("language"),
                "description": repo.get("description"),
                "topics": repo.get("topics", [])
            })

        page += 1
    return repos
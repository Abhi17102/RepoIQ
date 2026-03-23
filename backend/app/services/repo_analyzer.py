def analyze_repositories(repos):
    language_count={}
    ml_projects=0
    backend_projects =0
    devops_projects =0

    ml_keywords=["ml","ai","neural","model",]
    backend_keywords=["api","backend","server","fastapi","django","flask"]
    devops_keywords=["docker","kubernetes","deploy","ci","cd"]

    for repo in repos:
        repo_name = repo["name"].lower()
        description = (repo.get("description") or "").lower()
        combined_text= repo_name + " " + description
        topics =repo.get("topics", [])
        language = repo["language"]

        if language:                            #this loop is for language count
            if language in language_count:
                language_count[language] +=1
            else:
                language_count[language] =1
        
        for keyword in ml_keywords:
            if keyword in combined_text or keyword in topics:
                ml_projects +=1
                break
        
        for keyword in backend_keywords:
            if keyword in combined_text or keyword in topics:
                backend_projects +=1
                break

        for keyword in devops_keywords:
            if keyword in combined_text or keyword in topics:
                devops_projects +=1
                break

    return{
            "languages": language_count,
            "ml_projects": ml_projects,
            "backend_projects": backend_projects,
            "devops_projects": devops_projects
        }

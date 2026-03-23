def calculate_skill_scores(analysis):
    ml_projects = analysis["ml_projects"]
    backend_projects = analysis["backend_projects"]
    devops_projects = analysis["devops_projects"]

    def get_skill_level(count):
        if count >= 5:
            return "Advanced"
        elif count >= 2:
            return "Intermediate"
        elif count >= 1:
            return "Beginner"
        else:
            return "None"
        
    skills={
        "ml_projects" : ml_projects,
        "ml_skill" : get_skill_level(ml_projects),
        "backend_projects" : backend_projects,
        "backend_skill" : get_skill_level(backend_projects),
        "devops_projects" : devops_projects,
        "devops_skill" : get_skill_level(devops_projects),
    }

    return skills
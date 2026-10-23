
CAREER_PROFILES = {
    "AI Engineer": {
        "skills": {"Python", "Machine Learning", "SQL", "Data Analysis"},
        "interests": {"Artificial Intelligence", "Data Science"},
    },
    "Data Scientist": {
        "skills": {"Python", "Machine Learning", "SQL", "Data Analysis"},
        "interests": {"Data Science", "Artificial Intelligence"},
    },
    "Software Developer": {
        "skills": {"Python", "C Programming", "Java", "SQL", "Web Development"},
        "interests": {"Software Development", "Web Development"},
    },
    "Cybersecurity Analyst": {
        "skills": {"Python", "SQL", "C Programming"},
        "interests": {"Cybersecurity", "Cloud Computing"},
    },
    "Data Analyst": {
        "skills": {"Python", "SQL", "Data Analysis"},
        "interests": {"Data Science", "Business and Management"},
    },
}


def calculate_career_matches(skills, interests):
    selected_skills = set(skills)
    selected_interests = set(interests)
    results = []

    for career, profile in CAREER_PROFILES.items():
        required_skills = profile["skills"]
        relevant_interests = profile["interests"]

        skill_score = (
            len(selected_skills & required_skills)
            / len(required_skills)
        )

        interest_score = (
            len(selected_interests & relevant_interests)
            / len(relevant_interests)
        )

        match_score = (
            skill_score * 0.6 + interest_score * 0.4
        ) * 100

        results.append({
            "career": career,
            "skill_score": round(skill_score * 100),
            "interest_score": round(interest_score * 100),
            "match_score": round(match_score),
            "missing_skills": sorted(
                required_skills - selected_skills
            ),
        })

    return sorted(
        results,
        key=lambda item: item["match_score"],
        reverse=True,
    )

required_skills = {'python', 'github', 'linux'}

candidates = {
    'anna': {'java', 'linux', 'windows', 'github', 'python', 'full stack'},
    'bob': {'github', 'linux', 'python'},
    'carol': {'linux', 'javascript', 'html', 'python', 'github'},
    'daniel': {'pascal', 'java', 'c++', 'github'},
    'ekani': {'html', 'css', 'github', 'python', 'linux'},
    'fenna': {'linux', 'pascal', 'java', 'c', 'lisp', 'modula-2', 'perl', 'github'},
}

reach_baseline = set()
have_additional_skills = set()

for name, skills in candidates.items():
    if skills >= required_skills:
        reach_baseline.add(name)
        if skills > required_skills:
            have_additional_skills.add(name)
            
print(f"Interviewees: {reach_baseline}")
print(f"Better interviewees: {have_additional_skills}")
    
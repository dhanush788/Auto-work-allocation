from parse_sentence import parse
import json
import sys

# Mapping for skills (temporary for crude AI)
SKILL_MAPPING = {
        "Front End Developer" : [
            "React",
            "JS",
            "HTML",
            "JavaScript",
            "Graphic Design",
            "Adobe Illustrator",
            "UI/UX",
            "UI/UX Design",
            "Sketch",
            "Wireframing",
            "Photoshop",
            "Logo Design",
            "Angular",
            "TypeScript",
            "CSS",
            "Web Design",
            "HTML/CSS"
            ],

        "Back End Developer" : [
            "Python",
            "SQL",
            "Django",
            "PHP",
            "MySQL",
            "Laravel",
            "Node.js",
            "Express",
            "MongoDB"
            ],

        "Systems Programmer" : [

            ],

        "Devops Engineer" : [

            ],

        "Game Developer" : [

            ],

        "Mobile App Developer" : [
            "Java",
            "Spring Boot",
            ],

        "Marketing Expert" : [
            "Marketing",
            "SEO",
            "Content Strategy",
            "Copywriting",
            "Content Marketing",
            "Blogging"
            ],

        "Graphics Designer" : [
            "Graphic Design",
            "Photoshop",
            "Logo Design",
            "Illustration",
            "Digital Media",
            "Concept Art",
            "Painting",
            "Video Editing",
            "Adobe Premiere",
            "Motion Graphics"
            ],

        "Data Analyst" : [
            "Data Analysis",
            "Excel",
            "Statistics"
            ]
        }

def get_filtered_users(user_list, job_list):
    """ Get users filtered based on broad jobs """

    filtered_data = {}

    for user in user_list:
        email = user["email"]
        user_jobs = []

        for skill in user["skills"]:
            # Checking appropriate job for skill
            for job in job_list:
                if skill in job_list[job]:
                    if job not in user_jobs:
                        user_jobs.append(job)

        filtered_data[email] = user_jobs

    return filtered_data

def get_employee(task):
    # Loading data
    with open("../src/constant/constant.json", "r") as f:
        data = json.load(f)

    users = data["users"]
    filtered_users = get_filtered_users(users, SKILL_MAPPING)

    # Parsing task
    job = parse(task)
    print(job)

if __name__ == "__main__":
    task = sys.argv[1]
    get_employee(task)

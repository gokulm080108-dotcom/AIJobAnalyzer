import matplotlib.pyplot as plt
import re


skill_database={
    "Python":["python"],
    "Java":["java"],
    "C":["c programming","c language"],
    "SQL":["sql"],
    "Machine Learning":["machine learning","ml"],
    "Deep Learning":["deep learning","dl"],
    "Artificial Intelligence":["artificial intelligence","ai"],
    "Data Science":["data science"],
    "Data Analysis":["data analysis","data anlytics"],
    "Pandas":["pandas"],
    "Numpy":["numpy"],
    "TensorFlow":["tensorflow"],
    "Power BI":["power bi"],
    "Git":["git"],
    "Communication":["communication skills"]
}

print("================================================================")
print("AI RESUME SKILL ANALYZER")
print("================================================================")

print("\nPaste your resume text below.")
print("Type 'END' on a new line when you are done.\n")

resume_lines = []
while True:
    line = input()
    if line.strip().upper() == "END":
        break
    resume_lines.append(line)

resume_text = "\n".join(resume_lines)

clean_resume=resume_text.lower()

recognized_skills = []
for skill, keywords in skill_database.items():
    for keyword in keywords:
        pattern=r"(?<!\w)"+re.escape(keyword)+r"(?!\w)"
        if re.search(pattern, clean_resume):
            recognized_skills.append(skill)
            break

recognized_skills = list(dict.fromkeys(recognized_skills))

print("\nEnter the skills required for the job.")
print("Seperate each skill with a commas.")

job_input = input("\nRequired skills: ")

required_skills = [skill.strip().lower() for skill in job_input.split(",") if skill.strip()]

matched_skills = []
missing_skills = []

for skill in required_skills:
    found = False
    for recognized in recognized_skills:
        if skill==recognized.lower():
            matched_skills.append(recognized)
            found = True
            break
    if not found:
        missing_skills.append(skill.title())


if len(required_skills)>0:
    matched_percentage = (len(matched_skills) / len(required_skills)) * 100
else:
    matched_percentage = 0

print("\n================================================================")
print("ANALYSIS RESULTS")
print("================================================================")

print("\nRecognized Skills")
if recognized_skills:
    for skill in recognized_skills:
        print("-", skill)
else:
    print("No skills recognized in the resume.")

print("\nMatched job skills:")
if matched_skills:
    for skill in matched_skills:
        print("-", skill)
else:
    print("No matched skills found.")

print("\nMissing job skills:")
if missing_skills:
    for skill in missing_skills:
        print("-", skill)
else:
    print("No missing skills.")

print("\nMatched Skills Percentage: {:.2f}%".format(matched_percentage))     

print("\n================================================================")
print("Analysis completed successfully! Thank you for using the AI Resume Skill Analyzer.")
print("================================================================")


# --------------------------------
# DISPLAY SKILL MATCH PIE CHART
# --------------------------------

if len(required_skills) > 0:

    matched_percentage = matched_percentage
    missing_percentage = 100 - matched_percentage

    # Data for the pie chart
    values = [matched_percentage, missing_percentage]

    # Labels for the chart
    labels = ["Matched Skills", "Missing Skills"]

    # Create the pie chart
    plt.figure(figsize=(7, 7))

    plt.pie(
        values,
        labels=labels,
        autopct="%.1f%%",
        startangle=90
    )

    # Add a title
    plt.title("AI Resume Skill Match Analysis")

    # Display the chart
    plt.show()

else:
    print("Pie chart cannot be created without job requirements.")
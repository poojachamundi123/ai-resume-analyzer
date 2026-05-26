import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def analyze_resume(resume, job_description):
    # Convert text into vectors
    texts = [resume, job_description]

    vectorizer = CountVectorizer().fit_transform(texts)
    vectors = vectorizer.toarray()

    # Calculate similarity score
    similarity = cosine_similarity([vectors[0]], [vectors[1]])

    score = similarity[0][0] * 100
    return score

# Take input from user
print("=== AI Resume Analyzer ===\n")

resume = input("Enter your Resume text:\n")
job_description = input("\nEnter Job Description:\n")

# Get score
score = analyze_resume(resume, job_description)

# Show result
print("\n==========================")
print(f"Resume Match Score: {score:.2f}%")

# Evaluation message
if score > 70:
    print("Result: High Match - Good Resume 👍")
elif score > 40:
    print("Result: Medium Match - Improve Your Resume ⚠️")
else:
    print("Result: Low Match - Needs Improvement ❌")

print("==========================")

'''
--------------------------output------------------------------

=== AI Resume Analyzer ===

Enter your Resume text:
I am a student. I like music and gaming. I have basic knowledge of computers. I am looking for any job opportunity.

Enter Job Description:
We are looking for a Python developer with skills in Python, SQL, Machine Learning, Data Analysis, Flask framework, Pandas, NumPy, APIs, and databases. Candidate should have strong programming and problem-solving skills.

==========================
Resume Match Score: 18.86%
Result: Low Match - Needs Improvement ❌
==========================


=== AI Resume Analyzer ===

Enter your Resume text:
Python developer with strong knowledge of SQL, Machine Learning, Data Analysis, Flask, Pandas, and NumPy. Built projects using Python, Flask APIs, and data analysis tools. Good problem-solving skills and understanding of databases. B.Tech in Information Technology.

Enter Job Description:
We are looking for a Python developer with skills in Python, SQL, Machine Learning, Data Analysis, Flask framework, Pandas, NumPy, APIs, and databases. Candidate should have strong programming and problem-solving skills.

==========================
Resume Match Score: 70.00%
Result: High Match - Good Resume 👍
==========================

=== AI Resume Analyzer ===

Enter your Resume text:
Python developer with strong knowledge of SQL, Machine Learning, Data Analysis, Flask, Pandas, and NumPy. Built projects using Python, Flask APIs, and data analysis tools. Good problem-solving skills and understanding of databases. B.Tech in Information Technology.

Enter Job Description:
Python developer with strong knowledge of SQL, Machine Learning, Data Analysis, Flask, Pandas, and NumPy. Built projects using Python, Flask APIs, and data analysis tools. Good problem-solving skills and understanding of databases. B.Tech in Information Technology.

==========================
Resume Match Score: 100.00%
Result: High Match - Good Resume 👍
==========================

'''
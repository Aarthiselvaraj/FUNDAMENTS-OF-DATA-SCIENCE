import pandas as pd
data = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Course': ['Math', 'Math', 'Physics', 'Physics', 'English', 'English', 'History', 'History', 'Biology', 'Biology'],
    'Score': [85, 78, 90, 82, 75, 80, 88, 76, 92, 85],
    'Hours_Studied': [20, 15, 25, 18, 10, 12, 22, 17, 30, 28]
}

student_data = pd.DataFrame(data)
correlation_per_course = student_data.groupby('Course').apply(lambda x: x['Hours_Studied'].corr(x['Score']))
print("Correlation coefficient between Hours_Studied and Score for each course:")
print(correlation_per_course)


strongest_corr_course = correlation_per_course.idxmax()
weakest_corr_course = correlation_per_course.idxmin()
print("Course with the strongest correlation: ", strongest_corr_course,"\n")
print("Course with the weakest correlation: ", weakest_corr_course,"\n")


average_data = student_data.groupby('Course').agg({'Score': 'mean', 'Hours_Studied': 'mean'}).reset_index()
average_data.columns = ['Course', 'Average Score', 'Average Hours Studied']
print("Aggregated DataFrame showing average score and average hours studied for each course:")
print(average_data)

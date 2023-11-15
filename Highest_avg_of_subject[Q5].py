"""import numpy as np


student_scores = np.array([
    [85, 90, 75, 80],
    [70, 88, 92, 65],
    [78, 82, 80, 75],
    [88, 85, 90, 72]
])

average_scores = np.mean(student_scores, axis=0)
print("Average scores for each subject:", average_scores)

subject_names = ['Math', 'Science', 'English', 'History']
subject_highest_avg = subject_names[np.argmax(average_scores)]
print("Subject with the highest average score:", subject_highest_avg)"""
import numpy as np


np.random.seed(42)  

 
student_scores = np.random.randint(50, 100, size=(15, 4))

print("Student Scores Dataset:")
print(student_scores)


average_scores = np.mean(student_scores, axis=0)
print("\nAverage scores for each subject:", average_scores)


subject_names = ['Math', 'Science', 'English', 'History']
subject_highest_avg = subject_names[np.argmax(average_scores)]
print("Subject with the highest average score:", subject_highest_avg)


print("========================================")
print(" STUDENT PERFORMANCE ANALYTICS SYSTEM")
print("========================================")

print("\nWelcome to the Student Performance Analytics System!")
print("This project analyzes student marks and performance.")

print("\nProject Status: Started Successfully!")

import pandas as pd
import numpy as np

# Read student data from CSV file

df = pd.read_csv("students.csv")

# Display all student records

print("\n========== STUDENT RECORDS ==========")
print(df)

# Calculate total marks for each student

subjects = ["Python", "Statistics", "Java", "English"]

df["Total"] = df[subjects].sum(axis=1)

# Calculate average marks for each student

df["Average"] = df[subjects].mean(axis=1)

print("\n========== STUDENT MARKS ANALYSIS ==========")
print(df[["Name", "Total", "Average"]].to_string(index=False))

# Find the highest and lowest total marks

highest = df["Total"].max()
lowest = df["Total"].min()

print("\nHighest Total Marks:", highest)
print("Lowest Total Marks:", lowest)

# Calculate class average

class_average = df[subjects].mean().mean()

print("Class Average:", round(class_average, 2))

# Assign grades based on average marks
def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


# Check whether a student passes or fails
def calculate_result(row):
    for subject in subjects:
        if row[subject] < 35:
            return "Fail"
    return "Pass"


# Apply grade and result calculations
df["Grade"] = df["Average"].apply(calculate_grade)
df["Result"] = df.apply(calculate_result, axis=1)

# Display student results
print("\n========== GRADES AND RESULTS ==========")
print(df[["Name", "Average", "Grade", "Result"]].to_string(index=False))

# Find the top 3 students based on total marks

top_students = df.nlargest(3, "Total")

print("\n========== TOP 3 PERFORMERS ==========")
print(top_students[["Name", "Total", "Average", "Grade"]].to_string(index=False))

# Find the subject with the highest class average

subject_averages = df[subjects].mean()
best_subject = subject_averages.idxmax()

print("\n========== SUBJECT PERFORMANCE ==========")
print("Best Performing Subject:", best_subject)
print("Subject Average:", round(subject_averages[best_subject], 2))

# Calculate average marks for each subject

subject_averages = df[subjects].mean()

print("\n========== SUBJECT-WISE PERFORMANCE ==========")

for subject, average in subject_averages.items():
    np.mean(df[subject].to_numpy())
    print(f"{subject}:{average:.2f}")

# Find the best and weakest performing subjects

best_subject = subject_averages.idxmax()
weakest_subject = subject_averages.idxmin()

print("\nBest Performing Subject:", best_subject)
print("Weakest Performing Subject:", weakest_subject)

# Search for a student by name
print("\n========== STUDENT SEARCH ==========")

student_name = input("Enter student name to search: ")

student = df[df["Name"].str.lower() == student_name.strip().lower()]

if not student.empty:
    print("\nStudent Details:")
    print(student[["Name", "Python", "Statistics", "Java",
                   "English", "Total", "Average", "Grade",
                   "Result"]].to_string(index=False))
else:
    print("Student not found!")

# Count pass and fail students
pass_count = (df["Result"] == "Pass").sum()
fail_count = (df["Result"] == "Fail").sum()

print("\n========== CLASS RESULTS ==========")
print("Total Students:", len(df))
print("Students Passed:", pass_count)
print("Students Failed:", fail_count)

# Calculate pass percentage
pass_percentage = (pass_count / len(df)) * 100 if len(df) > 0 else 0

print("Pass Percentage:", round(pass_percentage, 2), "%")
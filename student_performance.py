import pandas as pd

# Load the dataset

df = pd.read_csv("student-mat.csv", sep=";")

# Display the first five rows

print("\n--- First Five Rows ---")
print(df.head())

# Display the number of rows and columns

print("\n--- Dataset Shape ---")
print(df.shape)

# Display column names

print("\n--- Column Names ---")
print(df.columns.tolist())

# Check for missing values

print("\n--- Missing Values ---")
print(df.isnull().sum())

# Basic statistical summary
print("\n--- Statistical Summary ---")
print(df.describe())

# Average final grade
print("\n--- Average Final Grade ---")
print(df["G3"].mean())

# Highest final grade
print("\n--- Highest Final Grade ---")
print(df["G3"].max())

# Lowest final grade
print("\n--- Lowest Final Grade ---")
print(df["G3"].min())

# Average final grade by study time

print("\n--- Average Final Grade by Study Time ---")

result = df.groupby("studytime")["G3"].mean()

print(result)



import matplotlib.pyplot as plt

# Calculate average final grade for each study time category
average_grades = df.groupby("studytime")["G3"].mean()

# Create a bar chart
plt.figure(figsize=(8, 5))
average_grades.plot(kind="bar")

# Add title and labels
plt.title("Average Final Grade by Study Time")
plt.xlabel("Study Time Category")
plt.ylabel("Average Final Grade")

# Improve chart readability
plt.xticks(rotation=0)
plt.tight_layout()

# Save the chart
plt.savefig("studytime_vs_final_grade.png")

# Display the chart
plt.show()


import matplotlib.pyplot as plt

# Create a scatter plot
plt.figure(figsize=(8, 5))

plt.scatter(df["G2"], df["G3"], alpha=0.6)

# Add title and labels
plt.title("Relationship Between G2 and G3 Grades")
plt.xlabel("Second-Period Grade (G2)")
plt.ylabel("Final Grade (G3)")

plt.tight_layout()

# Save the chart
plt.savefig("g2_vs_g3.png")

# Display the chart
plt.show()




# Correlation between second-period and final grades
correlation = df["G2"].corr(df["G3"])

print("\n--- Correlation Analysis ---")
print("Correlation between G2 and G3:", round(correlation, 3)) 

# Analyze absences vs final grades

print("\n--- Absences vs Final Grades ---")

# Check basic statistics
print(df[['absences', 'G3']].describe())

# Calculate correlation
correlation = df['absences'].corr(df['G3'])

print(f"Correlation between absences and final grades: {correlation:.3f}")

# Visualize the relationship
plt.figure(figsize=(8, 5))

plt.scatter(
    df['absences'],
    df['G3'],
    alpha=0.7
)

plt.xlabel('Number of Absences')
plt.ylabel('Final Grade (G3)')
plt.title('Student Absences vs Final Grades')

plt.grid(True, alpha=0.3)

plt.savefig('absences_vs_final_grade.png')
plt.show()

import matplotlib.pyplot as plt

subjects = ["Python", "Maths", "DSA", "Java"]
marks = [85, 78, 92, 88]

plt.bar(subjects, marks)

plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Marks in Different Subjects")

plt.show()
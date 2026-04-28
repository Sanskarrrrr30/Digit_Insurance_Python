# STEP 1: Constants
SCHOOL_NAME = "New School Of Learning"
CLASS_NAME = "Class XI"
MAX_MARKS = 50
NUM_STUDENTS = 3

# STEP 2–4: Student 1
name1 = input("Enter Student 1 Name: ")
p1 = int(input("Physics Marks: "))
c1 = int(input("Chemistry Marks: "))
m1 = int(input("Mathematics Marks: "))

total1 = p1 + c1 + m1
percent1 = (total1 / (3 * MAX_MARKS)) * 100

# STEP 5–7: Student 2
name2 = input("\nEnter Student 2 Name: ")
p2 = int(input("Physics Marks: "))
c2 = int(input("Chemistry Marks: "))
m2 = int(input("Mathematics Marks: "))

total2 = p2 + c2 + m2
percent2 = (total2 / (3 * MAX_MARKS)) * 100

# STEP 8–10: Student 3
name3 = input("\nEnter Student 3 Name: ")
p3 = int(input("Physics Marks: "))
c3 = int(input("Chemistry Marks: "))
m3 = int(input("Mathematics Marks: "))

total3 = p3 + c3 + m3
percent3 = (total3 / (3 * MAX_MARKS)) * 100

# FUNCTION TO PRINT REPORT
def print_report(name, p, c, m, total, percent):
    print("\n" + "="*50)
    print(f"{SCHOOL_NAME}")
    print(f"{CLASS_NAME} - Report Card")
    print(f"Student Name: {name}")
    print("="*50)
    print(f"{'Subject':<15}{'Marks':<10}{'%':<10}")
    print("-"*35)
    
    print(f"{'Physics':<15}{p:<10}{(p/MAX_MARKS*100):.2f}")
    print(f"{'Chemistry':<15}{c:<10}{(c/MAX_MARKS*100):.2f}")
    print(f"{'Mathematics':<15}{m:<10}{(m/MAX_MARKS*100):.2f}")
    
    print("-"*35)
    print(f"{'Total':<15}{total:<10}")
    print(f"{'Overall %':<15}{percent:.2f}")
    print("="*50)

# PRINT RESULTS
print_report(name1, p1, c1, m1, total1, percent1)
print_report(name2, p2, c2, m2, total2, percent2)
print_report(name3, p3, c3, m3, total3, percent3)

# STEP 11–15: CLASS SUMMARY
total_physics = p1 + p2 + p3
total_chemistry = c1 + c2 + c3
total_maths = m1 + m2 + m3

avg_physics = total_physics / NUM_STUDENTS
avg_chemistry = total_chemistry / NUM_STUDENTS
avg_maths = total_maths / NUM_STUDENTS

overall_total = total1 + total2 + total3
overall_percent = (overall_total / (NUM_STUDENTS * 3 * MAX_MARKS)) * 100

# STEP 16: PRINT SUMMARY
print("\n" + "="*50)
print("CLASS SUMMARY")
print("="*50)
print(f"{'Subject':<15}{'Average Marks':<15}{'Average %':<15}")
print("-"*45)

print(f"{'Physics':<15}{avg_physics:<15.2f}{(avg_physics/MAX_MARKS*100):.2f}")
print(f"{'Chemistry':<15}{avg_chemistry:<15.2f}{(avg_chemistry/MAX_MARKS*100):.2f}")
print(f"{'Mathematics':<15}{avg_maths:<15.2f}{(avg_maths/MAX_MARKS*100):.2f}")

print("-"*45)
print(f"{'Overall %':<15}{overall_percent:.2f}")
print("="*50)
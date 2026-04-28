import csv

# # writing to a csv file
with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Alice", 30, "New York"])
    writer.writerow(["Bob", 25, "Los Angeles"])
    writer.writerow(["Charlie", 35, "Chicago"])

with open("output.csv", "r") as file:
    reader=csv.reader(file,delimiter=",")
    for row in reader:
        print(row)

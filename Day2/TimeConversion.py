#PROG 05 : Time Conversion

# Get seconds from user

seconds = int(input("Enter time in seconds: "))
# Convert seconds to hours, minutes, and seconds
hours = seconds // 3600
minutes = (seconds % 3600) // 60
seconds = seconds % 60

print(f"Time: {hours} HH, {minutes} MM, {seconds} SS")

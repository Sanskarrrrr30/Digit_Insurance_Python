# String Slicing
def string_slicing(s):
    print("Original String: ", str1)
    mid=len(str1)//2
    print("First half: ", str1[:mid])
    print("Second half: ", str1[mid+1:])
    print("First character: ", str1[0])
    print("Middle character: ", str1[mid] if len(str1) % 2 != 0 else "No middle character (even length)")
    print("Last character: ", str1[-1])
    print("Reversed String: ", str1[::-1])

    new_string=str1[0]+str1[mid]+str1[-1]
    print("New String (first, middle, last characters): ", new_string)

str1=input("Enter a string: ")
string_slicing(str1)
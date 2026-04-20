'''
10. Exam Result Processor 
Problem Statement 
Input marks for 5 subjects: 
● If any mark < 35 → FAIL 
● Else average ≥ 75 → DISTINCTION 
● Else PASS 
Input 
m1 m2 m3 m4 m5 
Output 
FAIL / PASS / DISTINCTION 
Sample Input 
80 78 74 90 88 
Sample Output 
DISTINCTION 
Hint: 
First validate failure condition, then classify. 
'''

marks = []
fail = False

for i in range(5):
    mark = float(input())
    if mark < 35:
        fail = True
    marks.append(mark)

if fail:
    print("FAIL")
else:
    avg = sum(marks) / 5
    if avg >= 75:
        print("DISTINCTION")
    else:
        print("PASS")
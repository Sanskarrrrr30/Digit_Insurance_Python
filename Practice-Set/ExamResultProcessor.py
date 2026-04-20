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
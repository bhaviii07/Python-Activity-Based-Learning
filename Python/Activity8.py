#Student Performance Trend Analysis

print("STUDENT PERFORMANCE TREND ANALYSIS")

n = int(input("Enter the number of tests: "))

if n < 2:
    print("Invalid number of tests. Enter at least 2 tests.")
else:
    marks = []
    valid = True

    for i in range(n):
        mark = float(input("Enter marks for test " + str(i + 1) + ": "))

        if mark < 0 or mark > 100:
            print("Invalid marks. Marks must be between 0 and 100.")
            valid = False
            break
        else:
            marks.append(mark)

    if valid:
        total = sum(marks)
        average = total / n

        first = marks[0]
        last = marks[-1]

        print("\n--- Performance Report ---")
        print("First test marks:", first)
        print("Last test marks:", last)
        print("Average marks:", round(average, 2))

        if last > first:
            print("Performance trend: Improving")
        elif last < first:
            print("Performance trend: Decreasing")
        else:
            print("Performance trend: Unchanged")

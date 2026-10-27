#Student Email and Identifiers Validation

print("STUDENT EMAIL AND IDENTIFIERS VALIDATION")

email = input("Enter student email: ")
student_id = input("Enter student ID: ")

# Email validation
if (email.count("@") == 1
        and "." in email.split("@")[1]
        and " " not in email):
    email_valid = True
else:
    email_valid = False

# Student ID validation
if student_id.startswith("STU") and student_id[3:].isdigit():
    id_valid = True
else:
    id_valid = False

# Display results
print("\n--- Validation Results ---")

if email_valid:
    print("Email:", email)
    print("Email status: Valid")
else:
    print("Email status: Invalid")

if id_valid:
    print("Student ID:", student_id)
    print("Student ID status: Valid")
else:
    print("Student ID status: Invalid")

#Read student records from students.txt and calculate the average marks
try:
 total = 0
 count = 0
 with open("students.txt", "r") as file:
 for line_number, line in enumerate(file, start=1):
 if not line.strip():
 continue
 try:
 name, marks_text = line.strip().rsplit(",", 1)
 marks = float(marks_text)
 if not name.strip():
 raise ValueError("Student name is missing.")
 if not 0 <= marks <= 100:
 raise ValueError("Marks are outside the valid range.")
 total += marks
 count += 1
 except ValueError as e:
 print(f"Invalid record on line {line_number}: {e}")
 if count > 0:
 print("Total Students:", count)
 print("Average Marks:", round(total / count, 2))
 else:
 print("No valid student records found.")
except FileNotFoundError:
 print("Student file does not exist.")
except OSError as e:
 print("Unable to read student records:", e)

#Create a json file to store employee details
import json
employee = {
 "employee_id": 101,
 "name": "Rahul",
 "department": "Accounts",
 "salary": 25000
}
try:
 with open("employee.json", "w", encoding="utf-8") as file:
 json.dump(employee, file, indent=4)
 print("Employee data saved successfully.")
except OSError as e:
 print("Unable to save employee data:", e)
Read the JSON file
import json
try:
 with open("employee.json", "r", encoding="utf-8") as file:
 employee = json.load(file)
 print("Employee ID:", employee["employee_id"])
 print("Name:", employee["name"])
 print("Department:", employee["department"])
 print("Salary:", employee["salary"])
except FileNotFoundError:
 print("Employee file not found.")
except json.JSONDecodeError as e:
 print("Invalid JSON format:", e)
except KeyError as e:
 print("Required employee field is missing:", e)
except OSError as e:
 print("File error:", e)

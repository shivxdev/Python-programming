#Read the JSON file
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
 print("F

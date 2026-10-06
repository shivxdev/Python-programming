#Process a large file in chunks
from pathlib import Path
file_path = Path("server.log")
try:
 error_count = 0
 with file_path.open("r", encoding="utf-8") as file:
 for line in file:
 if "ERROR" in line.upper():
 error_count += 1
 print("Total error lines:", error_count)
except FileNotFoundError:
 print("Log file not found.")
except UnicodeDecodeError:
 print("The file could not be decoded using UTF-8.")
except OSError as e:
 print("Unable to process the file:",e)

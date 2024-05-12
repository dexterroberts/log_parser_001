# Created by: Dexter Roberts
# Date Created: 05.11.24
# Last Modified: 05.11.24
# Current Version: 1.0.0
# Description: Log parsing tool to detect patterns 

# Step 1: Import necessary modules
import re

# Step 2: Define a function to parse the log file
def parse_log_file(file_path):
    # Step 3: Open the log file
    with open(file_path, 'r') as file:
        # Step 4: Read each line in the log file
        for line in file:
            # Step 5: Check for specific patterns using regular expressions
            if re.search(r'FATAL ERROR', line):
                print("Found a FATAL error:", line.strip())
            elif re.search(r'Timeout', line):
                print("Found a Timeout:", line.strip())
            elif re.search(r'Retrying attempt', line):
                print("Found a retrying attempt:", line.strip())
            elif re.search(r'Failed', line):
                print("Found a failed attempt:", line.strip())
            # Step 6: Add more conditions for other common error codes or flags
            # For example:
            # elif re.search(r'ERROR_CODE', line):
            #     print("Found an ERROR_CODE:", line.strip())
            # elif re.search(r'ANOTHER_ERROR_CODE', line):
            #     print("Found ANOTHER_ERROR_CODE:", line.strip())

# Step 7: Call the parse_log_file function with the path to your log file
# For example: Copy file path and paste into line 34. Do not remove the 'r' that precedes before the file path.
parse_log_file(r'C:\Users\drob7\VS_Code_Projects\log_parser_001\log_file.txt')

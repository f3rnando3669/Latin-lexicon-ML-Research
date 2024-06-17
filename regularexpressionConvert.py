import os
import re

# Manual File path for where the csv file was at execution
folder_path = r'C:\Users\Liam\Desktop\Summer Research\Computer-Science-Research-Summer\DS1'

# Regular expression made to capture each group of data necessary
regex = r"(>[^ ]+)\s+([^[]+)\s+(\[[^\]]+\])\s+((?:[A-Z]+\n?)+)"

# Iterate over each file in a directory
for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)
    
    # Make sure the file exists
    if os.path.isfile(file_path):
        try:
            with open(file_path, 'r') as file:
                content = file.read()

            matches = re.search(regex, content)
            # When we find the groups strip away whitespaces and join them together with a '/'
            if matches:

                group1 = matches.group(1).strip()
                group2 = matches.group(2).strip()
                group3 = matches.group(3).strip()
                group4 = matches.group(4).replace('\n', '').strip()

                new_content = f"{group1}/{group2}/{group3}/{group4}"

                with open(file_path, 'w') as file:
                    file.write(new_content)

                print(f"File {file_name} updated successfully.")
            else:
                print(f"No match found in {file_name}.")

        except FileNotFoundError:
            print(f"Error: The file {file_name} does not exist.")
        except Exception as e:
            print(f"An error occurred with {file_name}: {e}")
    else:
        print(f"Skipping {file_name} as it is not a file.")

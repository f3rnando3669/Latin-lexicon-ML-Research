import csv
import os

directory = r"C:\Users\Liam\Desktop\Summer Research\Computer-Science-Research-Summer/DS1"
#output_file_name = "full_sequence_list.csv"
output_file_path = r"C:\Users\Liam\Desktop\Summer Research\Computer-Science-Research-Summer\good_boys.csv"

for file_name in os.listdir(directory):
    file_path = os.path.join(directory, file_name)
    
    if os.path.isfile(file_path) and file_path.endswith('.txt'):
        with open(file_path, 'r') as file:
            data = file.read()
        
        data_list = data.split("/")
        
        with open(output_file_path, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(data_list)

print("Data from all text files appended to CSV file successfully.")

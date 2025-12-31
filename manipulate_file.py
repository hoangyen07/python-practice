# function to read a log file and print its conntent
def read_all_log_file(filename='system.log'):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    print(f"📥 Reading all line in {filename} file...")
    print(content)

# function to read each line from log file then save to list and print as list
# read each line in system.log file to list
def read_log_file_to_list(filename='system.log'):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    print(f"📥 Reading each line in {filename} file to list...")
    # print(lines)
    for line in lines:
        print(line.strip()) # strip() is used to remove leading/trailing whitespace
        
# function traverse each line in the log file in order to save the memory
def read_log_file_line_by_line(filename='system.log'):
    with open(filename, 'r', encoding='utf-8') as file:
        print(f"📥 Reading each line in {filename} file line by line...")
        for line in file:
            print(line.strip())
            
# function to override data in output file
def override_output_file(filename='output.txt'):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write("This is new content replacing old content.\n")
    print(f"📝 Overriding content in {filename} file...")

# function to apppend data to output file
def append_output_file(filename='output.txt'):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write("This is appended content to the file.\n")
    print(f"📝 Appending content to {filename} file...")

def hanlde_json_file():
    import json
    
    # string to dictionary
    data = json.loads('{"key": "value", "number": 123}')
    print("📥 Handling JSON data...")
    print(data)
    
    # dictionary to string
    json_string = json.dumps(data)
    print("📤 Converting dictionary back to JSON string...")
    print(json_string)
    
    # read JSON file
    with open('data.json', 'r', encoding='utf-8') as file:
        json_data = json.load(file)
    print("📥 Reading JSON file data.json...")
    print(json_data)
    # print string representation of JSON data
    print("📤 Converting JSON data back to string...")
    json_format_string = json.dumps(json_data, indent=4)
    print(json_format_string)
    
    
def find_error_in_log(file_name='system.log'):
    with open(file_name, 'r', encoding='utf-8') as file:
        count = 0
        for line in file:
            if "ERROR" in line:
                count+=1
                with open('error_report.txt', 'a', encoding='utf-8') as f:
                    f.write(line.split("ERROR")[1])
        print(f'Found {count} errors. Report saved.') 
        with open('error_report.txt', 'r') as file:
            for line in file:
                print(line.strip())   

# optimize code 
def find_error_in_log_optimize(file_name='system.log'):
    
    errors = []
    count = 0
    # open file log to read 
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            if 'ERROR' in line:
                count += 1
                # Lấy phần nội dung sau "ERROR" và xóa khoảng trắng thừa
                errors.append(line.split('ERROR')[1].strip())
                
    # 2. Mở file báo cáo một lần duy nhất để ghi toàn bộ
    if count > 0:
        with open('error_report.txt', 'w', encoding='utf-8') as file:
            for mes in errors:
                file.write(mes + "\n")
    
    print(f'Found {count} errors. Report saved.')

    # 3. Đọc lại để kiểm tra (Optional)
    if count > 0:
        with open('error_report.txt', 'r') as f:
            print("--- Error Report Content ---")
            print(f.read().strip())            

if __name__ == "__main__":
    # read_all_log_file()
    # print("\n-----------------\n")
    # read_log_file_to_list()
    # print("\n-----------------\n")
    # read_log_file_line_by_line()
    # print("\n-----------------\n")
    # override_output_file()
    # print("\n-----------------\n")  
    # read_log_file_line_by_line("output.txt")
    # print("\n-----------------\n")
    # append_output_file()
    # print("\n-----------------\n")  
    # read_log_file_line_by_line("output.txt")
    # print("\n-----------------\n")
    # hanlde_json_file()
    # find_error_in_log()
    find_error_in_log_optimize()
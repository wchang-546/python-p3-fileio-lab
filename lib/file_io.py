def write_file(file_name, file_content):
    with open(f'{file_name}.txt', mode='w') as file_name: 
        file_name.write(file_content)

def append_file(file_name, append_content):
    with open(f'{file_name}.txt', mode='a') as file_name: 
        file_name.write(append_content)

def read_file(file_name):
    with open(f'{file_name}.txt') as file_name: 
        return file_name.read()

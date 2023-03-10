file_path = 'directory.txt'
my_list = ['apple', 'banana', 'orange', 'pear']

with open(file_path, 'a') as file:
    for item in my_list:
        file.write(item + '\n')

print(f'The list {my_list} was written to the file {file_path}.')
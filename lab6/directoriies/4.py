f = open('directory.txt', 'a')
file_path = 'directory.txt'

with open(file_path, 'r') as file:
    line_count = 0
    for line in file:
        line_count += 1

print(f'The file {file_path} has {line_count} lines.')
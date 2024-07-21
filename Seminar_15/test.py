import os

current_file = os.path.realpath(__file__)
current_directory = os.path.dirname(current_file)

print(current_file)
print(current_directory)

path = f'\'{current_file}\''
print(path)
filename = os.path.splitext(os.path.basename(path))[0]
print(filename)


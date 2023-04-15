import os

cwd = "./"
file_name = 'FIG00H00.ANM'
file_data = []

file_path = os.path.join(cwd, file_name)

lines_to_read = 784
start_offset = 0

with open(file_path, 'rb') as file:
    file.seek(start_offset)
    for index in range(0, lines_to_read*16, 4):
        data = file.read(4)
        data = int.from_bytes(data, byteorder = "little")
        file_data.append(data)

pass
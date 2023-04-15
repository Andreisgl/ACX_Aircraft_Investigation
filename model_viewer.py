import os

cwd = "./"
file_path = "FIG00H00.ANM"
ANM_file = ""

file_path = os.path.join(cwd, file_path)


with open(file_path) as ANM:
    ANM_file = ANM.read()
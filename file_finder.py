import glob
import sys
files = glob.glob("*")
files_1 = [file.split(".") for file in files]
file_type = sys.argv[1]
for file in files_1:
    if file_type in file:
        print(file[0])
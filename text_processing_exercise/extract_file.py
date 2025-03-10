file_directory = input().split("\\")
file_and_extension = file_directory[-1].split(".")
print(f"File name: {file_and_extension[0]}\nFile extension: {file_and_extension[1]}")

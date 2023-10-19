from os import remove as delete_file

path = input()

try:
    delete_file(path)
    print(f"{path} succesfully deleted")
except Exception as ex:
    print(f"Fil deleting error: {ex}")
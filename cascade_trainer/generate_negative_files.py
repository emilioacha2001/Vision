import os

cwd = os.path.dirname(os.path.abspath(__file__))
os.chdir(cwd)


object_name = "people"
positive_folder = os.listdir(f"{object_name}/positive")
negative_folder = f"{object_name}/negative/"
print(len(positive_folder))

with open(f"{object_name}/negative.txt", 'w') as f:
    for file_name in os.listdir(f"{object_name}/negative"):
        f.write(f"negative/{file_name}\n")
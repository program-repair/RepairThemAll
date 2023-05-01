import os

def load_paths(dir_path):
    buggy_code_path = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith(".py"):
                buggy_code_path.append(os.path.join(root, file))
    return buggy_code_path
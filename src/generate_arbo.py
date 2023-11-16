import os

def generate_arbo(directory_path):
    # Define the base directory path
    base_directory = 'backevent'

    # List of subdirectories
    subdirectories = ['css', 'js', 'images', 'requires']

    # Create the base directory
    base_directory_path = os.path.join(directory_path, base_directory)
    os.makedirs(base_directory_path)

    # Create the subdirectories within the base directory
    for subdirectory in subdirectories:
        subdirectory_path = os.path.join(base_directory_path, subdirectory)
        os.makedirs(subdirectory_path)

    print(f"Directory structure created at: {base_directory_path}")

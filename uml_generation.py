"""Script for creating UML diagrams."""

import os
import subprocess

uml_dir = "UML"
os.makedirs(uml_dir, exist_ok=True)

# Get the list of Python files in the current directory and its subdirectories
python_files = []
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".py"):
            python_files.append(os.path.join(root, file))

# Run pyreverse for each file and generate dot and png files in the 'uml' directory
for python_file in python_files:
    # Get the base name of the Python file (without the extension)
    base_name = os.path.splitext(os.path.basename(python_file))[0]

    # Construct the output file paths for the dot and png files
    dot_file_path = os.path.join(uml_dir, "classes_" + f"{base_name}.dot")
    png_file_path = os.path.join(uml_dir, f"{base_name}.png")

    # Run pyreverse to generate the dot file
    subprocess.run(
        [
            "pyreverse",
            "-p",
            base_name,
            "-m",
            "y",
            "-a",
            "1",
            python_file,
            "-d",
            f"{uml_dir}",
        ],
    )

    # Generate PNG image from the .dot file
    subprocess.run(["dot", "-Tpng", dot_file_path, "-o", png_file_path])

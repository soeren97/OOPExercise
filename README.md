# OOP excercise
This exercise is designed to familiarize myself with object oriented programing, universal modeling language and SQL. 

The code is executed from `main.py` and creates an SQL server as well as adding some items to it and fetching them again.

Furthermore UML diagrams can ge generated using the `uml_generation.py` script to visualize the classes used in all scripts.

## Installation Guide

### Prerequisites:
- Anaconda installed
- pip installed (usually comes with Anaconda)
- MySQL server installed
- Graphviz installed (for UML)

### Steps:

1. **Clone the Repository:**
`git clone https://github.com/soeren97/OOPExcercise.git`

2. **Navigate to the Repository Directory:**
`cd */OOPExcercise`

3. **Create a Virtual Environment (Optional but Recommended):**
`conda create -n your-env-name python=3.9`

4. **Activate the Virtual Environment:**
`conda activate your-env-name`

5. **Install Required Packages:**
`pip install .`

6. **Verify Installation:**
Ensure all dependencies are installed successfully without any errors.

7. **Deactivate Virtual Environment (If Created):**
`conda deactivate`

8. **Create config.json.**
Create a file containing the fields username, password, database and table in the repocetory directory.

### Additional Notes:

- **Virtual Environment:** Creating a virtual environment is a good practice to isolate project dependencies from other projects and the system Python environment.
- **pip Install:** The `pip install .` command installs the necessary packages specified in the `setup.py` file from the current directory.
- **requirements** The required packages can be found in the `setup.py` file as the variable `INSTALL_REQQUIRES`.
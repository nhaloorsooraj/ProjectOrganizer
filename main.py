import os

# Get project name and full custom path from the user
dirname = input("Enter Project name: ")
pathname = input("Enter full path: ")

# Create the full path for the project directory
projectpath = os.path.join(pathname, dirname)

# Create subdirectories within the project path
Sdirname = os.path.join(projectpath, "Source")
blenderpath = os.path.join(Sdirname, "Blender")
renderpath = os.path.join(projectpath, "RenderFiles")
resolvepath = os.path.join(Sdirname, "Resolve")
aepath = os.path.join(Sdirname, "AfterEffects")
prpath = os.path.join(Sdirname, "Premier")
outputpath = os.path.join(projectpath, "FinalOutput")

# Try to create the directory structure
try:
    os.mkdir(projectpath)  # Create the main project directory
    os.mkdir(Sdirname)  # Create the 'Source' directory
    os.mkdir(blenderpath)  # Create 'Blender' directory
    os.mkdir(resolvepath)  # Create 'Resolve' directory
    os.mkdir(renderpath)  # Create 'RenderFiles' directory
    os.mkdir(aepath)  # Create 'AfterEffects' directory
    os.mkdir(prpath)  # Create 'Premier' directory
    os.mkdir(outputpath)  # Create 'FinalOutput' directory
    
    print(f"Directory '{projectpath}' created successfully.")
except FileExistsError:
    print(f"Directory '{projectpath}' already exists.")
except PermissionError:
    print(f"Permission denied: Unable to create '{projectpath}'.")
except Exception as e:
    print(f"An error occurred: {e}")

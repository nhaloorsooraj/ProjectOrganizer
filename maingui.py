import os
import tkinter as tk
from tkinter import messagebox, filedialog

# Function to create project directories
def create_project():
    dirname = entry_project_name.get()  # Get project name from entry widget
    pathname = entry_path.get()  # Get the full path from entry widget
    
    if not dirname or not pathname:
        messagebox.showwarning("Input Error", "Both fields are required.")
        return
    
    # Create the full project path
    projectpath = os.path.join(pathname, dirname)
    Sdirname = os.path.join(projectpath, "Source")
    blenderpath = os.path.join(Sdirname, "Blender")
    renderpath = os.path.join(projectpath, "RenderFiles")
    resolvepath = os.path.join(Sdirname, "Resolve")
    aepath = os.path.join(Sdirname, "AfterEffects")
    prpath = os.path.join(Sdirname, "Premier")
    outputpath = os.path.join(projectpath, "FinalOutput")

    # Try creating directories
    try:
        os.makedirs(blenderpath, exist_ok=True)
        os.makedirs(resolvepath, exist_ok=True)
        os.makedirs(renderpath, exist_ok=True)
        os.makedirs(aepath, exist_ok=True)
        os.makedirs(prpath, exist_ok=True)
        os.makedirs(outputpath, exist_ok=True)
        messagebox.showinfo("Success", f"Project '{dirname}' created successfully at {pathname}")
    except FileExistsError:
        messagebox.showerror("Error", f"Directory '{projectpath}' already exists.")
    except PermissionError:
        messagebox.showerror("Error", f"Permission denied to create directory at '{pathname}'")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to browse directory using file dialog
def browse_path():
    selected_path = filedialog.askdirectory()  # Open file dialog to select folder
    entry_path.delete(0, tk.END)  # Clear the entry box
    entry_path.insert(0, selected_path)  # Insert the selected path

# Create main application window
root = tk.Tk()
root.title("Project Directory Creator")

# GUI layout: Labels and Entry fields
label_project_name = tk.Label(root, text="Project Name:")
label_project_name.grid(row=0, column=0, padx=10, pady=10)
entry_project_name = tk.Entry(root, width=40)
entry_project_name.grid(row=0, column=1, padx=10, pady=10)

label_path = tk.Label(root, text="Full Path:")
label_path.grid(row=1, column=0, padx=10, pady=10)
entry_path = tk.Entry(root, width=40)
entry_path.grid(row=1, column=1, padx=10, pady=10)

# Browse button to open file dialog
btn_browse = tk.Button(root, text="Browse", command=browse_path)
btn_browse.grid(row=1, column=2, padx=10, pady=10)

# Create Project button
btn_create = tk.Button(root, text="Create Project", command=create_project)
btn_create.grid(row=2, column=1, padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()

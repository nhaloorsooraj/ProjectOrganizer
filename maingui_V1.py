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
    outputpath = os.path.join(projectpath, "FinalOutput")

    try:
        os.makedirs(projectpath, exist_ok=True)  # Always create the main directory
        os.makedirs(Sdirname, exist_ok=True)  # Always create Source directory
        os.makedirs(outputpath, exist_ok=True)  # Always create FinalOutput directory
        
        if blender_var.get():  # Blender directory
            os.makedirs(blenderpath, exist_ok=True)
            if render_var.get():  # RenderFiles directory
                os.makedirs(renderpath, exist_ok=True)

        if resolve_var.get():  # Resolve directory
            os.makedirs(os.path.join(Sdirname, "Resolve"), exist_ok=True)
        if ae_var.get():  # AfterEffects directory
            os.makedirs(os.path.join(Sdirname, "AfterEffects"), exist_ok=True)
        if pr_var.get():  # Premier directory
            os.makedirs(os.path.join(Sdirname, "Premier"), exist_ok=True)

        messagebox.showinfo("Success", f"Project '{dirname}' created successfully at {pathname}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to browse directory using file dialog
def browse_path():
    selected_path = filedialog.askdirectory()  # Open file dialog to select folder
    entry_path.delete(0, tk.END)  # Clear the entry box
    entry_path.insert(0, selected_path)  # Insert the selected path

# Function to toggle the visibility of RenderFiles checkbox based on Blender selection
def toggle_render_checkbox():
    if blender_var.get():  # If Blender is selected, show RenderFiles checkbox
        chk_render.grid(row=5, column=0, padx=20, pady=5, sticky="w")
    else:  # If Blender is not selected, hide RenderFiles checkbox
        chk_render.grid_remove()

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

# Checkboxes for optional subdirectories
blender_var = tk.IntVar()
render_var = tk.IntVar()
resolve_var = tk.IntVar()
ae_var = tk.IntVar()
pr_var = tk.IntVar()

# Blender checkbox
chk_blender = tk.Checkbutton(root, text="Blender", variable=blender_var, command=toggle_render_checkbox)
chk_blender.grid(row=3, column=0, padx=10, pady=5, sticky="w")

# RenderFiles checkbox (initially hidden, only shown if Blender is checked)
chk_render = tk.Checkbutton(root, text="RenderFiles", variable=render_var)
# Initially not placed; will be added dynamically

# Resolve, AfterEffects, and Premier checkboxes
chk_resolve = tk.Checkbutton(root, text="Resolve", variable=resolve_var)
chk_resolve.grid(row=4, column=1, padx=10, pady=5, sticky="w")
chk_ae = tk.Checkbutton(root, text="AfterEffects", variable=ae_var)
chk_ae.grid(row=4, column=0, padx=10, pady=5, sticky="w")
chk_pr = tk.Checkbutton(root, text="Premier", variable=pr_var)
chk_pr.grid(row=3, column=1, padx=10, pady=5, sticky="w")

# Create Project button
btn_create = tk.Button(root, text="Create Project", command=create_project)
btn_create.grid(row=6, column=1, padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()

import os
import json
import argparse
import tkinter as tk
from tkinter import filedialog, messagebox

def directory_to_dict(path, include_content):
    directory_dict = {'name': os.path.basename(path), 'type': 'directory', 'children': []}
    try:
        for entry in os.scandir(path):
            if entry.name.startswith('.'):
                continue
            if entry.is_dir(follow_symlinks=False):
                directory_dict['children'].append(directory_to_dict(entry.path, include_content))
            elif entry.is_file(follow_symlinks=False):
                file_dict = {'name': entry.name, 'type': 'file'}
                if include_content:
                    try:
                        with open(entry.path, 'r', errors='ignore') as file:
                            content = file.read()
                        file_dict['content'] = content
                    except Exception as e:
                        file_dict['content'] = f"Error reading file: {str(e)}"
                directory_dict['children'].append(file_dict)
    except PermissionError:
        directory_dict['children'].append({'name': 'Permission Denied', 'type': 'error'})
    return directory_dict

def save_directory_structure(directory, include_content):
    directory_structure = directory_to_dict(directory, include_content)
    json_path = os.path.join(directory, 'directory_structure.json')
    with open(json_path, 'w') as json_file:
        json.dump(directory_structure, json_file, indent=4)
    return json_path

def main(directory=None, include_content=False):
    if directory is None:
        directory = os.path.abspath(os.path.dirname(__file__))
    json_path = save_directory_structure(directory, include_content)
    print(f'Directory structure saved to {json_path}')

def cli():
    parser = argparse.ArgumentParser(description='Generate a JSON representation of a directory structure.')
    parser.add_argument('directory', nargs='?', default=os.path.abspath(os.path.dirname(__file__)),
                        help='The directory to analyze')
    parser.add_argument('--include-content', action='store_true', help='Include file contents in the JSON output')
    args = parser.parse_args()
    
    main(args.directory, args.include_content)

def tk_interface():
    def select_directory():
        directory = filedialog.askdirectory()
        if directory:
            json_path = save_directory_structure(directory, include_content_var.get())
            messagebox.showinfo("Success", f"Directory structure saved to {json_path}")

    root = tk.Tk()
    root.title("Directory to JSON")
    root.geometry("300x100")

    frame = tk.Frame(root, padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    select_button = tk.Button(frame, text="Select Directory", command=select_directory)
    select_button.grid(row=0, column=0, padx=5, pady=5)

    include_content_var = tk.BooleanVar()
    include_content_check = tk.Checkbutton(frame, text="Include file content", variable=include_content_var)
    include_content_check.grid(row=1, column=0, padx=5, pady=5)

    root.mainloop()

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        cli()
    else:
        tk_interface()

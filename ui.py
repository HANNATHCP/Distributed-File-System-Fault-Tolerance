import tkinter as tk
from tkinter import simpledialog, messagebox
import metadata_server as ms
import storage_node as sn
import os

# ---------------- Window Setup ----------------
root = tk.Tk()
root.title("Distributed File System")
root.geometry("450x420")
root.configure(bg="#1e1e2f")

# ---------------- Title ----------------
title = tk.Label(
    root,
    text="Distributed File System\nwith Fault Tolerance",
    font=("Helvetica", 16, "bold"),
    fg="white",
    bg="#1e1e2f",
    pady=20
)
title.pack()

# ---------------- Button Style ----------------
def styled_button(text, command, color):
    return tk.Button(
        root,
        text=text,
        command=command,
        width=25,
        height=2,
        font=("Arial", 11, "bold"),
        bg=color,
        fg="white",
        activebackground="#444",
        relief="raised",
        bd=3
    )

# ---------------- Functions ----------------
def upload_file():
    filename = simpledialog.askstring("Upload File", "Enter file name:")
    if not filename:
        return

    if not os.path.exists(filename):
        messagebox.showerror("Error", "File does not exist!")
        return

    nodes = ms.add_file(filename)
    for n in nodes:
        sn.store_file(filename, n)

    messagebox.showinfo("Success", f"File stored on nodes: {nodes}")

# def download_file():
#     filename = simpledialog.askstring("Download File", "Enter file name:")
#     if not filename:
#         return

#     nodes = ms.get_file_nodes(filename)
#     if not nodes:
#         messagebox.showerror("Error", "File not found!")
#         return

#     for node in nodes:
#         if ms.is_node_alive(node):
#             sn.retrieve_file(filename, node)
#             messagebox.showinfo("Success", f"File downloaded from node {node}")
#             return

#     messagebox.showerror("Error", "All nodes containing the file have failed!")
def download_file():
    filename = simpledialog.askstring("Download", "Enter file name:")
    if not filename:
        return

    nodes = ms.get_file_nodes(filename)   # this returns a list, e.g. [3, 2]

    if not nodes:
        messagebox.showerror("Error", "File not found!")
        return

    node = nodes[0]   # pick the first node, e.g. 3

    sn.retrieve_file(filename, node)
    messagebox.showinfo("Success", f"File downloaded from node {node}")

def list_files():
    files = ms.list_files()
    if not files:
        messagebox.showinfo("Files", "No files found")
    else:
        messagebox.showinfo("Files", "\n".join(files))

def fail_node():
    node = simpledialog.askinteger("Simulate Node Failure", "Enter node number:")
    if node is None:
        return

    ms.fail_node(node)
    messagebox.showinfo("Status", f"Node {node} has failed!")

# ---------------- Buttons ----------------
styled_button("Upload File", upload_file, "#4CAF50").pack(pady=6)
styled_button("Download File", download_file, "#2196F3").pack(pady=6)
styled_button("List Files", list_files, "#9C27B0").pack(pady=6)
styled_button("Simulate Node Failure", fail_node, "#FF5722").pack(pady=6)
styled_button("Exit", root.quit, "#607D8B").pack(pady=12)

# ---------------- Run ----------------
root.mainloop()

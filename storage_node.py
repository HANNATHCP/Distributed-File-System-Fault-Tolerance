import shutil

def store_file(filename, node):
    destination = f"node{node}/{filename}"
    shutil.copy(filename, destination)

def retrieve_file(filename, node):
    source = f"node{node}/{filename}"
    destination = f"downloaded_{filename}"
    shutil.copy(source, destination)

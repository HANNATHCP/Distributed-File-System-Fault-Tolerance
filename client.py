import metadata_server as ms
import storage_node as sn
import os

while True:
    print("\n1. Upload File")
    print("2. Download File")
    print("3. List Files")
    print("4. Simulate Node Failure")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        filename = input("Enter file name: ")

        if not os.path.exists(filename):
            print("File does not exist!")
            continue

        nodes = ms.add_file(filename)

        for n in nodes:
            sn.store_file(filename, n)

        print("File stored on nodes:", nodes)

    elif choice == "2":
        filename = input("Enter file name: ")
        nodes = ms.get_file_nodes(filename)

        if not nodes:
            print("File not found in system")
            continue

        for n in nodes:
            try:
                sn.retrieve_file(filename, n)
                print("File downloaded from node", n)
                break
            except:
                continue

    elif choice == "3":
        files = ms.list_files()
        if not files:
            print("No files stored")
        for f, n in files.items():
            print(f, "-> nodes", n)

    elif choice == "4":
        node = int(input("Enter node number to fail (1/2/3): "))
        ms.fail_node(node)
        print("Node", node, "has failed!")

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice")

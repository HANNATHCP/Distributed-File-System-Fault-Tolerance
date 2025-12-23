import random
from common import TOTAL_NODES, REPLICA_COUNT

file_table = {}
node_status = {}

def init_nodes():
    for i in range(1, TOTAL_NODES + 1):
        node_status[i] = True

def add_file(filename):
    alive_nodes = [n for n in node_status if node_status[n]]
    chosen_nodes = random.sample(alive_nodes, REPLICA_COUNT)
    file_table[filename] = chosen_nodes
    return chosen_nodes
def get_file_nodes(filename):
    return file_table.get(filename, [])

def list_files():
    return file_table

def fail_node(node):
    node_status[node] = False

init_nodes()


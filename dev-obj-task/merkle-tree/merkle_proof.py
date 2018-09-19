from node import Node
from utils import *


def k_distance(root, k, level): # Recursively finds all of the nodes a certain distance from root.
    if root is None:
        return
    if k == 0:
        level.append(root) # Nodes compiled into a list.
    else:
        k_distance(root._left, k - 1,level)
        k_distance(root._right, k - 1, level)
    return level

def merkle_proof(tx, merkle_tree):
    """Given a tx and a Merkle tree object, retrieve its list of tx's and
    parse through it to arrive at the minimum amount of information required
    to arrive at the correct block header. This does not include the tx
    itself.

    Return this data as a list; remember that order matters!
    """
    #### YOUR CODE HERE
    data = []
    nodes = []

    if len(merkle_tree.leaves) == 1:
        data = []
        return data

    tx_list = merkle_tree.leaves
    tx_index = tx_list.index(tx)
    height = merkle_tree._height
    curr_row = height
    is_right = tx_index % 2 == 1  # Zero-indexed

    if is_right:
        data.append(Node('l', tx_list[tx_index - 1]))
        nodes.append(tx)
    else:
        data.append(Node('r', tx_list[tx_index + 1]))
        nodes.append(tx)
    curr_row -= 1

    while curr_row > 0:
        level = k_distance(merkle_tree._root, curr_row, [])
        index = 0
        for ind,cur_node in enumerate(level):
            if not isinstance(nodes[height-curr_row-1],str):
                first_hash_poss = concat_and_hash_list([data[height-curr_row-1].tx,nodes[height-curr_row-1].data])
                second_hash_poss = concat_and_hash_list([nodes[height-curr_row-1].data,data[height-curr_row-1].tx])
            else:
                first_hash_poss = concat_and_hash_list([data[height - curr_row - 1].tx, nodes[height - curr_row - 1]])
                second_hash_poss = concat_and_hash_list([nodes[height-curr_row-1],data[height-curr_row-1].tx])
            if cur_node.data == first_hash_poss or cur_node.data == second_hash_poss :
                index = ind
                nodes.append(cur_node)
        is_right = index % 2 == 1  # Zero-indexed
        if is_right:
            data.append(Node('l', level[index - 1].data))
        else:
            data.append(Node('r', level[index + 1].data))
        curr_row -= 1

    data.reverse()
    return data


def verify_proof(tx, merkle_proof):
    """Given a Merkle proof - constructed via `merkle_proof(...)` - verify
    that the correct block header can be retrieved by properly hashing the tx
    along with every other piece of data in the proof in the correct order
    """
    #### YOUR CODE HERE
    curr_row = len(merkle_proof)-1

    hash = tx

    while curr_row >= 0:
        if merkle_proof[curr_row].direction == 'l':
            hash = concat_and_hash_list([merkle_proof[curr_row].tx, hash])
        else:
            hash = concat_and_hash_list([hash,merkle_proof[curr_row].tx])
        curr_row -= 1

    return hash


    
